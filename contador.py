from collections import Counter
l=[1,1,1,4,5,2]
c=Counter(l)
print(c)
Counter({1: 3, 4: 1, 5: 1, 2: 1})
Counter('palabra')
Counter({'a': 3, 'b': 2, 'r': 1, 'p': 1, 'l': 1})
c=Counter('palabra')
print(c)
animales='gato perro canario gato perro gato'
Counter(animales.split())
Counter({'gato': 3, 'perro': 2, 'canario': 1})
c=Counter(animales.split())


animales='gato perro canario gato perro gato'
c=Counter(animales.split())

print(c.most_common(1))
print(c.most_common(2))
print(c.most_common(3))

[('perro', 2), ('canario', 1), ('gato', 1)]


l=[10,20,30,40,10,20,30,10,20,10]
c=Counter(l)
print