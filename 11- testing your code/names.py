from name_function import get_formatted_name as gfn

print("enter 'q' at any time to quit")
while True:
    first = input("\n please enter your first name - ")
    if first == 'q':
        break
    last = input("please enter last name - ")
    if last == 'q':
        break
    
    formatted_name = gfn(first, last)
    print(f"\t Neatly formatted name: {formatted_name}")

