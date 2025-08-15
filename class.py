
class A:
    @staticmethod
    def something():
        print("hello")

    def __init__(self):
        self.var1=200
class B(A):

    def __init__(self):
        super().__init__()
        self.var=100
    def something2(self):
        super().something()
b=B()
print(b.something2())
