# Week6_Assignment
## Partner Assignment for Week 6 CNE 310
### Pull Request Signed SoW
#### This is the debuging Project Code:

def lone_sum(a, b, c):
if a >= b:
return c
elif a == c:
return b
elif b == c:
return a
elif a == b and a == c and b == c:
return 0
else:
return a+b+c
print("lone_sum of 10, 10, 10 should be 0: " + str(lone_sum(10, 10, 10)))
print("lone_sum of 1, 2, 3 should be 6: " + str(lone_sum(1, 2, 3)))
print("lone_sum of 1, 2, 1 should be 2: " + str(lone_sum(1, 2, 1)))
print("lone_sum of 4, 5, 6 should be 15: " + str(lone_sum(4, 5, 6)))


This Python code defines a function called score_to_letter_grade that converts a numeric grade into a letter grade based on a set of conditions. 
This is a breakdown of what it does:

The function takes a numeric grade as input.
It then checks the value of grade against several thresholds using if-elif conditions to assign the appropriate letter grade:

If grade is 90 or higher, it returns "A".
If grade is between 87 and 89, it returns "B+".
If grade is between 80 and 86, it returns "B".
If grade is between 77 and 79, it returns "C+".
If grade is between 70 and 76, it returns "C".
If grade is between 67 and 69, it returns "D+".
If grade is between 60 and 66, it returns "D".
Otherwise, it returns "F" for any grade below 60.


Please create an issue report if you discover any bugs while running it with PyCharm.
