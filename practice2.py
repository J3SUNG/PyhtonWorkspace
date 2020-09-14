class People:
    def __init__(self):
        print("People 생성자")

class Car:
    def __init__(self):
        print("Car 생성자")

class detailPeople(People, Car):
    def __init__(self):
        super().__init__()

test = detailPeople()