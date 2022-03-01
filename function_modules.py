"""thehehheh hehehehh eheheheh"""
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