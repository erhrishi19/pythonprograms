#Function with multiple return values
a=5
def x(a,b):
    x=a+b
    y=a-b
    z=a*b
    print("Value of a :",a)
    return x,y,z
r=x(10,5)
print(r)
print("Values of a:",a)
f=x
f(6,5)
f(7,6)
f(8,7)