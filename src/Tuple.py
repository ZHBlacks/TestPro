'''
Created on 2019年11月12日

@author: Veryci
'''
a = (1,2,"d",(1,"dd"))
print(a[0])
print(a[-1])
print(a[3])

c = [1,2,"d",(1,"dd")]
d = [4,["a",3],"ddd"]
c.extend(d)
print(c)
d = c + d
print(d)

