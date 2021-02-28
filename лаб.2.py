import math
x=float(input('x='))
t=float(input('t='))
z=((9*math.pi*t+10*math.cos(x))/(math.sqrt(t)-math.fabs(math.sin(t))))*math.pow(math.e,x)
print('z={0:.2f}' . format (z))


import math
x=input("Enter x:")
x=int(x)
z=math.log2(x**3)+math.log10(x)
print('z=',z)


import math
a=input('Enter a:')
a=int(a)
z=(math.pow(a,1/3)*math.sin(math.pow(a,5)))/(a+math.exp(a))
print('z=',z)


import math
a=input('Enter a:')
a=int(a)
b=input('Enter b:')
b=int(b)
z=(math.sqrt(b-a))/(a**2)*abs(math.cos(math.radians(15)))/(math.sin(math.radians(15)))
print('z=',z)


import math
x=input('Enter x:')
x=int(x)
z=(math.pow(x,1/5))/(math.exp(abs(x+1)))
print('z=',z)


import math
x=input('Enter x:')
x=int(x)
z=(math.exp(3+x))/(9*(math.cos(x)/math.sin(x)))+math.tan((math.pow(x,3))/3)
print('z=',z)


import math
x=input('Enter x:')
z=math.loge(abs(x-15))+math.sqrt(math.pow(x,4/5))+math.sqrt((math.exp(3x)+4),1/3)
print('z=',z)


