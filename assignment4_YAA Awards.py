# -*- coding: utf-8 -*-
"""
@author: MEL

"""

months = int(input("Number of month your prize will be paid: "))

payment = 1

for month in range(1, months + 1):    
    if month == 1:
        print ('{} {}: ${}'.format("Month", "1", "1") )       
    
    elif month % 2 == 1:
        payment = payment * 3
        print ('{} {}: ${}'.format("Month", month, payment) )    
        
    else:
        payment = payment * 2
        print ('{} {}: ${}'.format("Month", month, payment) )
    
    
