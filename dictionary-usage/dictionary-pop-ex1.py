dic = {
    "shammi": "red",
    "trijal": "blue",
    "mumma": "purple",
    "vasu": "brown",
    "peda": "orange"
}
original_length = len(dic)
print(original_length)
key_to_del = ""
for index in dic:
    print(index)
    if (dic[index]) == "blue":
        key_to_del = index

dic.pop(key_to_del)
print(dic)
