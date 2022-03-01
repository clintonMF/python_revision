# writing to a file
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('i love programming. \n')
    file_object.write('i love creating new games. \n')
# appending to a file
with open(filename, 'a') as file_object:
    file_object.write('I always love finding meaning in large datasets.\n')
    file_object.write('I love creating new apps that can run in a browser. \n')
    
    
# # exercise 10-3
# filename1 = 'guest.txt'

# username = input('please enter your name - ')

# with open(filename1, 'w') as file_object1:
#     file_object1.write(username)
    
# # exercise 10-4
# filename2 = 'guest_book.txt'
# print("enter 'quit' when you are finished")

# while True:
#     username1 = input('please enter your name - ')
#     if username1 == 'quit':
#         break
#     else:
#         with open(filename2, 'a') as file_object2:
#             file_object2.write(f"Hello {username1} its nice to have you here. \n")


# exercise 10-5
filename3 = 'programming_poll.txt'
print("enter 'quit' when you are done")
while True:
    reason = input('state your reason here - ')
    if reason == 'quit':
        break
    else:
        with open(filename3, 'a') as file_object3:
            file_object3.write(f"i like programming because {reason}\n")
            
