class People:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        print("{0}이 입장하였습니다.".format(self.name))
        print("나이는 {0}, 몸무게는 {1} 입니다.".format(self.age, self.weight))

class Car:
    def __init__(self, speed):
        self.speed = speed

    def drive(self, name):
        print("{0}이 {1}속도로 주행중입니다.".format(name, self.speed))

class detailPeople(People, Car):
    def __init__(self, name, age, weight, height, speed):
        People.__init__(self, name, age, weight)
        Car.__init__(self, speed)
        self.height = height

guest_3 = detailPeople("June", 20, 70, 170, "100km/h")
print("이름 : {0}, 나이 : {1}, 몸무게 : {2})".format(guest_3.name, guest_3.age, guest_3.weight))
print("키 : {0}, 속도 : {1}".format(guest_3.height, guest_3.speed))
guest_3.drive(guest_3.name)