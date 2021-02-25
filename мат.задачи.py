from math import * #15

k=int(input("k:"))
z=int(input("z:"))

if k<1:
    x=k*z**3
else:
    k>=1
    x=z*(z+1)


y=(log10(1+x**2)+cos(x+1))
print('y', y)


import math  #16

a=int(input("a:"))
b=int(input("b:"))
z=int(input("z:"))

if z<a*b:
    x= math.sqrt((a**2)+(b**2)*z)
else:
    z>=a*b
    x= (math.sin(z)**2) + abs(a*b*z)

y= a*x+b*x* math.cos(math.sqrt(x)) / x + a*b
print('y', y)


import math  #17

b=int(input("b:"))
z=int(input("z:"))

if z<1:
    x=z/b
else:
    z>=1
    x= math.sqrt(z*b)**3

y= -math.pi+(math.cos(x**3)**2) + (math.sin(x**2)**3)
print('y', y)


import math  #18

z=int(input("z:"))

if z<1:
    x=(z**3)+0.2
else:
    z>=1
    x= z + math.log10(z)

y= (math.cos(x**2)**3) + math.sin(x**3)**2
print('y', y)


import math  #19

e=float(2.71)
z=int(input("z:"))

if z<-1:
    x=-z/3
else:
    z>=0
    x=abs(z)

y= math.log10(x+0.5) + ((e**x)-e**-x)
print('y', y)


import math  #20

z=int(input("z:"))

if z<0:
    x=z
else:
    z>=0
    x= math.sin(z)

y= (2/3 * math.sin(x)**2) - (3/4 * math.cos(x)**2)
print('y', y)


import math  #21

k=int(input("k:"))
z=int(input("z:"))
c=int(input("c:"))
d=int(input("d:"))

if z<0:
    x=(z**2)-z
else:
    z>=0
    x=z**3

y= math.sin(c*x+(d**2)+k*x**2)**3
print('y', y)


import math  #22

z=int(input("z:"))

if z>=0:
    x=2*z+1
else:
    z<0
    x=math.log10((z**2)-z)

y=(math.sin(x)**2) + (math.cos(x**3)**5) + math.log10(x**2/5)
print('y', y)


import math  #23

b=int(input("b:"))
z=int(input("z:"))

if z<=0:
    x=(z**b)+abs(b/2)
else:
    z>0
    x=math.sqrt(z)

y=(1/math.cos(x))+math.log10(abs(math.atan(x/2)))
print('y', y)


import math  #24

e=float(2.71)
z=int(input("z:"))

if z>=1:
    x=z-1
else:
    z<1
    x=(z**2)+1

y=(e**math.sin(x)**3) + math.log10(x+1)/math.sqrt(x)
print('y', y)


import math  #25

e=float(2.71)
z=int(input("z:"))

if z>0:
    x=1/(z**2)+2*z
else:
    z<=0
    x=1-z**3

y=2*(e**(-3*x))-4*x**2/(math.log10(abs(x))+x)
print('y', y)  


import math  #26

z=int(input('z:'))
e=float(2.71)

if z<=0:
    x=(z**2)+5
else:
    z>0
    x=1/math.sqrt(z-1)

y= (math.sin((x**2)-1)**3) + math.log10(abs(x))+e**x    
print('y', y)

from math import *  #27

z=int(input("z:"))
n=int(input("n:"))
k=int(input("k:"))
m=int(input("m:"))
e=float(2.71)

if z>1:
    x= e**z + z
else:
    z<=0
    x= (z**2)+1
    
import math
y= math.sin(n*x) + math.cos(k*x)+ math.log10(m*x)    
print('y', y)

from math import * #28

z=int(input("z:"))

if z>0:
    x= math.sqrt(z)
else:
    z<=0
    x=(3*(z**3)-z)-5

y=math.cos(5*x) + math.sin(1/5*x) + math.e**x    
print('y', y)
