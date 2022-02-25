# i had to split this up for ease of studying. it is still the same chapter 6
# in this part of chapter 6 we are looking at Nesting
# Nesting is basically involves storing of dictionaries in a list , list in dictionaries or dictionaries in dictionaries

# a list of dictionaries
# to make a fleet of aliens
aliens=[]
for new_alien in range(1,11):
    new_alien={'speed':'slow','color':'green'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='fast'
for  alien in aliens:
    print(alien)
    
# a list in a dictionary
# taking the order for the rice type and other food
order={'rice':'jollof','additions':['plantain','beans','meat','fish'],}
print(f"the order is {order['rice']} rice \n with")
for food in order['additions']:
    print(f"\t {food}")

# dictionary in dictionaries - this method can be complicated
users = {
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    },
    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    },
    }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    
# exercise 6-8
bruno={'name':'bruno','animal':'dog','owner':'daniel'}
sassy={'name':'sassy','animal':'cat','owner':'clinton'}
nine_tail={'name':'nine_tails','animal':'fox','owner':'naruto'}
pets=[bruno,sassy,nine_tail]

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['animal']} and he belongs to {pet['owner']}")

# exercise 6-9
favorite_places={
    'clinton':['my room','the library',],
    'daniel':['football stadium','cinema','training center'],
    'kerry':['o2 arena','theatre']
    }
for name, places in favorite_places.items():
    print(f"\n my name is {name} and my favorite places are:")
    for place in places:
        print(place)
# exercise 6-11
cities={
    'lagos':{'country':'nigeria','population':15_000_000,'size':1_171},
    'texxas':{'country':'usa','population':29_000_000,'size':695_662},
    'ottawa':{'country':'canada','population':994_837,'size':2_790},
}
for city,description in cities.items():
    print(f"\n {city.title()} is a city located in {description['country']}")
    print(f" if has a popualtion size of {description['population']} and covers {description['size']} of land")