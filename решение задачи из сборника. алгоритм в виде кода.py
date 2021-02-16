a=0 #1 задача
b=0
a,b=b,a
print(a,b)

a=0
b=5
a,b=b,a
print(a,b)

a=10
b=20
a,b=b,a
print(a,b)

a=10 
b=10
a,b=b,a
print(a,b)

a=3 #задача2
b=4
import math
y= math.sqrt(a**2+b**2)
p=y+a+b
print(p)

a=0
b=3
import math
y= math.sqrt(a**2+b**2)
p=y+a+b
print(p)

a=6
b=8
import math
y= math.sqrt(a**2+b**2)
p=y+a+b
print(p)

a=9
b=12 
import math
y= math.sqrt(a**2+b**2)
p=y+a+b
print(p)

a=1 #3 задача
b=2
c=3
s=a+b
s=s+c
print(a)

a=9
b=0
c=1
s=a+b
s=s+c
print(s)

a=5
b=6
c=9
s=a+b
s=s+c
print(s)

a=8 #задача4
b=2
import math
g= math.sqrt(a*b)
print(g)

x=0 #5задача a
y=1
if x>=0:
    print(x,y)
elif x<=0:
    print(x,y)

x=1 #б    
y=1
if x>=0:
    print(x,y)
elif x<=0:
    print(x,y)

x=-5 #в
y=1
if x>=0:
    print(x,y)
elif x<=0:
    print(x,y)

import math #задача6 

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr >= 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")



import math #задача7
print('введите цифры')
x = int(input("x = "))
y = int(input("y = "))

if x == 0:
    print('ошибка')
elif x != 0:
    z=y/x
    print(z,x,y)

print('введите цену и количество') #задача8
a = int(input("a = "))
b = int(input("b = "))
s=a*b

if s>500
    print(s)
elif s<500:
    s=s*0,9
    print(s)

a = int(input("a = ")) #9
b = int(input("b = "))

if a == b:
    print(a)
elif a>b:
    b=b-a
    print(a)
else:
    a=a-b
    print(a)

n = float(input('введите')) #10
s=0
i=0

while i<=n:
    print(s)
    i=i+2
    s=s+i
    continue

i=0 #11
p=1
i=i+1

while p<=30:
    print(i)
    p=p*i
    i=i+1

q=float(input('введите ')) #12
s=0
i=1

if s > q:
    print(i-2)
elif s>q:
    print(i-2)
    s += i
    i += 1

n=3b #13
i=1
s=0
s=s+(3*i+2)
i=i+1
while i<=n:
    s=s+(3*i+2)
    i=i+1
    print(s)
    

    

