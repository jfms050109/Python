a={1,2}
b={2,3}
print(a)
print(b)
a.add("ola")
print (a)
b.update(['da','para','adcionar','varios','itens','ao','conjunto','usando','o','update'])
print(b)
b.remove('o')
print(b)
b.discard("da")
print(b)
a.clear()
b.clear()
print(b)
print(a)
a={'1','2'}
b={"3","4"}
c=a.union(b)
print(c)


d={1,2,3}
e={2,3,4}
print(e.intersection(d))

print(e.difference(d))
print(d.difference(e))








print(e.issubset(d))