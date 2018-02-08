# -*- coding: utf-8 -*-
"""
@author: MEL
"""
 # Monthly premium cost for a var
def insurance_premium():
    age = int(input("Please Enter your age: "))    
    # starting cost = $50    
    starting_cost = 50;

    # Monthly premium due to age 
    if age > 18:  
        if age <= 25:
            age_cost = 100
        
        elif age > 25 and age <= 35:
            age_cost = 20
            
        else:
            age_cost = 0;
            
    # Accident cost             
        accident = int(input("Please enter the number of the accident within 5 years: " ))
        
        if accident == 2:
            accident_cost = accident * 40
    
        elif accident >= 3 and accident <= 4:
            accident_cost = accident * 60
        
        elif accident > 4:
            print("We can't provode insurance")
    
        else:
            accident_cost = 0;
    
        print("Your total Insurance cost is : $",starting_cost + age_cost + accident_cost)
    
    else:
        print ("You are too young to drive")
        
    
       

insurance_premium()  





     