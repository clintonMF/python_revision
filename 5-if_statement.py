# exercise 5.1
Nigerias_population=230_000_000
print('is nigerias population== 230000000? i predict true')
print(Nigerias_population)
# exercise 5.2
lst=['daniel','daniella','kerry']

if lst[1]!='clinton':
    print('username created')
if lst[0].lower()=='daniel':
    print('this name already exist')

username='favour'
if username!=lst[0] and username!=lst[-1]:
    print('username created')
if username == lst[0] or username == lst[1]:
    print('username already exist')
else:
    print('username created ')
if username in lst:
    print('username already exist')
else:
    print('username created')
if username not in lst:
    print('username created')

# exercise 5-3
alien_color='green'
if alien_color=='green':
    print('you just earned 5 points')
    
alien_color='yellow'
if alien_color=='green':
    print('you just earned 5 points')
# exercise 5-4
alien_color='yellow'  #this version works for the 'else block'
if alien_color=='green':
    print('you just earned 5 points')
else:
    print('you just earned 10 points')

alien_color='green' #this version works for the 'if block'
if alien_color=='green':
    print('you just earned 5 points')
else:
    print('you just earned 10 points')

# exercise 5-6
age=50
if age<2:
    print('a baby')
if age>=2 and age<4:
    print('a toddler')
if age>=4 and age<13:
    print('a kid')
if age>=13 and age<20:
    print('a teenager')
if age>=20 and age<65:
    print('an adult')
if age>=65:
    print('an elder')
    
# exercise 5-8
usernames=['admin','goku','gohan','deku']
for user in usernames:
    if len(usernames)==0:
        print('we need to find some users!')
    if user=='admin':
        print(f'Hello "admin", would you like to see a status report?')
    else:
        print(f'Hello {user}, thank you for logging in again')
            
# exercise 5-9
usernames=[]
if len(usernames)==0:
        print('we need to find some users!')
else:
    for user in usernames:
        if len(usernames)==0:
            print('we need to find some users!')
        if user=='admin':
            print(f'Hello "admin", would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in again') 
# exercise 5-10   - a program that simulates usernames
current_users=['goku','vegita','krilin','bulma','master roshi']
new_users=['naruto','hinata','bulma','nagato','krilin']
for users in new_users:
    if users in current_users:
        print(f'this "{users}" username is already taken')
        print('please choose a new username')
    else:
        print(f'this "{users}" username is available ')
# execise 5-11 - ordinal numbers
nums=list(range(1,10))
for num in nums:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')