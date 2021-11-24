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

# function to turn number into a list of digits
# function to sum up all individual numbers into one number
# returns original number minus sumed digits
def subtract_the_sum(num):
    x = [int(a) for a in str(num)]
    return num - sum(x)


# method to loops through fruit_list_dictionary until key is found
# assume n >= 10 and n <= 10000
def return_the_value(num):
    new_num = subtract_the_sum(num)
    should_restart = True
    while should_restart:
        for key in fruit_list_dictionary:
            if str(new_num) in fruit_list_dictionary.keys():
                should_restart = False
                return fruit_list_dictionary[str(new_num)]
            else:
                new_num = subtract_the_sum(new_num)
                print(new_num, key, fruit_list_dictionary[key])
                continue
            
        
return_the_value(7576)