name = "JON"


def change(name):
    name = "S" + name[1:]
    return name


name = change(name)

print(name)