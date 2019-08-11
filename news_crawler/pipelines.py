# Pipelines used in News Crawler are defined here.
#
# Pipelines defined here are added to ITEM_PIPELINES setting

from   scrapy.exceptions import DropItem
from   scrapy import signals
from   pydispatch import dispatcher
from   scrapy.exporters import JsonItemExporter
from   readability import Document
from   scrapy.conf import settings
from   datetime import datetime
from   lxml import etree
# import geograpy
import requests, html2text
import pymongo, logging
from bs4 import BeautifulSoup
import re
import os

class NewsCrawlerPipeline(object):
    def process_item(self, item, spider):
        return item

remove_words = [
    "\\n",
    "\"",
    "\\t",
    "[", "]", "‘", "’", "·"
    "Media playback is unsupported on your device",
    "Media caption",
    "Image copyright",
    "Images caption",
    "Image caption",
    "Read more",
    "Getty Images",
    u"Bản quyền hình ảnh"
]

class NewsTextPipeline(object):
    '''
    DESCRIPTION:
    ------------
    This pipeline is used for extracting news article text.
    '''

    def process_item(self, item, spider):
        '''
        DESCRIPTION:
        ------------
        For each news item, corresponding news text is extracted
        using python library 'readability'.

        RETURNS:
        --------
        News item with 'newsText' field updated is returned.
        '''
        try:
            response = requests.get(item['newsUrl'])
            doc      = Document(response.text)
            content  = Document(doc.content()).summary()

            soup = BeautifulSoup(content, "html.parser")

            tags_to_delete = soup.findAll('figure')
            for tag in tags_to_delete:
                tag.extract()

            articleText = soup.get_text(" ").replace(u'\xa0', u' ')
            
            if (articleText != ""):
                articleText = articleText.replace("\\'", "'")

                for word in remove_words:
                    if word in articleText:
                        articleText = articleText.replace(word, u"")

                articleText = re.sub(" +", " ", articleText) # remove multi-spaces
                
                if (len(articleText) >= 20):
                    item['newsText'] = articleText
        except Exception:
            raise DropItem("Failed to extract article text from: " + item['newsUrl'])  
        return item

class DropIfEmptyPipeline(object):
    '''
    DESCRIPTION:
    ------------
    This function drops news item if either of following
    mandatory fields are empty:
    1. newsHeadline
    2. newsUrl
    3. newsText
    4. author
    '''
    def process_item(self, item, spider):
        if ((not item['newsHeadline']) or (not item['newsUrl'])
             or (not item['newsText']) or (not item['author'])):
            raise DropItem()
        else:
            return item

class DuplicatesPipeline(object):
    '''
    DESCRIPTION:
    ------------
    This pipeline is used to remove the duplicate news items.
    '''
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['newsUrl'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['newsUrl'])
            return item

class MongoDBPipeline(object):
    '''
    DESCRIPTION:
    ------------
    * This pipeline is used to insert data in to MongoDB.
    * MongoDB setting are provided in settings.py
    '''
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_URI']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if ((data == 'newsUrl' or data == 'newsHeadline' or data == 'newsText'
                 or data == 'author') and not data):
                valid = False
                raise DropItem('News Item dropped, missing ' + data)
        if valid:
            self.collection.insert(dict(item))
            logging.info('News Article inserted to MongoDB database!')
        
        filename = "Output/bbc.en.txt"
        if (spider.language == 'vn'):
            filename = "Output/bbc_vn.txt"
        elif (spider.language == 'zh'):
            filename = "Output/bbc_zh.txt"
        
        myfile = open(filename, "a", encoding='utf-8')
        sentences = list(map(str.strip, re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", item['newsText'])))
        for each_sentence in sentences:
            if (len(each_sentence) >= 20):
                myfile.write(each_sentence.lstrip() + "\n")
        myfile.close()
        return item
