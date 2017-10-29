class Car(object):
    def __init__(self, car_type, name=None, model=None):
        self.car_type = car_type
        self.model = "Gm" if model is None else model
        self.name = 'General' if name is None else name
        self.num_of_doors = 4
        self.num_of_wheels = 4
        self.speed = 0
    def car_wheels(self):
        if self.car_type == 'trailer':
            self.num_of_wheels = 8
        else:
            return self.num_of_wheels

        if self.model is None:
            self.model = 'GM'

        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            num_of_doors = 2
    def drive(self, num):
        if self.car_type == 'saloon':
            self.speed = 10 ** num
        else:
            self.speed = 77
        return self

    def details(self):
        return "{} {} {}".format(self.car_type, self.name, self.model)
