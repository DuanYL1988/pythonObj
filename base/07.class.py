#=======================================================================
# 1.类的用法主要是面向对象编程,用途和java类似
# 2.定义方法 class Module():
# 3.构造函数 def __init__():
# 4.self相当于java的this,构造函数时需要在传参数中声明,但是调用时不用传递
#=======================================================================
class Figure():
    '''构造函数'''
    def __init__(self,name,origin,buyDate):
        self.name = name
        self.origin = origin
        self.buyDate = buyDate

    def printInfo(self):
        print(self.name.title())

figure = Figure('hikari','ZenoBlade','2020/5/20')
figure.printInfo()
