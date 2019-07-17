import re

if __name__ == "__main__":
    infile = open("Output/bbc_eng - temp.txt")
    for line in infile:
        text = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", line)
        with open("Output/bbc_eng_edited.txt", "a") as outfile:
                outfile.write(text)
    infile.close()