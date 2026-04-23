# Tuple

B2a = (23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37)
B2b = (39, 40, 41, 42, 43, 44)

print(B2a)
print(B2b)

# Concatenation
b = B2a + B2b
print(b)

# Length of tuple
print(len(b))

# Type of tuple
print(type(b))

# Slicing operation
print(b[3:7])
print(b[7:])
print(b[:7])

# Membership operation
print(42 in b)

# Repetition
print(b * 10)

# Minimum and maximum value
print(min(b))
print(max(b))

# Converting tuple into list
l = list(b)
print(l)

# Converting list into tuple
t = tuple(l)
print(t)