from math import sqrt

l = [("ali", "umar", "usman"), ("hashim","zarak", "ahmed")]
def func(l):
    out = []
    for i  in l:
        out.append(i[::-1])
    return out
# print(func(l))  

def distance(p1,p2,p3):
    x1 = sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    x2 = sqrt((p1[0]-p3[0]**2)+(p1[1]-p3[1])**2)
    if x1<x2:
        return 2
    elif x1 == x2:
        return -1
    else:
        return 3
# print(distance((0,2),(4,2),(0,0)))    
x = (10,10)
y = (10,20)
def savemoney(x, y):
    out =[]
    a = x[0]
    b = y[0]
    t= x[1]+y[1]
    for i in range(7):
        a += b
        out.append((a,t))
        t += y[1] 
    return out    
print(savemoney(x, y))
    
    