# create new files without duplicate lines
# with open('bbc_para.en', 'r', encoding='utf-8') as f:
#     unique_lines = set(f.readlines())
# with open('bbc_para_no_dups.en', 'w', encoding='utf-8') as f:
#     f.writelines(unique_lines)

# with open('bbc_para.vi', 'r', encoding='utf-8') as f:
#     unique_lines = set(f.readlines())
# with open('bbc_para_no_dups.vi', 'w', encoding='utf-8') as f:
#     f.writelines(unique_lines)

# create new files with original orders
# en file
# with open('bbc_para_no_dups.en', 'r', encoding='utf-8') as f:
#     unique_lines = set(f.readlines())

# bbc_en = open("bbc_para.en", "r", encoding='utf-8')
# outfile_en = open("bbc_para_final.en", "a", encoding='utf-8')
# for cnt, line in enumerate(bbc_en):
#     if line in unique_lines:
#         outfile_en.write(line)
#         unique_lines.remove(line)

# # vi file
# with open('bbc_para_no_dups.vi', 'r', encoding='utf-8') as f:
#     unique_lines = set(f.readlines())

# bbc_vi = open("bbc_para.vi", "r", encoding='utf-8')
# outfile_vi = open("bbc_para_final.vi", "a", encoding='utf-8')
# for cnt, line in enumerate(bbc_vi):
#     if line in unique_lines:
#         outfile_vi.write(line)
#         unique_lines.remove(line)

# CREATE VALIDATION AND TEST FILES FROM 1 FILE
outfile_val_en = open("bbc_para_val.en", "a", encoding='utf-8')
outfile_test_en = open("bbc_para_test.en", "a", encoding='utf-8')
outfile_val_vi = open("bbc_para_val.vi", "a", encoding='utf-8')
outfile_test_vi = open("bbc_para_test.vi", "a", encoding='utf-8')

with open("bbc_para_dup.en", "r", encoding='utf-8') as infile_en:
    num_lines_en = sum(1 for line in infile_en)

    infile_en.seek(0)  # offset of 0
    count = 1
    for line in infile_en:
        if (count < num_lines_en / 2):
            outfile_val_en.write(line)
        else:
            outfile_test_en.write(line)
        count = count + 1

with open("bbc_para_dup.vi", "r", encoding='utf-8') as infile_vi:
    num_lines_vi = sum(1 for line in infile_vi)

    infile_vi.seek(0)  # offset of 0
    count = 1
    for line in infile_vi:
        if (count < num_lines_vi / 2):
            outfile_val_vi.write(line)
        else:
            outfile_test_vi.write(line)
        count = count + 1