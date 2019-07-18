import re

remove_words = [
    "Media playback is unsupported on your device",
    "Media caption",
    "Image copyright",
    "Images caption",
    "Image caption",
    "Read more",
    "Getty Images",
    "Bản quyền hình ảnh",
    "\\n",
    "\"",
    "\\t",
    "[", "]"
]

if __name__ == "__main__":
    infile = open("Output/bbc_vn.txt", "r", encoding='utf-8')
    for line in infile:
        for word in remove_words:
            if word in line:
                print(word)
                print(line)
                print(line.replace(word, "***"))
    infile.close()