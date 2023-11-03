data = ("Ala", "Ola", "Kasia")
print (data)

names = data + ("Rafał",)
print (names)
print(len(names))
print(type(names))

emptyTuple=()
print(type(emptyTuple))

print(names[1])
print(names[-1])
print(names[1:3])

cars = (("dodge", "ford"), 
        ("pontiac"))

print (cars[0][0])

if "ford" in cars[0]:
    print("Ford w krotce nr 1")

#del cars

#del names[0]

