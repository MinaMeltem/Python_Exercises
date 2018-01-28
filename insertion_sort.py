# Insertion Sort with python

def insertion_sort(given_list):
    
    for index in range (1, len(given_list)): # starting index 1 to length of the list
        number = given_list[index] # value on the right
        i = index - 1  # value on the left
        while i >= 0:            
            if number < given_list[i]: # if the right value is smaller than the left value
                given_list[i + 1] = given_list[i] #assign right value to the left
                given_list[i] = number # assign left value to the right 
                i = i - 1
            else:
                break   
            
my_list = [0, 33, 13, 55, 2, 65, 1, 42]
insertion_sort(my_list)

print(my_list) # [0, 1, 2, 13, 33, 42, 55, 65]
