#Flores Cesar
#04/28/2024
#P4 HW1
#Grading system
min = 100
score = 0 
sum = 0
num_scores = int(input("How many scores do you want to enter?"))
total_nums = num_scores
while num_scores > 0:
 score = int(input(f"Enter scores #{num_scores}:"))
 sum = sum + score
 if score < 0 or score > 100:
   print ("Invalid Score entered!!!")
   print ("Score should be between 0 and 100")
   score = int(input(f"Enter score #{num_scores} again:"))
 num_scores = num_scores - 1
 if min > score:
   min = score
avg = sum / total_nums
while avg <= 100 and avg >= 90:
      grade = 'A'
if avg <= 89 and avg >=80:
      grade = 'B'
elif avg <= 79 and avg >=70:
      grade = 'C'
elif avg <= 69 and avg >=60:
      grade = 'D'
elif avg <= 59 and avg >= 0:
      grade = 'F'
print("Results")
print(f"Lowest Score:{min}")
print(f"Modifified List:{range(score)}")
print(f"Scores Average:{avg}")
print(f"Grade:{grade}")