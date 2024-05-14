#Flores Cesar
#05/06/2024
#P5HW
#adding and substarting numbers

import random
def disperce_adding():
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    number3 = number1 + number2
    print (f"{number1}+{number2}=")
    sum = float(input("Enter a number:"))
    if sum == number3:
       print("Congradulations!!! Your answer is correct.")
       return main()
    else:
       print("Sorry guess again:")
def disperce_subtracting():
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    number4 = number1 + number2
    print (f"{number1}-{number2}=")
    sum = float(input("Enter a number:"))
    if sum == number4:
       print("Congradulations!!! Your answer is correct.")
       return main()
    else:
       print("Sorry guess again:")
def main ():
 print ("Welcome to Math Quiz")
 print ("Main Menu")
 print ("1. Adding Random Number")
 print ("2. Substarcting Random Numbers")
 print ("3. Exit")
 options = float(input("Please choose one of the menu options:"))
 while True:
  if options == 1:
    disperce_adding() 
  elif options == 2:
    disperce_subtracting()
  elif options == 3:
    print("Thank you for playing...")
    print("Bye!!")
    break
 
main()