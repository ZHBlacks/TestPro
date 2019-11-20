'''
Created on 2019年11月12日

@author: Veryci
'''
a = 1
def d():
    global a
    a = 2
if __name__ == '__main__':
    d()
    print(a)
    
def add():
    a = 1
    b = a + 3
    print(b)
add() 

def add1(e = 1, d = 1):
    f = e + d
    return f
print(add1())