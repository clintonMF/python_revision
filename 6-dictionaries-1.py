# a dictionary in python is a collection of key-value pairs
alien_0={'color':'green','point':4}
print(alien_0['point'])
print(alien_0['color'])
# adding new key-value pairs to a dictionary
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
# modifying the values in a dictionary
alien_0['color']='yellow'
print(alien_0)
# a short game simulation to show the position of an alien
alien_1={'x_position':0,'y_position':2,'speed':'fast'}
print(f"aliens original position-{alien_1['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_1['speed']=='slow':
    x_increment=1
elif alien_1['speed']=='medium':
    x_increment=2
elif alien_1['speed']=='fast':
    x_increment=3
alien_1['x_position']+=x_increment
print(f"aliens new position-{alien_1['x_position']}")

# removing key-value pair; this is done with del statement
del alien_0['color']
print(alien_0)
# using the get() function to retrieve values in a dictionary
# the advantage of get() function is that if the value doesn't exist it doesn't show an error
# print(alien_0['color'])  - using this square bracket would bring up an error code as the value doesn't exist
print(alien_0.get('color',"this value doesn't exist"))
# exercise 6-1
daniel_bio={
    'f_name':'daniel',
    'l_name':'mekwunye',
    'age':14,
    'city':'lagos'
}
print(daniel_bio['age'])
# exercise 6-3

glossary={
    'dictionary':'it is a collection of key-value pairs',
    'tuple':'an immutable list',
    'variable':'a container used to store value'
    }
print(f"dictionary: {glossary['dictionary']}")
print(f"tuple \n {glossary['tuple']}")
print(f"variable \n {glossary['variable']}")

# looping through a dictionary
# in the codes below i write a program that sends a message to all my friends, and some extra message which varies per person depending on their favorite language
fav_lang={
    'daniel':'python',
    'kerry':'c++',
    'clinton':'java',
}
friends=['amina','kerry','clinton','jean']

for name in friends:
    print(f"Hi! {name.title()}")
    
    
    if name in fav_lang:
        print(f"\t i heard your favourite language is {fav_lang[name]}")
        
    if name not in fav_lang:
        print(f'\t {name} you never told me what your favourite language is ')
        
# looping through a dict in a particular order
for name in sorted(fav_lang):
    print(name)
    
# exercise 6-5
rivers={
    'nile':'egypt',
    'niger':'nigeria',
    'jordan':'isreal'
}
for river, country in rivers.items():
    print(f"the river {river} runs through {country.title()}.")
    print(river.title())
    print(country.title())
    


    