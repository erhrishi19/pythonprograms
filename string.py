# Creatin a string
s="Welcome Blackmoon"
print(s)
print(len(s))
print(s[0])
print(s[8])
s="""I am BlackMoon
 and i am learning
 python write now"""
print(s)
print(len(s))
print(s[0])
print(s[5])


#Slicing a string
s1="Welcome  Blackmoon"
print(s1)
print(len(s1))
print(s1[0:])
print(s1[:14])
print(s1[:])
print(s1[0:4])

#Steps In Slicing
print("Steps in Slicing :")
s1="Welcome Blackmoon"

print(s1[0:len(s1):2])
print(s1[0:len(s1):3])
print(s1[len(s1):0:-1])
print(s1[::-1])

#Strip the spaces
s="""                    I am BlackMoon
 and i am learning
 python write now       """
print(s)
print(s.strip())
print(s.lstrip())
print(s.rstrip())