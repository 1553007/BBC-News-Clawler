import copy
from googletrans import Translator
import random

infile = open("bbc.en", "r", encoding='utf-8')
outfile_vi = open("bbc_para.vi", "a", encoding='utf-8')
outfile_en = open("bbc_para.en", "a", encoding='utf-8')

count = 0

list_lines = list(infile.readlines())

while (count < 1):
    line = random.choice(list_lines)
    check = True
    while(check):
        try:
            translator = Translator()
            translated_line_vi = translator.translate(line.replace('\n', ''), src='en', dest='vi').text
            print("*** Translated line: " + str(count))
            check = False
        except Exception as e:
            print(str(e))
            
    outfile_en.write(line)
    outfile_vi.write(translated_line_vi + "\n")
    count = count + 1

print("Done.")