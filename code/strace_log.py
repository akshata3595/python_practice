my_dict = {}        # This is a dictionary.  I will use this to store the parsed information.

with open("my_log.log", "r") as fs:
     split_data = fs.readlines()
     for line in split_data:
         word = line.split()
         print(word)
         my_dict = { word[0] : word[1] }
         print(my_dict)
