#Cesar Flores
#4/7/24
#P1LAB2_FloresCesar
#program with basic numbers and equations
print('This program calculates and displays travel expenses')
print('Enter Budget:',end='')
budget=int(input())
print('Enter your travel destination:',end='')
destination=input()
print('How much do you think you will spend on gas?',end='')
gas=int(input())
print('Approximately,how much will you need for accomodation/hotel?',end='')
hotel=int(input())
print('Last,how much do you need for food?',end='')
food=int(input())
print('Travel Expenses')
print('Location:',destination)
print('Initial Budget:',budget)
print('Fuel',gas)
print('Accomodation',hotel)
print('Food:',food)
remain=budget-gas-hotel-food
print('Remaining Budget:',remain)