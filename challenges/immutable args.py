def increaseSalary(money, bonus):
    money = money + (money * 0.2)
    
    return money + bonus
salary = 5000 
print(salary)
newSalary = increaseSalary (salary, 1000)
print (newSalary)