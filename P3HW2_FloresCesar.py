#Cesar Flores
#04/21/24
#P3HW2
#Pay chart
print("Enter employee's name:", end="") 
name = input()
hours_work = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print("Employee name:", name)
RegHour_Pay = hours_work * pay_rate
if hours_work > 40:
  overtime = hours_work - 40
else:
  overtime = 0
overtime_pay = overtime * (pay_rate * 1.5)
Gross_pay = overtime_pay + RegHour_Pay
print ("Hours Worked", hours_work)
print ("Pay Rate", pay_rate)
if overtime > 0:
 print (f"OverTime",overtime)
else:
  ()
if overtime_pay < 0:
  print ("OverTime Pay", overtime_pay)
else:
  ()
print ("RegHour Pay", RegHour_Pay)
print ("Gross Pay", Gross_pay)