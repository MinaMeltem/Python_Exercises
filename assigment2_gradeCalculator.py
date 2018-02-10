# -*- coding: utf-8 -*-
"""
@author: MEL

Question : Write a program to promt user to enter the grades of the student. 
User should enter -1 to terminate the program. 
Output should be Total and the avarge of the grades.
(Use for loop , not while loop) 

"""
# Loop through the list to get last item, if it isn't -1, 
# promt user to enter new grade, and add it in to the list,
# Terminate the loop if it's - 1

grades = [0]
total = 0

for g in grades:    
    if grades[len(grades)-1] == -1:
        break
    else:
        grade = input("Enter the grade: ")
        total = total + int(grade)
        grades.append(int(grade))
        
total = total + 1    # removing -1 from the list since it's not a grade
length =  len(grades) - 2

print ("Sum of the grades : " , total)
print ("Average of the grades : " , total / length )

