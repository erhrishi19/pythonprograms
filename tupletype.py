#Creation of tuple
tpl=(10,20,30,("BLACK","moon"))
print(tpl)
print(tpl*3)
print(tpl.count(30))
print(tpl.index(30))

#Adding list to tuple
ls=[10,20,30,40]
print(ls)
tpl1=tuple(ls)
print(tpl1)