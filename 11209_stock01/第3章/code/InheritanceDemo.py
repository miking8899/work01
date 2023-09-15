# !/usr/bin/env python
# coding=utf-8
class Employee(object):   # 定義一個父類別
    def __init__(self,name):
        self.__name = name  
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name        
    def login(self):    # 父類別中的方法
        print("Employee In Office")
    def changeSalary(self,newSalary):
        self._salary = newSalary
    def get_Salary(self):
        return self._salary    
# 定義一個子類別，繼承Employee類別          
class Manager(Employee):    
    def login(self):    # 在子類別中覆蓋父類別的方法
        print("Manager In Office")
        print("Check the Account List")
    def attendWeeklyMeeting(self):
        print("Manager attend Weekly Meeting")
# 使用類別 
manager = Manager("Peter")
print(manager.get_name())   # Peter
manager.login()             # 呼叫子類別的方法，Manager In Office
manager.changeSalary(30000)
print(manager.get_Salary()) # 30000
manager.attendWeeklyMeeting()
