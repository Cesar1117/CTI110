#Cesar Flores
#04/28/24
#P4HW2
#Pay chart
tot_overtime_pay=0
tot_reg_pay=0
tot_gross_pay=0
tot_employees=0
overtime_hours=0
while True:
  name = input("Enter employee's name or 'Done' to terminate: ")
  if name.lower() == 'done':
     break
  hours_worked = float(input(f"How many hours did {name} work? "))
  pay_rate = float(input(f"What is {name}'s pay rate? "))
  if hours_worked <= 40:
    regular_pay = hours_worked * pay_rate
    overtime_pay = 0
  else:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
  gross_pay = regular_pay + overtime_pay
  tot_employees += 1
  tot_reg_pay += regular_pay
  tot_overtime_pay += overtime_pay
  tot_gross_pay += gross_pay
  print(f"Employee name: {name}")
  print(f"Hours Worked: {hours_worked:.1f}") 
  print(f"Pay Rate: {pay_rate:.2f}")
  print(f"OverTime: {overtime_hours:.1f}")
  print(f"OverTime Pay: ${overtime_pay:.2f}")
  print(f"RegHour Pay: ${regular_pay:.2f}")
  print(f"Gross Pay: ${gross_pay:.2f}")
print(f"Total number of employees entered: {tot_employees}")
print(f"Total amount paid for overtime: ${tot_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${tot_reg_pay:.2f}")
print(f"Total amount paid in gross: ${tot_gross_pay:.2f}")