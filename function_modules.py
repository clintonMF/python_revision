def my_details(**details):
    '''Gives a brief description of myself'''
    print('\n these are my details')
    for key,value in details.items():
        print(f"{key} - {value}")