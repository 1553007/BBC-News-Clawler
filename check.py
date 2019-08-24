# CASE 1: check duplicate lines, remove and save in new file
# outfile = open('train.vi', "w", encoding='utf-8')
# with open('train_dup.vi', 'r', encoding='utf-8') as f:
#     seen = set()
#     for i, line in enumerate(f):
#         line_lower = line.lower()
#         if line_lower in seen:
#             print(str(i) + ";")
#         else:
#             outfile.write(line)
#             seen.add(line_lower)
# outfile.close()

# CASE 2: check not captipal first word in lines
# outfile = open('train_new.en', "w", encoding='utf-8')
# with open('train.en', 'r', encoding='utf-8') as f:
#     for i, line in enumerate(f):
#         if "{\\" not in line:
#             # print(line)
#             outfile.write(line)
# outfile.close()

# CASE 3:
# line.replace("(c", "")
# line.replace("﻿", "")


# CASE 4: check wrong split line
# outfile = open('train_new.vi', "w", encoding='utf-8')
# with open('train.vi', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     skipline = False
#     for i in range(0, len(lines) - 1):
#         if (not skipline):
#             line = lines[i]
#             nextline = lines[i + 1]
#             if "(" in line and ")" in nextline:
#                 print("> " + str(i))
#                 outfile.write(line.replace("\n", "") + nextline)
#                 skipline = True
#             else:
#                 outfile.write(line)
#         else:
#             skipline = False
# outfile.close()

# CASE 5: find all words contain & character
# infile = open('html_entities.txt', "r", encoding='utf-8')
# existed = infile.readlines()
# infile.close()
# outfile = open('html_entities.txt', "a", encoding='utf-8')

# list_inFile = ["train.en", "train.vi", "tst2012_test.en",
#                "tst2012_test.vi", "tst2013_val.en", "tst2013_val.vi"]
# for each_file in list_inFile:
#     infile = open(each_file, "r", encoding='utf-8')
#     unique_words = set(infile.read().split())
#     unique_words = list(unique_words)
#     unique_words = sorted(unique_words, key=str.lower)
#     print(len(unique_words))
#     for word in unique_words:
#         if "&" in word and word + "\n" not in existed:
#             outfile.write(word + "\n")
#             existed.append(word)
# outfile.close()

# CASE 6: remove words contain & character
{
    "&#91;": "[",  # delete
    "&#93;": "]",  # delete
    "&amp;": "&",
    "&apos;": "'",
    "&quot;": "\""  # delete
}
# list_file = ["train.en", "train.vi", "tst2012_test.en",
#              "tst2012_test.vi", "tst2013_val.en", "tst2013_val.vi"]
list_file = ["train_para.en",
             "train_para.vi","bbc.en","bbc.vi"]
for each_file in list_file:
    infile = open(each_file, "r", encoding='utf-8')
    outfile = open("new_" + each_file, "w", encoding='utf-8')
    print("> File " + each_file)
    for i, line in enumerate(infile):
        if "&" in line:
            # if "&" == line[0]:
            #     print(*Line " + str(i) + ": " + line)
            while " &#91; " in line:
                line = line.replace(" &#91; ", " ")
            while "&#91; " in line:
                line = line.replace("&#91; ", "")

            while " &#93; " in line:
                line = line.replace(" &#93; ", " ")
            while " &#93;" in line:
                line = line.replace(" &#93;", "")

            while " &amp; " in line:
                line = line.replace(" &amp; ", " & ")
            while "&amp; " in line:
                line = line.replace("&amp; ", "&")
            while " &amp;" in line:
                line = line.replace(" &amp;", "&")
            while "& amp ;" in line:
                line = line.replace("& amp ;", "&")
            while "&amp ;" in line:
                line = line.replace("&amp ;", "&")

            while " &apos; " in line:
                line = line.replace(" &apos; ", " ' ")
            while "&apos; " in line:
                line = line.replace("&apos; ", "'")
            while " &apos;" in line:
                line = line.replace(" &apos;", "'")
            while "&apos;" in line:
                line = line.replace("&apos;", "'")

            while " &quot; " in line:
                line = line.replace(" &quot; ", " ")
            while "&quot; " in line:
                line = line.replace("&quot; ", "")
            while " &quot;" in line:
                line = line.replace(" &quot;", "")
            while " & quot ; " in line:
                line = line.replace(" & quot ; ", " ")
            while "& quot ; " in line:
                line = line.replace("& quot ; ", "")
            while " & quot ;" in line:
                line = line.replace(" & quot ;", "")
            while "&quot;" in line:
                line = line.replace("&quot;", "")

            while " &lt ; em &gt ; &lt ; / em &gt ; " in line:
                line = line.replace(" &lt ; em &gt ; &lt ; / em &gt ; ", " ")
            while "&lt ; em &gt ; " in line:
                line = line.replace("&lt ; em &gt ; ", "")
            while " &lt ; / em &gt ;" in line:
                line = line.replace(" &lt ; / em &gt ;", "")
            while "& lt ; em & gt ; " in line:
                line = line.replace("& lt ; em & gt ; ", "")
            while " & lt ; / em & gt ;" in line:
                line = line.replace(" & lt ; / em & gt ;", "")
            while "& lt ; " in line:
                line = line.replace("& lt ; ", "")
            while " & gt ;" in line:
                line = line.replace(" & gt ;", "")
            while "&lt ; " in line:
                line = line.replace("&lt ; ", "")
            while " &gt ;" in line:
                line = line.replace(" &gt ;", "")

            while (" &lt ; i &gt ; &lt ; / i &gt ; " in line):
                line = line.replace(" &lt ; i &gt ; &lt ; / i &gt ; ", " ")
            while ("&lt ; i &gt ; " in line):
                line = line.replace("&lt ; i &gt ; ", "")
            while (" &lt ; / i &gt ;" in line):
                line = line.replace(" &lt ; / i &gt ;", "")

            while ("... ..." in line):
                line = line.replace("... ...", "...")
            while (". ." in line):
                line = line.replace(". .", ".")

            while (" / b / " in line):
                line = line.replace(" / b / ", " ")
            while ("/ b / " in line):
                line = line.replace("/ b / ", "")

            while (" i / i" in line):
                line = line.replace(" i / i", "")

            while (" ; " in line):
                line = line.replace(" ; ", " , ")
        if ":" in line:
            index = -1
            index = line.find(":")
            words = list(line[:index].split())
            check_all_cap = True
            for word in words:
                if (word.islower()):
                    check_all_cap = False
            if (check_all_cap == True):
                line = line[(index + 2):]
            while (" : " in line):
                line = line.replace(" : ", " ")
        while (" -- " in line):
            line = line.replace(" -- ", " ")
        while ("--" in line):
            line = line.replace("--", " ")
        while ("  " in line):
            line = line.replace("  ", " ")

        outfile.write(line)
    outfile.close()
