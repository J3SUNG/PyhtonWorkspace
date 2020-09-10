print("{0: >8}".format(1234))

print("{0: >+8}".format(1234))
print("{0: >+8}".format(-1234))

print("{0:_<8}".format(1234))

print("{0:,}".format(1234567890))

print("{0:+,}".format(1234567890))
print("{0:+,}".format(-1234567890))

print("{0:_<+20,}".format(1234567890))

print("{0:f}".format(10/3))

print("{0:.3f}".format(10/3))

print("{0:_<+20,.3f}".format(1234567890.1234))