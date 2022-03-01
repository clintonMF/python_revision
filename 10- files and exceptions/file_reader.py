# working with files content
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    
print(pi_string[:10])
print(len(pi_string))

# # a program to show if your birthday is contained in pi?
# birthday = input('enter your birthday in the form of mmddyy- ')
# if birthday in pi_string:
#     print(f"your birthday appears in the first 1million digit of pi")
# else:
#     print('your birthday does not appear in the first 1 million digit of pi')
    
# exercise 10-1
# A - print the contents by reading in the entire file
filename1 = 'learning_python.txt'
with open(filename1) as file_object1:
      contents = file_object1.read()
print(contents)

# B - print the contents by looping over the file object
filename2 = 'learning_python.txt'
with open(filename2) as file_object2:
    lines = file_object2.readlines()
    
for line in lines:
    print(line)
    
# C - print the contents by storing the lines in a list and then working with them outside the with block
filename3 = 'learning_python.txt'
with open(filename3) as file_object3:
    lin = file_object3.readlines()
    
learn_pstring = ''
for li in lin:
    learn_pstring += li.rstrip()
print(learn_pstring)


# exercise 10-2
# using the replace function

filename4 = 'learning_python.txt'
with open(filename4) as file_object4:
    lines1 = file_object4.readlines()
    
replace_str=''
    
for line1 in lines1:
    replace_str += line1.replace('python','c')
print(replace_str)
replace_str
print(replace_str)

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)
