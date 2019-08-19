import os, io, codecs
import sys
from underthesea import word_tokenize
path = sys.argv[1]
def sorted_stopwords_list(stopwords_list):
    stopwords_list.sort(key = lambda s: len(s), reverse=True)
    return stopwords_list

def load_vietnamese_stopwords():
    vi_stopwords_list = []
    with io.open("stopwords.vi", 'r', encoding='utf-8') as f:
        for index, line in enumerate(f):
            if line == '':
                continue
            line = line.replace('\n','')
            if line not in vi_stopwords_list:
                vi_stopwords_list.append(line)
        f.close()
    return sorted_stopwords_list(vi_stopwords_list)

#main
assert os.path.isfile(path)
with io.open(path, 'r', encoding='utf-8') as f:
    stopwords_list = load_vietnamese_stopwords()
    fo = codecs.open(sys.argv[2], "w", "utf-8")
    for line in f:
        if line == '':
            continue
        parts = word_tokenize(line)
        line2 = ""
        for idx, word in enumerate(parts):
            found = False
            for stopword in stopwords_list:
                index = word.find(stopword)
                if index >= 0:
                    found = True
                    break
            if found:
                line = line.replace(' ' + word + ' ',' ', 1)
        fo.write(line)
    fo.close()
exit()