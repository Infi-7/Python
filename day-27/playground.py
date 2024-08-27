def add(*args):
    new_list = [arg for arg in args]
    return sum(new_list)


print(add(50, 10, 20, 20))


def calculate(**kwargs):
    print(kwargs)


calculate(add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
