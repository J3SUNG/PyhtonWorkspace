class People:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        print("{0}이 입장하였습니다.".format(self.name))
        print("나이는 {0}, 몸무게는 {1} 입니다.".format(self.age, self.weight))

    def eat(self, food):
        print("{0}이 {1}을 먹습니다.".format(self.name, food))
        self.increase()

    def increase(self):
        print("몸무게가 {0}에서 {1}로 증가되었습니다.".format(self.weight, self.weight + 1))
        self.weight += 1

class detailPeople(People):
    def __init__(self, name, age, weight, height):
        People.__init__(self, name, age, weight)
        self.height = height

guest_1 = People("OWEN", 23, 80)
guest_2 = People("JOLLY", 19, 52)

print("이름 : {0}, 나이 : {1}, 몸무게 : {2}".format(guest_1.name, guest_1.age, guest_1.weight))

guest_1.adult = True
if guest_1.adult == True:
    print("{0}은 성인입니다.".format(guest_1.name))

guest_1.eat("치킨")
print(guest_1.weight)

guest_3 = detailPeople("June", 20, 70, 170)
print("이름 : {0}, 나이 : {1}, 몸무게 : {2}, 키 : {3}".format(guest_3.name, guest_3.age, guest_3.weight, guest_3.height))