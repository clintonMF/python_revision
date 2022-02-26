def greeting(username):
    '''displaying a simple greeting'''  #this is  called a doc string
    print(f"Hello! {username.title()}")

greeting('clinton')

# arguments and parameters - in the code above username is the parameter and 'clinton' is the argument
# exercise 8-1
def display_message():
    print('hey everyone, i am learning how to create functions in python')

display_message()

# exercise 8-2
def favorite_book(title):
    """"displaying my favorite book"""
    print(f"one of my favorite book is {title.title()}")

favorite_book('sublte act of not giving a fuck')

# positional arguments - this arguments follow the same structure as their parameters, their values match up 

def describe_pet(animal_type, pet_name):
    """"displaying information on my pet"""
    print(f" \n I have a {animal_type.title()}")
    print(f" My {animal_type.title()}'s name is {pet_name.title()}")
    
describe_pet('dog','bruno')
describe_pet('nine tail', 'kurama')
# in the example above we can see positional argument at play. the position of dog in the argument is the same as the position of animal 
# type in the parameter. mixing up the order whiie using positional arguments can lead to unexpected results.

# keyword arguments - they are key-value pairs passed into a function call. while using keyword argument the position of the argument is
# irrelevant and the code will produce the same output irrespective of the order in which the arguments are passed and example is shown 
# below

def describe_pet(animal_type, pet_name):
    """"displaying information on my pet"""
    print(f" \n I have a {animal_type.title()}")
    print(f" My {animal_type.title()}'s name is {pet_name.title()}")
    
describe_pet(animal_type='dog',pet_name='bruno')
describe_pet(pet_name='bruno', animal_type='dog')

# default values
def describe_pet(pet_name,animal_type='dog'):
    """"displaying information on my pet"""
    print(f" \n I have a {animal_type.title()}")
    print(f" My {animal_type.title()}'s name is {pet_name.title()}")
    
describe_pet(pet_name='bruno' )

# equivalent function calls - most times there are several ways to call a function. All the calls below would produce the same output
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# exercise 8-3
def make_shirt(size, text_on_shirt):
    '''describing the size of a shirt and the text on the shirt'''
    print(f"\n i have a {size} size shirt with the text {text_on_shirt} written on it")
make_shirt('meduim', 'i am KIRA, i am justice')
make_shirt(size='meduim', text_on_shirt='i am KIRA, i am justice')

# exercise 8-4
def make_shirt(size='large', text_on_shirt='i love python'):
    '''describing the size of a shirt and the text on the shirt'''
    print(f"\n i have a {size} size shirt with the text {text_on_shirt} written on it")
make_shirt()
make_shirt('small', 'i am KIRA, i am justice')

# exercise 8-5
def describe_city(city, country="nigeria"):
    '''telling the locations of cities'''
    print(f"{city.title()} is located in {country.title()}")
    
describe_city('lagos')
describe_city('ibadan')
describe_city('accra', 'ghana')

# making an argument optional and using the return statement
# to make an argument optional we set the default value to an empty string

def get_formatted_name(first_name,last_name, middle_name=""):
    '''return a full name, neatly formatted'''
    if middle_name:
        full_name=f"{first_name} {middle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"
    return full_name.title()
names1=get_formatted_name('clinton','daniel')
print(names1)
names2=get_formatted_name('clinton','daniel','kerry')
print(names2)
# using a while loop
# while True:
#     print('\n please tell me your name')
#     print('enter \'quit\' at any time to quit')
#     f_name = input('first name - ')
#     if f_name == 'quit':
#         break 
#     l_name = input('last name - ')
#     if l_name == 'quit':
#         break
    
#     name3 = get_formatted_name(f_name,l_name)
#     print(name3)
    
# exercise 8-6
def city_country(city, country):
    '''showing the cities and their countries'''
    citycountry=f'"{city.title()}, {country.title()}"'
    return citycountry
lagos=city_country('lagos','nigeria')
warri = city_country('warri','nigeria')
print(lagos)
print(warri)

# exercise 8-7
def make_album(artist_name, album_title,no_of_songs=None):
    '''showing details of an album'''
    if no_of_songs:
        album_details={'artist name': artist_name, 'album title':album_title, 'number of songs':no_of_songs}
    else:
        album_details={'artist name': artist_name, 'album title':album_title}
    return album_details

donda=make_album('kanye','donda',12)
donda2 = make_album('kanye','donda2')
print(donda)
print(donda2)

# exercise 8-8
while True:
    print('\n please enter album details')
    print("enter 'done' when you are done")
    
    artist = input('artist name - ')
    if artist == 'done':
        break
    name6 = input('name of the album - ')
    if name6 == 'done':
        break
    
    details = make_album(artist, name6)
    print(details)
    



    
