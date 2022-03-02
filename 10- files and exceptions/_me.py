# import json
# filename = 'username.json'

# username = input('what is your name? ')

# with open(filename, 'w') as f:
#     json.dump(username, f)
#     print(f"we'll remember you when you come back, {username}!")


filename = 'pi_digits.txt'
lst = []
with open(filename) as f:
    contents = f.readlines()
    print(contents)
print(lst)
    
    