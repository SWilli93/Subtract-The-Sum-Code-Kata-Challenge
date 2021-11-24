from os import replace

#open file and clear of all line breaks
list_of_fruit = []
with open('fruit.txt') as fruit:
    fruits = fruit.readlines()
    for fruit in fruits:
       replaced_fruit = [fruit.replace("\n", "")]
       list_of_fruit.append(replaced_fruit)

# split into new list with just the number and fruit
new_list_of_fruit = []
for fruit in list_of_fruit:
    for string in fruit:
        split_string = string.split('-')
    new_fruit = split_string
    new_list_of_fruit.append(new_fruit)
    
# change list of values into dictionary
fruit_list_dictionary = {}
keys = []
values = []
for block in new_list_of_fruit:
    keys.append(block[0])
    values.append(block[1])
fruit_list_dictionary = dict(zip(keys, values))