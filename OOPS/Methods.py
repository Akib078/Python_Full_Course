class Methods:
    a = 10

    def demo(self):
        c = self.a + self.a
        print(self.a)
        print(c)

    def demo2(self,x,y):
        print("demo2 =",x+y)

methodObj = Methods()

methodObj.demo()

methodObj.demo2(10,40)