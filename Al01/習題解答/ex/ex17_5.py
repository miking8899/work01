# ex17_5.py
import hashlib

data1 = hashlib.md5()                                # 建立data物件
data1.update(b'Ming-Chi Institute of Technology')    # 更新data物件內容
print('md5    = ', data1.hexdigest())

data2 = hashlib.sha256()                             # 建立data物件
data2.update(b'Ming-Chi Institute of Technology')    # 更新data物件內容
print('sha256 = ', data2.hexdigest())

data3 = hashlib.sha512()                             # 建立data物件
data3.update(b'Ming-Chi Institute of Technology')    # 更新data物件內容
print('sha512 = ', data3.hexdigest())










