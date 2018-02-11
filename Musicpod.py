import collections
 
#   Args: 
#       song_list (list): List of the songs in the db
#   Returns: 
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
    total_item = 0
    total_song = 0
    for users in user_dict:
        total_item += 1
        new_dict[users] = len(user_dict[users])
        total_song += len(user_dict[users])    
    return (max(new_dict, key=new_dict.get), total_song/total_item)
    

with open ("E:\\Coding_practice\\Python\\streaming.txt" , 'r') as f:
    content = f.readlines()
f.close()

data_pairs = {} # { 'user' : [songs], ...} 
song_list = [] # list of songs in the db

for lines in content:
    lines = lines.split("\n")[0].split(" ") # ['user', 'song']
    user = lines[0] # each line is a list, and first item is a username
    song = lines[1]# second item is a song number
    song_list.append(song) # list of all the songs in db  
  
    if user not in data_pairs: 
        data_pairs[user] = [song]
    else:
        data_pairs[user].append(song)
        
act_user , ave_song = active_user(data_pairs) # most active user and average song number
print('Most popular song is {}.\n'
      'Most active user is {}.\n'
      'Users listen {} songs on average.'
      .format(popular_song(song_list), act_user, int(ave_song))
      )
       

