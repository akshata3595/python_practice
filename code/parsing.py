my_dict = {}        # This is a dictionary.  I will use this to store the parsed information.

infile = open('output.log')      # open the file for reading

for line in infile:      # go through the input file, one line at a time
    line = line.strip()     # remove the newline character at the end of each line
    read, close = line.split('=')       # split up line around comma characters
    my_dict = { 'read':read, 'close':close }

print(my_dict)
print(my_dict['read'])
