class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def Find(self):
        print("Area of the reactangle :",self.length*self.width)

r1=Rectangle(1,10)
r1.Find()