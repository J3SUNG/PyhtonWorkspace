import random

class inputWrongNumError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

randomNum = random.randint(1, 9)

while(1):
    try:
        print("1 ~ 9의 값 중 입력하여 맞추어보세요.")
        num = int(input("입력 : "))

        if num < 1 or num > 9:
            raise inputWrongNumError("Err) input : {0}".format(num))

        if num == randomNum:
            print("성공!")
            break
        else:
            print("다시 시도 해보세요")
            continue
    except inputWrongNumError as err:
        print(err)
        print("1 ~ 9 값을 입력해주세요\n")    