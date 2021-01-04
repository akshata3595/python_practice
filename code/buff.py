import os

#Method to create List for creating multiple files.
def createList(r1, r2):
    return list(range(r1, r2+1))

# Driver Code
r1, r2 = 1, 5
print(createList(r1, r2))

#Create multiple Files by writing some content to it.
for item in createList(r1, r2):
    with open("%d_file.txt" % (item), "w") as fw:
         for r in range(100):
             fw.write("\nHi Akshata!\nWelcome to python")
             fw.write("\nThis is sample file.")

    #Append mode.
    with open("%d_file.txt" % (item), "a") as fa:
         fa.write("\nThis will add last line") 
    
    #read mode.
    with open("%d_file.txt" % (item), "r") as fr:
         print(fr.read())

#Get file size
print(os.stat("%d_file.txt" % (item)).st_size)
