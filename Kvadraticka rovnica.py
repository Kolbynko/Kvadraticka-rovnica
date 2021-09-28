import math

a=int(input('Zadaj hodnotu pre a: '))
b=int(input('Zadaj hodnotu pre b: '))
c=int(input('Zadaj hodnotu pre c: '))
#d -> diskriminant
d=(b*b)-(4*a*c)
if d < 0:
    print('Rovnica nemá riešenie')
else:
    print('x1 je',int((-b)+math.sqrt(d)/(2*a)))
    print('x2 je',int((-b)-math.sqrt(d)/(2*a)))