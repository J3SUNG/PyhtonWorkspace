from global_variable import *

name = "A"


def printName():
    # global name
    name = "z"
    print(name)


printName()

print(name)

func(name)
