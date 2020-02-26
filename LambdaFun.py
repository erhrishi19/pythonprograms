from functools import reduce
#simple function for cube
def cu(a):
    return a**3
r=cu(5)
print(r)

#Lambda expression
lr=lambda n: n**3
print(lr(5))

#if else in lambda

a=lambda x: 'Yes' if x%2==0 else 'No'
print(a(4))
print(a(7))

#Filter in lambda
ls=[10,11,12,13,14,15]
r=list(filter(lambda x:x%2==0,ls))
print(r)

#map in lamba
ls=[10,11,12,13,14,15]
re=list(map(lambda x:x*2,ls))
print(re)

#reduce for lambda

ls=[10,11,12,13,14,15]
r=reduce(lambda x,y:x+y,ls)
print(r)