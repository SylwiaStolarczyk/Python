number = 4
while number > 0:
    print(number)
    number -= 1

print("Kod po pętli")

num = 1
while num <6:
    print(num)
    num +=1

licz = 0
while True:
    print("Wprowadź liczbę lub exit aby zakończyć")
    strData = input()
    if strData == "exit": break
    licz += int(strData)
    print("wartość po dodaniu liczby:", str(licz))

number = 3
while number > 0:
    print(number)
    number-=1
else:
    print("number po pętli:", str(number))