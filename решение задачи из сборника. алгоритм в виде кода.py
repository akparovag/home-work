x=0 #5задача a
y=1
if x>=0:
    print('x,y')
elif x<=0:
    print('x,y')

x=1 #б    
y=1
if x>=0:
    print('x,y')
elif x<=0:
    print('x,y')

x=-5 #в
y=1
if x>=0:
    print('x,y')
elif x<=0:
    print('x,y')

import math #задача6 а

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
    print('z,x,y')

print('введите цену и количество') #задача8
a = int(input("a = "))
b = int(input("b = "))
s=a*b

if s>500:
    print('s')
elif s<500:
    s=s*0.9
    print('s')    




    

