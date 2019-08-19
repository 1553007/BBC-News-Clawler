# check duplicate lines, remove and save in new file
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

# check not captipal first word in lines
outfile = open('train_new.en', "w", encoding='utf-8')
with open('train.en', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if "{\\" not in line:
            # print(line)
            outfile.write(line)
outfile.close()

# line.replace("(c", "")
# line.replace("﻿", "")


# check wrong split line
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