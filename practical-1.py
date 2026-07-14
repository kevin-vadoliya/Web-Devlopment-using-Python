class Car:
    
    wheels = 4

    
    def __init__(self, make, model, year):
        self.make = make    
        self.model = model  
        self.year = year    
        self.speed = 0      

    
    def accelerate(self, increment):
        self.speed += increment
        return f"The {self.model} is now moving at {self.speed} km/h."

    
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"


car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Tesla", "Model 3", 2023)


print(f"Car 1: {car1.display_info()}")
print(f"Car 2: {car2.display_info()}")


print(car1.accelerate(30))
print(car2.accelerate(60))


print(f"All these cars have {Car.wheels} wheels.")
