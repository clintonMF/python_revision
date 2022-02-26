uncompleted_desings = ['naruto','goku','gohan']
completed_desings = []
def print_desings(uncompleted_desings, completed_desings):
    '''to show the designs being printed'''
    while uncompleted_desings:
        current_desing = uncompleted_desings.pop()
        print(f"Printing model: {current_desing}")
        completed_desings.append(current_desing)
def show_completed_desings(completed_desings):
    '''displaying the completed desings'''
    print('\nthese are the completed desings')
    for desing in completed_desings:
        print(desing)
        

print_desings(uncompleted_desings[:],completed_desings)  #this ([:]) will make sure that the uncompleted_desing list is not modified.
show_completed_desings(completed_desings)

print(uncompleted_desings)

# exercise 8-9
def show_messages(messages):
    for message in messages:
        print(message)
messages1=['Hi! how do you do','good morning, its nice to have you here', 'you are welcome']
show_messages(messages1[:])

# exercise 8-10
sent_messages = []
def send_messages(messages):
    for message in messages:
        print(message)
        sent_messages.append(message)
    print('\n these messages have been sent:')
    for message in sent_messages:
        print(message)
        
send_messages(messages1[:])
print(messages1) #exercise 8-11

# passing an arbituaary number of arguments: this is done using * before the parameter
def make_pizza(size, *toppings):
    '''summarize the pizza we are about to make'''
    print(f'\n we are about to make a {size} inch pizza with the following toppings:')
    for topping in toppings:
        print(f"- {topping}")
make_pizza(12,'cheese')
make_pizza(16,'pepperoni','cheese')

# using arbituary key word arguments: thiw is done using ** before the parameter (in this case we can pass in key value pair)
def build_profile(f_namne, l_name, **user_info):
    '''building a user profile'''
    user_info['first name'] = f_namne.title()
    user_info['last name'] = l_name.title()
    return user_info
clintonMF=build_profile('clinton','mekwunye',department='met and mat engr',year = 'year 5', age = 19)
print(clintonMF)  # exercise 8-13

# exercise 8-12
def make_sandwich(*ingredients, no_of_ingredients):
    '''summarings the sandwich we are about to make'''
    print('\n the ingredients in the sandwich are:')
    for ingredient in ingredients:
        print(ingredient)
    print(f'number of ingredients-{no_of_ingredients}')
make_sandwich('meat','fish','pepper','cheese',no_of_ingredients=4)

# exercise 8-16

import function_modules
function_modules.my_details(first_name='clinton',last_name='mekwunye',age=19,eye_color='brown')

from function_modules import my_details as md
md(age=19,eye_color='brown')

import function_modules as fm
fm.my_details(first_name='clinton',last_name='mekwunye')