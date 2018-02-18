import collections
import numpy as np

with open ("E:\\Coding_practice\\Python\\cbpss.txt" , 'r') as f:
    content = f.readlines()
f.close()

vote_list = []
for lines in content:
    vote = int(lines.split("\n")[0])   
    if vote in range(1,5): # Ratings from 1 to 4
        vote_list.append(vote)        
         
#frequency of elements in the list, e.g [(4,10), (3,8)...] 
frequency = collections.Counter(vote_list)
 

print('Highest Rating: {}.\n'
      'Lowest Rating: {}.\n'
      'Average Rating: {}.\n'      
      .format(max(vote_list), min(vote_list), int(sum(vote_list)/len(vote_list)))) 

#Numpy array to find standard deviation
_np_vl = np.array(vote_list) 

#(4 most common items in the tuple)[.th item pair][.th item in the pair]
#e.g [(4,10), (3,8) , (2,3), (1,2)]
print('# of {} Ratings {} '.format(frequency.most_common(4)[3][0],frequency.most_common(4)[3][1]))
print('# of {} Ratings {} '.format(frequency.most_common(4)[2][0],frequency.most_common(4)[2][1]))
print('# of {} Ratings {} '.format(frequency.most_common(4)[1][0],frequency.most_common(4)[1][1]))
print('# of {} Ratings {} '.format(frequency.most_common(4)[0][0],frequency.most_common(4)[0][1]))
print('Standatd Deviation: {}.\n'.format(np.std(_np_vl)))

'''
Output :
    Highest Rating: 4.
    Lowest Rating: 1.
    Average Rating: 3.

    # of 1 Ratings 2 
    # of 2 Ratings 3 
    # of 3 Ratings 8 
    # of 4 Ratings 10 
    Standatd Deviation: 0.946588741612054.
'''