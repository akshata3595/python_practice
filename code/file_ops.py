import glob
import os

def createList(r1, r2):
    return list(range(r1, r2+1))

# Driver Code
r1, r2 = 1, 5
print(createList(r1, r2))

content = "This is the first line of code\nThis is my second line of code with %s the first item in my list\nAnd this is my last line of code"

for item in createList(r1, r2):
    with open("%d_hello_world.txt" % (item), "w", 4096) as f:
         f.write(content % item)
   
list_of_files = glob.glob('./*.txt')           # create the list of file
for file_name in list_of_files:
  FI = open(file_name, 'r')
  print(FI.read())
  print(FI.read(123))
  FO = open(file_name.replace('txt', 'out'), 'w') 
  for line in FI:
    FO.write(line)
  
  FI.close()
  FO.close()
    
pid = os.getpid() 
print("This process has the PID", pid)

#stream = os.popen("strace -o output.txt -p %d -s 50" % (pid))
#print(stream.readline())
