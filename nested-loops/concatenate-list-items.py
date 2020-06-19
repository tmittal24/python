list1 = ["m", "n", "t"]
list2 = ["y", "o", "i"]
list3 = [i + j for i, j in zip(list1,list2)]
print (list3)
for index_list1, list1_val_at_index in enumerate(list1):
    for index_list2, list2_val_at_index in enumerate(list2):
        # print(index_list1, list1_val_at_index, index_list2, list2_val_at_index)
        if (index_list1 == index_list2):
            print(list1_val_at_index, list2_val_at_index)
