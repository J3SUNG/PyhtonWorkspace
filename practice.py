test_file = open("test.txt", "w", encoding="utf8")
print("Hello,", file=test_file)
print("Python!", file=test_file)
test_file.close()

test_file = open("test.txt", "a", encoding="utf8")
test_file.write("Nice to ")
test_file.write("Meet You")
print("Python!", file=test_file)
test_file.close()

test_file = open("test.txt", "r", encoding="utf8")
print(test_file.read())
test_file.close()

test_file = open("test.txt", "r", encoding="utf8")
while True:
    line = test_file.readline()
    if not line:
        break
    print(line, end="")
test_file.close()
print()

test_file = open("test.txt", "r", encoding="utf8")
lines = test_file.readlines()
for line in lines:
    print(line, end="")
test_file.close()