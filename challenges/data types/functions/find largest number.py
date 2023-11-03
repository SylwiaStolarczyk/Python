def findLargest(num1,num2):
    if num1==num2:
        return print('Podane liczby są równe')
    elif num2>num1:
        return print(f'Liczba {num2} jest większa od {num1}')
    else:
        return print(f'Liczba {num1} jest większa od {num2}')
    
findLargest(50,12)
        