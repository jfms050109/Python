import math
a=1
b=1
c=-1
try:
    
    res1=((0-1)*b+math.sqrt(b*b+(0-4)*a*c))/(2*a)
    res2=((0-1)*b-math.sqrt(b*b+(0-4)*a*c))/(2*a)
    print(res1)
    print(res2)
    if math.sqrt(b*b+(0-4)*a*c)!= int(math.sqrt(b*b+(0-4)*a*c)):
        print('raizes aproximadas')
except:
    print('delta é negativo ou a é igual a zero')
