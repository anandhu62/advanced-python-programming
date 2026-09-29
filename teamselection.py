import sys
import random
import itertools
import math
from collections import defaultdict
from functools import reduce
from datetime import date

# Student data
students = [
    ("Anita", "CSE", 85),
    ("Rahul", "CSE", 78),
    ("Priya", "CSE", 92),
    ("Kiran", "CSE", 88),

    ("Arun", "AI", 90),
    ("Meera", "AI", 82),
    ("Vishnu", "AI", 76),

    ("Neha", "Data Science", 91),
    ("Ravi", "Data Science", 84),
    ("Akhil", "Data Science", 79),

    ("Anu", "Cyber Security", 87),
    ("Sree", "Cyber Security", 81)
]

#Input team size from command line
if len(sys.argv) < 2:
    print("Please provide team size.")
    print("Example: python allocation.py 3")
    sys.exit()

team_size = int(sys.argv[1])



#Group students by department
departments = defaultdict(list)

for name, department, marks in students:
    departments[department].append((name, marks))



#Random selection of a department
department = random.choice(list(departments.keys()))
student_list = departments[department]



#possible teams
if len(student_list) < team_size:
    print("Not enough students in the selected department.")
    sys.exit()

possible_teams = list(
    itertools.combinations(student_list, team_size)
)



#Randomly selecting a team
selected_team = random.sample(possible_teams, 1)[0]



#total marks 
marks = [student[1] for student in selected_team]
total_marks = reduce(lambda x, y: x + y, marks)


#average
average_marks = total_marks / team_size




print("===== PROJECT TEAM ALLOCATION =====")
print("Team Size:", team_size)
print("Allocation Date:", date.today())
print("Department:", department)

print("\nSelected Team:")

for i, student in enumerate(selected_team, 1):
    print(i, ".", student[0], "-", student[1])

print("Total Marks:", total_marks)
print("Average Marks:", f"{average_marks:.2f}")