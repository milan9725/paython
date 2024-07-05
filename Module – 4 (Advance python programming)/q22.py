class P:
    def get_data(self,a,b):
        self.a=a
        self.b=b
    def put_data(self):
        print("P:",self.a)
        print("Q:",self.b)

a1=P()
a=int(input("Enter P: "))
b=int(input("Enter Q: "))

a1.get_data(a,b)
a1.put_data()