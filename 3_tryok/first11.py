
try:

    fo = open("README.md", "r")

    print("文件名 :", fo.name)
    print("文件 模式:", fo.mode)
    print("文件關閉否:", fo.closed)
    print("文件", fo.__sizeof__)

    str = fo.read(100)

    print("FO file string :", str)
except:
    print("file try error")
finally:
    print("Close file OK")
    fo.close()
