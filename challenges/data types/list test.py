data = [1,2,3,4,5,6]
print (len(data))

del data[2]
print (data)
print(len(data))
if 1 in data:
    print("3 jest na liście")
for v in data:
    print(v)

for v in data:
    print("element listy z dodaną wartością 2 =", v+2)

for p in data:
    print("element z listy data pomnożony x2 =", p*2)