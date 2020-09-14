try:
    a = {}
    print(a[2])
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except NameError:
    print("문자열처리 오류 발생.")
except:
    print("예상치 못한 오류가 발생했습니다.")