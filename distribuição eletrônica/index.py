sub = []
s=0
z=int(input("protons: "))
sub=[]
    
for ia in range(z):
    i=ia+1
    if i<3 or (i>10 and i<13)or(i<21 and i>18) or (i<39 and i>36)or(i<57 and i>54)or(i<89 and i>86):
        s+=1
        print(f"{s}s{s}")
print(sub)