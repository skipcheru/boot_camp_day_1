"""Car model to describe all oop techniques
"""

class Car(object):
    """
    Object constructor
    if arguments are not passed return default values otherwise override
    """

    def __init__(self, name='General', model='GM', car_type='saloon', speed=0):
        self.model = model
        self.name = name
        self.speed = speed
        self.car_type = car_type

    @property
    def num_of_doors(self):
        """method checks if car is saloon or truck"""
        if self.name == 'Koenigsegg' or self.name == 'Porshe':
            return 2
        else:
            return 4

    @property  # return value not object instance
    def num_of_wheels(self):
        """method returns number of wheels of the car"""
        if self.car_type == 'trailer':
            return 8
        else:
            return 4

    def is_saloon(self):
        """method checks if car is saloon or truck"""
        if self.car_type == 'saloon':
            return True
        else:
            return False

    """method check speed of the car"""

    def drive(self, speed):

        if self.car_type == 'trailer':
            self.speed = speed * 11
        else:
            self.speed = 10 ** speed
            #self.speed = round((1000/3) * speed)
        return self











