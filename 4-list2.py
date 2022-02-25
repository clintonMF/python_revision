# making use of for loops to write on the type of rice i like 
list_of_rice=['jollof','white','fried']
for rice in list_of_rice:
    print(f'i love {rice} so much')
print('i really love rice, it is my favourite food')

wild_cats=['lion','leopard','tiger']
for animal in wild_cats:
    print(f'{animal}\'s are great hunters')
print('all of these animals are very dangerous')

numbers=list(range(2, 10, 2))
print(numbers)
# code to get the square of numbers from 1 to 10
lst=list(range(1,11))
sq=[]
for num in lst:
    sq.append(num**2)
print(sq)
#using simple statistics on list
print(min(sq))
print(max(sq))
print(sum(sq))  
# using list comprehension to generate the square of numbers from 1-10
squares=[value**2 for value in range(1,11)]
print(squares)
# exercise 
print(list(range(1,21)))
lst2=list(range(1,1000000))
print(min(lst2))
print(max(lst2))
print(sum(lst2))
# slicing a list
print(squares[:5]) #when you omit the number before the ':' python starts from the first number
print(squares[5:]) #the earlier rule stated above applies here just in reverse
# exercise 4.10
print(f'the first 3 items are- {squares[:3]}')
print(f'3 items from the middle are- {squares[5:8]}')
print(f'the last 3 items are- {squares[7:]}')
# exercise 4.11
list_of_rice2=list_of_rice[:]
list_of_rice.append('ofada')
list_of_rice2.append('tuwo shinkafa')
print(list_of_rice)
print(list_of_rice2)

#TUPLES- an immutable list is called a tuple (a list whose values cannot be  modified).
# most of the operations that can be carried out on a list can be carried out on a tuple
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
# if we want to modify the values of a tuple the only way to do this is by changing the entire tuple assigned to the variable
print('the old dimensions are')
for dimension in dimensions:
    print(dimension)
    
dimensions=(400,100)
print('the new dimensions are')
for dimension in dimensions:
    print(dimension)