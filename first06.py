

def chagelist(mylist):
    mylist.append([1, 2, 3, 4, 5])
    print("mylist append ", mylist)
    mylist.extend([3, 4, 5, 6, 8])
    print("mylist extend ", mylist)
    print("函數值: ", mylist)

    return


mainlist = [100, 99, 98, 97]
print(mainlist)

chagelist(mainlist)
print(" mainlist chage = ", mainlist)
