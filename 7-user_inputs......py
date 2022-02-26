# using input
prompt='giving us your infomation would help us personalise the messages you receive'
prompt+='\n what\'s your first name? '
name=input(prompt)
print(f'hey! {name} it is nice to have you here.')
# using the modulo operator
# this operator gives the remainder: it can be used to tell if a number is 
# a multiple of another(if a number is even or odd) using if and else statements
num=input('enter a number, and i will tell you if its even or odd - ')
num=int(num)

if num % 2 == 0:
    print(f"the number is even")
else:
    print('the number is odd')
# exercise 7-1
rental_car=input('what car would you like today ma? ')
print(f"let me see if i an find you a {rental_car}")
# exercise 7-2
reservation=input('please sir how, what table would you life? a table for - ')
reservation=int(reservation)
if reservation>8:
    print('i am sorry sir,but you will have to wait for a table')
else:
    print ('a table is ready')
# exercise 7-3
num1=input('tell me a number and i will tell you if it\'s a multiple of 10 - ')
num1=int(num1)
if num1 % 10 == 0:
    print('it is a multiple of 10')
else:
    print('it is not a multiple of 10')
# while loops
# creating a system that lets the user choose when to quit
game = "\n tell me something, and i will repeat it back to you"
game += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message=input(game)
    
    if message != 'quit':
        print(message)
# a better method of doing the above using flags(a variable that holds the conditions)
game1 = "\n tell me something, and i will repeat it back to you"
game1 += "\nEnter 'quit' to end the program. "
active=True    #this is the flag variable
while active:
    message1 = input(game1)
    if message1 == 'quit':
        active=False
    else:
        print(message1)
        
# using break to exit a loop 
# a loop that starts with 'while True' will run forever
game2 = "\n tell me something, and i will repeat it back to you"
game2 += "\nEnter 'quit' to end the program. "
while True:
    message2=input(game2)
    if message2 == 'quit':
        break
    else:
        print(message2)
# exercise 7-4
print('nice to have you here')
pizza_order = '\n what toppings would you like today? when you are done enter \'quit\' '
while True:
    message3=input(pizza_order)
    if message3 == 'quit':
        break
    else:
        print(f"i'll add {message3} to your pizza")
# exercise 7-5
question='how old are you? '
age=input(question)
age=int(age)
if age < 3:
    print('you get a free ticket')
elif age >=3 and age < 12:
    print('your ticket would cost 10 dollars')
elif age >= 12:
    print('your ticket would cost 15 dollars')   # i couldn't figure out a way to use while loop for this problem and since the if statement works perfectly i didn't see the need to 
# exercise 7-6 b


print('nice to have you here today')
pizza_order1='what topping would you like? when done enter \'quit\' '
active= True
while active:
    message4=input(pizza_order1)
    if message4 == 'quit':
        active = False
    else:
        print(f"i will add {message4} to your pizza")
        
        
# using while loop on list and dictionaries
unconfirmed_users=['goku','gohan','vegita','vegito']
confirmed_users=[]

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"verifying current user: {current_user.title()}")
    confirmed_users.append(current_user)
    
print(f" the following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)
    
# making a poll
responses = {}
poll_active = True
while poll_active:
    message5=input('\n what is your name? ')
    message6= input('what mountain would you like to climb today? ')
    
    responses[message5]=message6
    
    message7= input('would you like someone else to play? input yes or no ')
    
    if message7 == 'no':
        poll_active=False
    
print("... polling results....")
for name,response in responses.items():
    print(f"{name} wants to climb mount {response}")
    
# exercise 7-8
rice_orders = [
    'jollof',
    'white',
    'ofada',
    'fried',
]
finished_rice = []
serving= True
while serving:
    for rice_order in rice_orders:
        print(f"i made {rice_order} rice")
        finished_rice.append(rice_order)
    if len(finished_rice) == len(rice_orders):
        serving = False
print('the rice made are:')
for rice in finished_rice:
    print(f"\t{rice}")    
    


    


    