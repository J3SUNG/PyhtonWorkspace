class People:
    def __init__(self, name, age, weight, run_speed):
        self.name = name
        self.age = age
        self.weight = weight
        self.run_speed = run_speed
        print("{0}이 입장하였습니다.".format(self.name))
        print("나이는 {0}, 몸무게는 {1} 입니다.".format(self.age, self.weight))
    
    def move(self):
        print("{0}이 {1}속도로 달리고있습니다.".format(self.name, self.run_speed))

class Car:
    def __init__(self, speed):
        self.speed = speed

    def drive(self):
        print("{0}이 {1}속도로 주행중입니다.".format(self.name, self.speed))

class detailPeople(People, Car):
    def __init__(self, name, age, weight, height):
        People.__init__(self, name, age, weight, "0km/h")
        Car.__init__(self, "0km/h")
        self.height = height
        self.flight_speed = "200km/h"
    
    def fly(self):
        print("{0}이 {1}속도로 비행 하고 있습니다.".format(self.name, self.flight_speed))

    def move(self):
        self.fly()

guest_3 = detailPeople("June", 20, 70, 170)
guest_3.move()