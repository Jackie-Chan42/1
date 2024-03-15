class Pet:
    def __init__(self, name="pet",age=0,type="cat"):
        self.name = name
        self.age=age
        self.type=type
class Human:
    def __init__(self, name="Human"):
        self.name = name
        self.listpet=[]

    def add_pets(self, *args):
        for pet in args:
            self.listpet.append(pet)

    def print_info(self):
        if
class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = [] #список
    def add_passenger(self, human):
        self.passengers.append(human)
    # def add_passenger(self, *args):
    #     for passenger in args:
    #         self.passengers.append(passenger)
    def print_passengers_names(self):
        if self.passengers!= []:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengersin {self.brand}")
nick = Human("Nick") #екземпляр класу (об'єкт)
kate = Human("Kate") #екземпляр класу (об'єкт)

car = Auto("Mercedes") #екземпляр класу (об'єкт)
car.add_passenger(nick)  #зв'язок класів
car.add_passenger(kate)
car.print_passengers_names()

pet=Pet(name:"L",age:12,type:"cat")
