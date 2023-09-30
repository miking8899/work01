import time

class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        print("CLASS METH =",t.tm_year, t.tm_mon, t.tm_mday )
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

#a = Date(2012, 12, 21) # Primary
c= Date.today()
print("Alternate:=",c)

b = Date.today() # Alternate

print(b) 















