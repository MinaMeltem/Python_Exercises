import collections
 
#   Args: 
#       song_list (list): List of the songs in the db
#  Returns: 
#       str: The most common song number

def popular_song(song_list):
    frequency = collections.Counter(song_list)
    common_song = frequency.most_common(1)[0][0]
    return (common_song)

#   Args: 
#     user_dict (dict): {'user' : [list of songs]}
#   Returns: 
#     str: The most common song , int : average number of songs streamed 
def active_user(user_dict):
    new_dict = {} 
    user_counter = 0 # number of users in the dict
    song_counter = 0 # total number of songs in the dict
    for users in user_dict:
        user_counter += 1
        # key: user, value: the total # of songs in the user's song list. e.g. {"A" : 5}.
        new_dict[users] = len(user_dict[users])  
        song_counter += len(user_dict[users])         
    return (max(new_dict, key=new_dict.get), song_counter/user_counter)




    
with open ("E:\\Coding_practice\\Python\\streaming.txt" , 'r') as f:
    content = f.readlines()
f.close()

data_pairs = {} #e.g. { 'user1': [song1, song2 ..], 'user2':[song1, song2] ...} 
song_list = [] # list of songs in the db


for lines in content:
    lines = lines.split("\n")[0].split(" ") # each line is a list, e.g. ['A', '1']
    user = lines[0] # first item is a username
    song = lines[1]# second item is a song number
    song_list.append(song) # appending songs in a separte list

  
    if user not in data_pairs: # adding { user: song} pair in to the dict
        data_pairs[user] = [song]
    else:
        data_pairs[user].append(song) # appending new value in to the song list 

# most active user and average song number        
act_user , ave_song = active_user(data_pairs) 
print('Most popular song is {}.\n'
      'Most active user is {}.\n'
      'Users listen {} songs on average.'
      .format(popular_song(song_list), act_user, int(ave_song))
      )
       

