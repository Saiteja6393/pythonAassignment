# def add(x,y):
#     return x+y
# def sub(x,y):
#     if x>y:
#         return x-y
#     else:
#         return y-x
    
# def mul(x,y):
#     return x*y

# def div(x,y):
#     if x>0 and y>0:
#         return x/y
#     else:
#         return
class Employee():
    def __init__(self,name,pos):
        self.name=name
        self.pos=pos
    def show(self):
        print("Employee name:",self.name)
        print("Employee Position:",self.pos)
        