str = 'Hello World!'
print(str)
print ( len(str))
print(type(str))

print(str [11])
print(str[len(str)-1])

print(str[0:5])
print (str *3)

strX3 = str *3
print(strX3)

str2 = str + " and Hello again!"
print(str2)

print(str2[6:]) #od 6 elementu do końca

print (str2[::3]) #co 3ci element wyświetlaj

multiLine  = """Pierwsza linia
Druga linia
Trzecia linia
"""

print(multiLine)
multiLine2 = "Pierwsza \"linia \n Druga \tlinia\n Trzecia\t linia"
print (multiLine2)