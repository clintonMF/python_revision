# # using ZeroDivisionError exception
# try:
#     number = 5/0
#     print(number)
# except:
#     ZeroDivisionError
#     print('you cannot divide a number by 0')
    
# print('tell me 2 numbers and i will divide the first by the second')
# print("enter 'q' when you are done")

# while True:
#     f_number = input('first number - ')
#     if f_number == 'q':
#         break
    
#     s_number = input('second number - ')
#     if s_number == 'q':
#         break

#     try:
#         div_num = int(f_number)/int(s_number)
#         print(div_num)
#     except:
#         ZeroDivisionError
#         print('you cannot divide a by 0')
        
# # handling the FileNotFoundError Exception
# filename = 'programming.txt'

# try:
#     with open(filename) as f:
#         contents = f.read()
# except:
#     FileNotFoundError
#     print(f'sorry,the file {filename} does not exist')
# else:
#     # count the approximate number of words in the file.
#     words = contents.split()
#     num_words = len(words)
#     print(f"the file {filename} contains about {num_words} words.")
    
# # these line of codes can be modified to work for several files by simply making it a function
# def count_words(filename):
#     try:
#         with open(filename) as f:
#             contents = f.read()
#     except:
#         FileNotFoundError
#         print(f'sorry,the file {filename} does not exist')
#     else:
#         # count the approximate number of words in the file.
#         words = contents.split()
#         num_words = len(words)
#         print(f"the file {filename} contains about {num_words} words.")
        
# filenames = ['programming.txt', 'alice.txt', 'guest.txt', 'guest_book.txt']
        
# for filename in filenames:
#     count_words(filename)
    
# # failing silently - you don't have to report every error. to make a progarm fail silently use the "pass" statement

# # exercise 10-6 and 10-7
# print('tell me 2 numbers and i will tell you their sum')
# print("enter 'quit' when you are done.")
# while True:
#     first_number = input('first number - ')
#     if first_number == 'quit':
#         break
    
#     second_number = input('second number - ')
#     if second_number == 'quit':
#         break
#     try:
#         sum = int(first_number) + int(second_number)
#     except:
#         ValueError
#         print('please enter numbers, letters or sentences cannot be added')
#     else:
#         print(sum)

# # exercise 10-8 and 10-9
# def animal_names(filename):
#     try:
#         with open(filename) as f:
#             lines = f.readlines()
#     except:
#         FileNotFoundError
#         pass 
#     else:
#         for line in lines:
#             print(line, end='')
# lst = ['cats.txt','pigs.txt','dogs.txt']  #this is to show that the code silent error works as there is no 'pigs.txt'
# for ele in lst:
#     animal_names(ele)


# exercise 10-11 and 10-12
import json
filename = 'fav_num.json'

def get_stored_favnum():
    '''get the favorite number stored'''
    try:
        with open(filename) as f:
            favnum = json.load(f)
    except:
        FileNotFoundError
        return None
    else:
        return favnum
        
        
def get_favnum():
    '''print a message telling the favorite number'''
    favnum = get_stored_favnum()
    try:
        if favnum:
            print(f'your favourite number is - {favnum}') 
    except:
        FileNotFoundError
        favnum = input('pleease input your favourite number- ')
        with open(filename, 'w') as f:
            json.dump(favnum, f)   
            
get_favnum()
            



