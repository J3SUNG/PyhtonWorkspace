try:
    print(3/0)
    print("try!")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
    print("except!")
finally:
    print("Hello\n")