#Cesar Flores
#04/14/24
#P2HW2_FloresCesar
#Program a grade test average 
print('Enter grade for Module 1:',end='')
module_1=float(input())
print('Enter grade for Module 2:',end='')
module_2=float(input())
print('Enter grade for Module 3:',end='')
module_3=float(input())
print('Enter grade for Module 4:',end='')
module_4=float(input())
print('Enter grade for Module 5:', end='')
module_5=float(input())
print('Enter grade for Module 6:', end='')
module_6=float(input())
print('Results')
grades={module_1, module_2, module_3, module_4, module_5, module_6}
average = sum(grades)/6
print(f'Lowest Grade:{min(grades)}')
print(f'Highest Grade:{max(grades)}')
print(f'Sum of Grades:{sum(grades)}')
print(f'Average:{average:.2f}')