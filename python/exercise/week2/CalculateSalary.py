def calculate_salary(basic, hra, da, bonus=0):
    total_salary = basic + hra + da + bonus
    return total_salary

salary = calculate_salary(5000, 2000, 1500)
print("The total salary without Bonus is: " + str(salary))

salary = calculate_salary(5000, 2000, 1500, 500)
print("The total salary with Bonus is: " + str(salary))
