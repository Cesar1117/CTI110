#Cesar Flores
#4/14/24
#P2HW1_FloresCesar
#program with addtional lists
print('This program calculates and displays travel expenses')
print('Enter Budget:',end='')
budget=float(input())
print('Enter your travel destination:',end='')
destination=input()
print('How much do you think you will spend on gas?',end='')
gas=float(input())
print('Approximately,how much will you need for accomodation/hotel?',end='')
hotel=float(input())
print('Last,how much do you need for food?',end='')
food=float(input())
print('Travel Expenses')
print('Location:',destination)
print(f'Initial Budget:${budget:.2f}')
print(f'Fuel:${gas:.2f}')
print(f'Accomodation:${hotel:.2f}')
print(f'Food:${food:.2f}')
remain=budget-gas-hotel-food
print(f'Remaining Budget:${remain:.2f}')