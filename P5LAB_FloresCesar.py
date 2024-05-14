#Flores Cesar
#05/05/2024
#P5LAB
#Using user-defined functions

import random

def disperse_change(change):
    change = round(change * 100)
    print(f"Change owed as integer: ${change}")
    num_dollars = change // 100
    change = change - (num_dollars *  100)

    num_quarters = change // 25
    change = change - (num_quarters*25)

    num_dimes = change // 10
    change= change-(num_dimes*10)

    num_nickles = change // 5
    change = change -(num_nickles*5)

    num_pennies = change

    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} Dollars")
        else:
            print(f"{num_dollars} Dollars")

    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} Quarters")
        else:
            print(f"{num_quarters} Quarters")

    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes}Dimes")
        else:
            print(f"{num_dimes} Dimes")

    if num_nickles > 0:
        if num_nickles == 1:
            print(f"{num_nickles} Nickles")
        else:
            print(f"{num_nickles} Nickles")

    if num_pennies > 0:
        if num_pennies ==  1:
            print(f"{num_pennies} Pennies")
        else:
            print(f"{num_pennies} Pennies")
def main ():


    amount_owned = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owned:.2f}")

    money_in = float(input("How much cash will you put in the self-checkout?"))

    change = money_in - amount_owned
    print(f"Change owned: ${change: .2f}")
    disperse_change(change)

main()