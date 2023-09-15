class Parent:
    def myMethod(self):
        print("Parent Method")
        return


class Child(Parent):
    def myMethod(self):
        print("Child Method")
        return


c = Child()
c.myMethod()
super(Child, c).myMethod()  # 調用父類別 myMedthod
