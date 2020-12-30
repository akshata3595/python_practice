# Print out the items in the dictionary by looping through.
python_words = {'list': 'A collection of values that are not connected, but have an order.',
                'dictionary': 'A collection of key-value pairs.',
                'function': 'A named set of instructions that defines a set of actions in Python.',
                }

for key, value in python_words.items():
    print("\nKey: %s" % key)
    print("Value: %s" % value)

#Get keys and values in order.
for key in sorted(python_words.keys()):
    print("%s: %s" % (key.title(), python_words[key]))

#Looping through all keys in a dictionary
my_dict = {'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    }
update_dict= {'key_4': 'value_5'}

for key in my_dict.keys():
    print('Key: %s' % key)

#To get value of specific key
for key in my_dict:
    if key == 'key_2':
        print("The value for key_2 is %s." % my_dict[key])

#Looping through all values in a dictionary.
for value in my_dict.values():
    print('Value: %s' % value)

#Update a dictionary
my_dict.update({"key_4" : "value_4"})
print(my_dict)

my_dict.update(update_dict)
print("Dictionary after updation:")
print(my_dict)

#Store dictionary value as a list.
favorite_numbers = {'eric': [3, 11, 19, 23, 42],
                    'ever': [2, 4, 5],
                    'willie': [5, 35, 120],
                    }

# Display each person's favorite numbers.
for name in favorite_numbers:
    print("\n%s's favorite numbers are:" % name.title())
    print(favorite_numbers[name])      
