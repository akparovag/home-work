x=float(input('x: '))  #14

if x<0:
    y=(x**2)+1
else: 
    if x>=1: 
        y=4*x-1
    else:
        y=2*x+1

print('y: ',y)

a=int(input('a: '))

if a==0:  #15
    print('x-любое')
else:
    c=3/a
    if a>0:
        print('x<c')
    else:
        print('x>c')

a, b = int(input('a: ')), int(input('b: '))  #16

if a!=0:
    print('Уравнение имеет один корень b/a')
else:
    if b!=0:
        print('Любое число-корень уравнение')
    else:
        print('Уравнение не имеет корней')
        

a=int(input('a: '))  #17
b=int(input('b: '))

if a==0:
    if b==0:
        print('x-любое')
    else:
        print('решений нет')

else:
    c=b/a
    if a>0:
        x>c
        print('x>c')
    else:
        x<c
        print('x<c')


a=int(input('a: '))  #18
b=int(input('b: '))
c=int(input('c: '))
min=5


if min>b:
    min==b

if min>c:
    min==c
print('min',min)


st=int(input('st: '))  #19
if st<5:
    zp=130
if st<=5:
    zp=180
else:
    zp=180+(st-15)*10
print('zp:', zp)


x=int(input('x: '))  #20
a=int(input('a: '))
b=int(input('b: '))

if x<10:
    y=x+a
if x<=23:
    y=x+b
else:
    y=x+a**2
print('y: ',y)


a=int(input('a: '))  #21
b=int(input('b: '))
c=int(input('c: '))
if a>c:
    print('кошка не подходит')

if c<b:
    print('кошка подходит')
else:
    print('кошка не подходит')


a=int(input('a: '))  #22
b=int(input('b: '))
c=int(input('c: '))
x=int(input('x: '))
y=int(input('y: '))

if a>b:
    r=a
    a=b
    b=r

if b>c:
    r=b
    b=c
    c=r

if a>b:
    r=a
    a=b
    b=r

if x>y:
    r=x
    x=y
    y=r

if a<x and b<y:
    print('Пройдёт')
else:
    print('Не Пройдёт')    
