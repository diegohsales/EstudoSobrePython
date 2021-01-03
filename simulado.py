"""
class Demo:
    def __init__(self):
        self.x = 1

    def change(self):
        self.x = 10


class Demo_derived(Demo):
    def __init__(self):
        super().__init__()
        self.x = 10

    def change(self):
         self.x = self.x + 1
         return self.x

obj = Demo_derived()
print(obj.change())



def inserir(item):
    if item in total:
        total[item] += 1
    else:
        total[item] = 1


total = {}
inserir('Apple')
inserir('Ball')
inserir('Apple')
print(len(total))


class A:
    def __init__(self):
        self.i = None

class B(A):
    def __init__(self):
        self.j = None

    def display(self):
        print(self.i)

obj = B()
obj.j = 2
obj.display()


a = {'a': 1, 'b': 2, 'c': 3}
print(a[a])
"""
