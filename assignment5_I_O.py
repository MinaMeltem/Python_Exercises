"""
@author: MEL
"""
with open ("E:\\Coding_practice\\Python\\input.txt" , 'r') as f:
    content = f.readlines()
f.close()
    
tickets = {} 
total = 0
lenght = 0   

for line in content:
    ID = line.split(" ")[0]
    price = float(line.split(" ")[1])  
    
    if ID not in tickets:
        tickets[ID] = price
    else:
        tickets.update({ID:price})
        
    total += tickets[ID]
    lenght += 1
    
    
max_ID = max(tickets, key=tickets.get)
min_ID = min(tickets, key=tickets.get)
ave = total / lenght

output = ('======================================================\n'
       '\t\t TICKET REPORT \t\t' 
       '======================================================\n'
       ' There are {} tickets in the database\n\n'
       ' Maximum Ticket price is ${}\n'
       ' Minimum Ticket price is ${}\n'
       ' Avarage Ticket price is ${:.2f}\n\n'
       ' Thank you for using  ticket system!') .format(lenght, tickets[max_ID],tickets[min_ID], ave)

print(output)