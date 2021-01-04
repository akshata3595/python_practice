my_dict = {}        # This is a dictionary.  I will use this to store the parsed information.

with open("my_log.log", "r") as fs:
     split_data = fs.readlines()
     for line in split_data:
         word = line.split()
         if len(word) == 5:
            my_dict = { word[4] : word[3] }
         else:
             my_dict = { word[5] : word[3] }
         print(my_dict)
