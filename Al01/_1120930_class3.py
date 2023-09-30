#方法二: 使用 property 函數
class Person:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # Getter function
    def get_first_name(self):
        return self._first_name

    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)
    
person = Person('travis')
person.name # 'travis'

#方法三: 定義動態計算屬性的方法
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    #注意: 只有確定要對屬性執行其他額外的操作時才應該用到 property，否則，它會讓代碼變得很臃腫，迷惑閱讀者。程序運行起來變慢很多。如下例子。
    class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self.first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value