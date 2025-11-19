class Car:

    all_cars = []
    def __init__(self, id, make, model, year, mileage):
        self._id = id
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = None
        self.add_car()
    
    def add_car(self):
        Car.all_cars.append(self)

    def __str__(self):
        return f"This is a Chevy: {self._id}"

# car_input= CarManager()
# car_input.add_car(1234, "Chevy", "Camaro", 2020, 13000)

car1 = Car(1234, "Chevy", "Camaro", 2020, 13000)
print(car1.all_cars)
