test_file = open("test.txt", "w", encoding="utf8")
print("Hello,", file=test_file)
print("Python!", file=test_file)
test_file.close()