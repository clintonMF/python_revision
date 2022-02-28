class Dog:
    '''A simple attempt to model a dog'''
    
    def __init__(self, name, age):
        '''Initialize name and age attributes.'''
        self.name = name
        self.age = age
        
    def sit(self):
        '''simulate a dog sitting in response to a command.'''
        print(f"{self.name} is now sitting")
    
    def roll_over(self):
        '''simulating a dog rolling over in response to a command'''
        print(f"{self.name} rolled over!")
        
# making an instance from a class
my_dog = Dog('bruno',6)

print(f"My dog's name is {my_dog.name}")
print(f"my dog is {my_dog.age} years old")

# calling methods
my_dog.roll_over()
my_dog.sit()

# exercise 9-1   this has been moved to exercise 9-4
# class Restaurant:
#     '''A model of a restaurant'''
#     def __init__(self, restaurant_name, cuisine_type):
#         """initializing the name of restaurant and cuisine type"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
        
#     def describe_restaurant(self):
#         '''showing details of restaurant'''
#         print(f"\nresturant name - {self.restaurant_name}")
#         print(f"type of cuisine sold - {self.cuisine_type}")
#     def open_restaurant(self):
#         '''simulating an opened restaurant'''
#         print(f'the restaurant is opened')
        
# restaurant = Restaurant('nkwobi shop', 'cow head')
# print(f"\n {restaurant.restaurant_name}")
# print(restaurant.cuisine_type)

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# exercise 9-2  (if you want to run the code for this exercise unhash this  esercise as well as
# 9-1 and hash exercise 9-4)
# restaurant1=Restaurant('Korean_shop','korean cuisine')
# restaurant2=Restaurant('chinese_palace','chinese cuisine')
# restaurant3=Restaurant('namaste_shop','indian cuisine')

# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()

# exercise 9-3
class User:
    '''A model of user information'''
    def __init__(self, first_name, last_name, year_of_birth, gender):
        '''user information'''
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender
    def describe_user(self):
        '''summary of user information'''
        print(f"\n name - {self.first_name} {self.last_name}")
        print(f"born in the year {self.year_of_birth}")
    def greet_user(self):
        '''personalized greeting'''
        if self.gender == 'male':
            print(f"good morning Mr {self.first_name}{self.last_name}")
        else:
            print(f"good morning Mrs {self.first_name} {self.last_name}")

clintonMF = User('clinton','mekwunye',2002,'male')
daniellamek = User('daniella','mekwunye',2008,'female')

clintonMF.describe_user()
clintonMF.greet_user()
daniellamek.describe_user()  
daniellamek.greet_user() 

class Car:
    '''A simple attempt to represent a car.'''
    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car'''
        self.make = make 
        self.model = model
        self.year = year
        self.odometer_reading = 0 #this is how to set a default value for an attribute
    def get_descriptive_name(self):
        '''Return a neatly descriptive name.'''
        long_name = f'\n {self.year} {self.make} {self.model}'
        return long_name
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"this car has {self.odometer_reading} miles on it")
        
    def update_odometer(self, mileage): # modifying an attribute's value through a method
        """
        set the odometer reading to the given value.
        reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back the odometer")
    def increment_odometer(self, miles):
        """adding the given amount to the odometer reading"""
        self.odometer_reading += miles
        
my_new_car = Car('toyota','camry','2020')
print(my_new_car.get_descriptive_name()) 

my_new_car.read_odometer()

# modifying an attributes value directly

my_new_car.odometer_reading = 30
my_new_car.read_odometer()
# modifying an attribute's value through a method
my_new_car.update_odometer(40)
my_new_car.read_odometer()

my_new_car.increment_odometer(15)
my_new_car.read_odometer()

# exercise 9-4
class Restaurant:
    '''A model of a restaurant'''
    def __init__(self, restaurant_name, cuisine_type):
        """initializing the name of restaurant and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        '''showing details of restaurant'''
        print(f"\nresturant name - {self.restaurant_name}")
        print(f"type of cuisine sold - {self.cuisine_type}")
    def open_restaurant(self):
        '''simulating an opened restaurant'''
        print(f'the restaurant is opened')
    def set_number_served(self, num_served):
        '''setting the number of customers served'''
        self.number_served = num_served
    def increment_number_served(self, increment_served):
        
        self.number_served += increment_served
        
restaurant = Restaurant('nkwobi shop', 'cow head')
print(restaurant.number_served)
restaurant.number_served = 4
print(restaurant.number_served)
restaurant.set_number_served(20)
print(restaurant.number_served)
restaurant.increment_number_served(5)

# inheritance

class Battery:
    '''a simple attempt to model the battery for an electric car'''
    def __init__(self, battery_size=75):
        """Initialise the battery's attribute"""
        self.battery_size = battery_size
    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
    def describe_battery(self):
        """Printing a statement telling the battery size"""
        print(f"this car has a {self.battery_size} KWH battery.")
    def get_range(self):
        """Printing a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f"this car can go about {range} miles on a full charge")
    
class ElectricCar(Car):
    """Represent aspect of a car, specific to eletric vehicles"""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
        
        
my_tesla = ElectricCar('tesla','model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# to overide a method from the parent class - define a method in the child class
# with the same name as the method you want to overide in the parent class

# exercise 9-6
class IceCreamStand(Restaurant):
    """a simple model of an icecreamstand"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initializing"""
        super().__init__( restaurant_name, cuisine_type)
        self.flavors = ['valina','strawberry','banana']
    def display_flavor(self):
        '''Printing the flavors of icecream available.'''
        print("\n available flavors are")
        for flavor in self.flavors:
            print(f"- {flavor}")
            
ice_cream = IceCreamStand('icepalace','ice cream')
ice_cream.display_flavor()

my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


        


    


