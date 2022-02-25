# below is a list of people i want to invite to my party
guest_list=['daniel','kerry','ifesh','ruka']
for ele in guest_list:
    print(f'dear {ele.title()}, i am organizing a party to celebrate my winning of the nobel prize.\nI would be pleased if you could come')
# A guest won't be able to make it to the party, replace the guest
name_of_unvailable_guest='ruke'
name_of_replacement='daniella'

guest_list[-1]='daniella'
print(guest_list)
for ele in guest_list:
    print(f'dear {ele.title()}, i am organizing a party to celebrate my winning of the nobel prize.\nI would be pleased if you could come')
# more guest are available for the party and you need to add them
# i would do this through various methods
guest_list.insert(0,'clinton')
guest_list.insert(2,'amos')
guest_list.append('eben')
print(guest_list)
for ele in guest_list:
    print(f'dear {ele.title()}, i am organizing a party to celebrate my winning of the nobel prize.\nI would be pleased if you could come')

# i just figured out that i can only invite two people to the party
print('i am sorry to inform you that i would only be able to invite 2 people to the party')
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
print(guest_list)
for ele in guest_list:
    print(f'dear {ele.title()}, i am organizing a party to celebrate my winning of the nobel prize.\nI would be pleased if you could come')
del guest_list[0]
del guest_list[0]
print(guest_list)
# organizing a list
# the sort() and sorted() functions are used in organizing a list
# when the former is used you can't get the original list back 
# the original can be gotten when sorted is used
cars=['tesla','toyota','benz']
cars.sort()
print(cars)

payments=[12000,30000,5000]
sorted_list=sorted(payments)
print(f'sorted list is -{sorted_list}')
print(f"original list is -{payments}")

cars.reverse()
print(cars)
no_of_element_in_the_list=len(payments)
print(no_of_element_in_the_list)

print(f'sorted list is -{sorted_list}')
#using sort and sorted function to get the reverse order of a list
reverse_of_payments=sorted(payments, reverse=True)
cars.sort(reverse=True)
print(reverse_of_payments)
print(cars)