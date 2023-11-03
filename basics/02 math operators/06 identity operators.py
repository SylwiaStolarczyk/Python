#operatory tożsamości
a = [1,2,3,4,5]
b = [1,2,3,4,5]

print( a is b) #false
print( a in b)

strData = "test"

print( dir(strData))
print(strData.upper())

intData = 10
print( dir(intData))

b = a
print( a is b)
a.append(77)
print(a)
print(b)

print(a is not b)

c= [3,4,5]
print( a is not c)