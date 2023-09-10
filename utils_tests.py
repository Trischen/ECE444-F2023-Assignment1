import utils

"""
Reverse tests
"""

#strings
out = utils.utils.reversed("a string")
if out != "Invalid datatype":
    print("Test 1 failed")
else:
    print("Test 1 passed")

#floats
out = utils.utils.reversed(353.25)
if out != "Invalid datatype":
    print("Test 2 failed")
else:
    print("Test 2 passed")

#int
out = utils.utils.reversed(1234)
if out != 4321:
    print("Test 3 failed")
else:
    print("Test 3 passed")

"""
Formatter tests
"""
#strings
out1, out2 = utils.utils.formatter("a string")
if out1 != "Invalid datatype":
    print("Test 4 failed")
else:
    print("Test 4 passed")

#floats
out1, out2 = utils.utils.formatter(353.25)
if out1 != "Invalid datatype":
    print("Test 5 failed")
else:
    print("Test 5 passed")

#int
out1, out2 = utils.utils.formatter(1234)
if out1 != bin(1234) or out2 != oct(1234):
    print("Test 6 failed")
else:
    print("Test 6 passed")