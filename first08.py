
def printinfo(arg1, *vararg2):
    print("輸出")
    print(arg1)

    for var in vararg2:
        print(var)
    return


printinfo("any meth", 2, 3, 5, 99, 78, 334)
printinfo("test 2", 3, 5, 66, 88, 9, 34, 56, 77, 90)
