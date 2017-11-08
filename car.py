class Car(object):
    def __init__(self, name ='General', model ='GM', car_type = 'saloon'):
        self.car_type = car_type
        self.model = model
        self.name = name
        self.num_of_doors = 4
        self.num_of_wheels = 4
        self.speed = 0

        if self.car_type == 'trailer':
            self.num_of_wheels = 8

        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2

        #checks if the car is a saloon car or trailer
    def is_saloon(self):
        if self.car_type == 'saloon':
            return True
        return False

    def car_wheels(self):
        pass
            #returns the speed of the car depending on the type
    def drive(self, num):
        if self.car_type == 'saloon':
            self.speed = 10 ** num
        else:
            self.speed = 77
        return self

    def details(self):
        return "{} {} {}".format(self.car_type, self.name, self.model)
