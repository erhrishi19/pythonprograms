s={10,20,30,"xyz",30,15, 10}
print(s)
print(type(s))
s.update([22,33,44,55])
print(s)
s.remove(22)
print(s)

#frozenset type
s1=frozenset(s)
