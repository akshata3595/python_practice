import os

#Method to create List for creating multiple files.
def createList(r1, r2):
    return list(range(r1, r2+1))

# Driver Code
r1, r2 = 1, 5
print(createList(r1, r2))

content = "This is the first line of code\nThis is my second line of code with %s the first item in my list\nAnd this is my last line of code"

#Create multiple Files by writing some content to it.
for item in createList(r1, r2):
    with open("%d_hello_world.txt" % (item), "w") as fw:
         fw.write(content % item)

    #Read file content.
    with open("%d_hello_world.txt" % (item), "r") as fr:
    #This will print every line one by one in the file 
         for each in fr: 
             print(each)
             #To extract a string that contains all characters in the file.
             print(fr.read())
             #It will read the first five characters of stored data
             print(fr.read(5))

    #read only one line at a time.
    with open("%d_hello_world.txt" % (item), "r") as f:
         print(f.readline())

    #To get all the lines, use a loop until
    with open("%d_hello_world.txt" % (item), "r") as f:
         line = f.readline()
         while line != "":
             print(line)
             line = f.readline()

    #Reading all the lines present inside the text file
    #Readline method is memory efficient as it reads one line at a time.
    with open("%d_hello_world.txt" % (item), "r") as f:
         print(f.readlines())

    #Append mode.
    with open("%d_hello_world.txt" % (item), "a") as fa:
         fa.write("\nThis will add this line") 

    #Read file again.
    with open("%d_hello_world.txt" % (item), "r") as fd:
         read_data = fd.read()
         print(read_data)

    #split lines using split() method
    with open("%d_hello_world.txt" % (item), "r") as fs: 
         split_data = fs.readlines() 
         for line in split_data: 
             word = line.split() 
             print(word)

    #Moving the cursor in the file
    with open("%d_hello_world.txt" % (item), "r") as f:
         print(f.tell())
         print(f.seek(4))
         print(f.tell())
         print(f.read())
         #Check file status
         print(os.stat("%d_hello_world.txt" % (item)))
