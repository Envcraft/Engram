# Level 1 - Topic 2b: Type Conversion
# Converting between Python's built-in data types

# str -> int
num_str = "42"
num = int(num_str)
print(num + 1)       # 43

# float -> int (truncates decimal)
pi = 3.14
print(int(pi))       # 3

# int/float -> str
print(str(100))      # "100"
print(str(3.14))     # "3.14"

# int -> float
print(float(5))      # 5.0

# str -> float
print(float("2.71")) # 2.71

# int/float -> bool (0 is False, everything else is True)
print(bool(0))       # False
print(bool(42))      # True

# str -> bool (empty string is False)
print(bool(""))      # False
print(bool("hello")) # True
