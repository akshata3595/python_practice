#Access Elements

dict = {'Student Name': 'Pooja', 'Roll No.': 12, 'Subject': 'English'}
print("dict['Student Name']: ", dict['Student Name'])
print("dict['Roll No.']: ", dict['Roll No.'])
print("dict['Subject']: ", dict['Subject'])

#Append in a Dictionary
dict_append = {"1" : "Python", "2" : "Java"}
print(dict_append)
dict_append["3"] = "CPP"
print(dict_append)

#Update Method to Append Elements
dict_append.update({"4" : "JavaScript"})
print(dict_append)

'''
Remove Elements from Dictionary.
'''

# Create a Python dictionary
sixMonths = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30}

# Delete a specific element
print(sixMonths.pop(6)) 
print(sixMonths)

# Delete an random element
print(sixMonths.popitem())
print(sixMonths)

# Remove a specific element
del sixMonths[4]
print(sixMonths)

# Delete all elements from the dictionary
sixMonths.clear()
print(sixMonths)

# Finally, eliminate the dictionary object
del sixMonths
#print(sixMonths)

#Iterate Dictionary
dict = {'Student Name': 'Pooja', 'Roll No.': 12, 'Subject': 'English'}
print("Keys are:")
for key in dict:
 print(key)

print (dict.items())
