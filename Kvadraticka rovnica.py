import math
a=int(input('Zadaj hodnotu pre a: '))
b=int(input('Zadaj hodnotu pre b: '))
c=int(input('Zadaj hodnotu pre c: '))
#d -> diskriminant
d=(b*b)-(4*a*c)
if d < 0:
    print('Rovnica nemá riešenie')
else:
    x=((-b)+math.sqrt(d))/(2*a)
    y=((-b)-math.sqrt(d))/(2*a)

    print('x1 je',x, 'a x2 je',y )