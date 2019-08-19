# python .\remove_stopwords.py <input file> <train_new.en>
# python .\remove_stopwords.py train.en train_new.en

from nltk.corpus import stopwords
from file_read_backwards import FileReadBackwards
import re
import sys
if (".en" in sys.argv[1]):
    # English
    stop_words_en = set(stopwords.words('english'))
    with open(sys.argv[1], 'r', encoding='utf-8') as inFile, open(sys.argv[2], 'w', encoding='utf-8') as outFile:
        for line in inFile.readlines():
            line = ' '.join([word for word in line.split()
                             if word not in stop_words_en])
            outFile.write(line + "\n")
elif (".vi" in sys.argv[1]):
    # Vietnamese
    stopwords = list()
    with FileReadBackwards('stopwords.vi', encoding="utf-8") as stop_words_vi_file:
        for word in stop_words_vi_file:
            stopwords.append(word)
    with open(sys.argv[1], 'r', encoding='utf-8') as inFile, open(sys.argv[2], 'w', encoding='utf-8') as outFile:
        for line in inFile.readlines():
            for word in stopwords:
                if re.search(r"\b" + re.escape(word) + r"\b", line):
                    line = re.sub(" +", " ", line.replace(word, ""))
            outFile.write(line)
