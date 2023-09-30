##創建可管理屬性: 為了給某個實例的屬性增加除 訪問 與 修改 之外的其他處理邏輯，比如 類型檢查 或 合法性驗證。

#方法一 (data, getter, setter, deleter)
# 屬性要求特定類型，無法刪除屬性
class Person:
    def __init__(self, first_name):
        self._first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

a = Person('Guido')
print(a)
a.first_name # 'Guido'
a.first_name = 42 
print(a)
# Calls the setter
# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
#     File "prop.py", line 14, in first_name
#         raise TypeError('Expected a string')
# TypeError: Expected a string
#del a.first_name
# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
# AttributeError: can`t delete attribute


