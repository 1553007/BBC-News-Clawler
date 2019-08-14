import requests
from   readability import Document
from bs4 import BeautifulSoup
import re, os, json
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from mtranslate import translate

remove_words = ["\\n", "\"", "\\t", "[", "]", "‘", "’", "·"]
stop_words = set(stopwords.words('english')) 

def getFirstContent(soup):
    p_sentences = list()
    div = soup.find('div', {'class': 'mw-parser-output'})
    if (div is None):
        return ''
    children = div.findChildren(recursive=False)
    for child in children:   
        if (child.name == 'h2' or child.name == 'h3'):
            break
        if (child.name == 'p'):
            if (child.text == "\\n\\n"):
                break
            tags_to_delete = child.findAll('sup')
            if (tags_to_delete is not None):
                for tg in tags_to_delete:
                    tg.extract()
            articleText = child.get_text(" ").replace(u'\xa0', u' ')
            articleText = articleText.replace("\\'", "'")
            for word in remove_words:
                if word in articleText:
                    articleText = articleText.replace(word, u"")
            # remove the characters between the parentheses and brackets
            articleText = re.sub("[\(\[].*?[\)\]]", "", articleText)
            # remove multi-spaces
            articleText = re.sub(" +", " ", articleText)
            sentences = list(map(str.strip, re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", articleText)))
            for each_sentence in sentences:
                if (len(each_sentence) >= 10):
                    p_sentences.append(each_sentence)
    return p_sentences

def getSentences(response, outfile):
    doc      = Document(response.text)
    content  = Document(doc.content()).summary()

    soup = BeautifulSoup(content, "html.parser")

    delete_tags = ['figure']
    for tag in delete_tags:
        tags_to_delete = soup.findAll(tag)
        if (tags_to_delete is not None):
            for tg in tags_to_delete:
                tg.extract()
    tags_to_delete = soup.findAll('p', text="\\n")
    if (tags_to_delete is not None):
        for tg in tags_to_delete:
            tg.extract()
    tags_to_delete = soup.findAll('p', {"class": "shortdescription"})
    if (tags_to_delete is not None):
        for tg in tags_to_delete:
            tg.extract()

    p_sentences = getFirstContent(soup)
    if (p_sentences == ''):
        return False
    for sen in p_sentences:
        outfile.write(sen + "\n")
    outfile.close()
    return True


def getContentOnWiki(link, rec=True):
    visitedUrlFile = "visited_urls.txt"
    try:
        fileUrls = open(visitedUrlFile, 'r', encoding='utf-8')
    except IOError:
        visitedUrls = []
    else:
        visitedUrls  = [url.strip() for url in fileUrls.readlines()]
        fileUrls.close()

    if str(link) in visitedUrls:
        print('Visited link!')
        return

    fileUrls.close()
    if (link[8:10] == 'vi'):
        link_lang2 = link.replace('https://vi', 'https://en')
        outfile = open("train.vi", "a", encoding='utf-8')
        outfile_lang2 = open("train.en", "a", encoding='utf-8')
    elif (link[8:10] == 'en'):
        translated_vi = translate(link[30:], 'vi')
        link_lang2 = 'https://vi.wikipedia.org/wiki/' + translated_vi
        outfile = open("train.en", "a", encoding='utf-8')
        outfile_lang2 = open("train.vi", "a", encoding='utf-8')
    else:
        print('No support!')
        return
    # print("Get response from: " + link + " ...")
    response = requests.get(link)
    # print("Get response from: " + link_lang2 + " ...")
    response_lang2 = requests.get(link_lang2)
    if (response.status_code == 404 or response_lang2.status_code == 404):
        print('No bilingual websites here!')
        return
        
    visited_file = open("visited_urls.txt", "a", encoding='utf-8')
    visited_file.write(link + "\n")
    visited_file.close()

    if (getSentences(response, outfile)):
        getSentences(response_lang2, outfile_lang2)
        
    print("Crawled data from: " + link)




# main
# CHANGE INPUT FILE HERE 'tst2013.en' <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
data = [line.strip() for line in open('bbc.en', 'r', encoding='utf-8')]
unique_words = set()
for text in data:
    word_tokens = word_tokenize(text)
    tags = pos_tag(word_tokens)
    nouns = [word for word,pos in tags if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
    for word in nouns:
        w = word.lower()
        if w not in stop_words: 
            unique_words.add(w)

print("Number of nouns: " + str(len(unique_words)))

for word in unique_words:
    getContentOnWiki('https://en.wikipedia.org/wiki/' + word)
print("Done.")

# getContentOnWiki('https://en.wikipedia.org/wiki/corn')

# f = open('train.vi', 'r', encoding='utf-8')
# outfile = open("train.2.vi", "a", encoding='utf-8')
# for line in f:
#     # remove the characters between the parentheses and brackets
#     line = re.sub("[\(\[].*?[\)\]]", "", line)
#     # remove multi-spaces
#     line = re.sub(" +", " ", line)
#     outfile.write(line)