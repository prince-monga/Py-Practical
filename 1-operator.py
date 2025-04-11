# Python Program to Demonstrate the Use of Operators

# Input values
a = 20
b = 4

# 1. Arithmetic Operators
print("Arithmetic Operators:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)

print("\nComparison Operators:")
# 2. Comparison Operators
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\nLogical Operators:")
# 3. Logical Operators
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

print("\nBitwise Operators:")
# 4. Bitwise Operators
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)

print("\nAssignment Operators:")
# 5. Assignment Operators
c = a
print("c =", c)
c += b
print("c += b:", c)
c -= b
print("c -= b:", c)

print("\nMembership Operators:")
# 6. Membership Operators
my_list = [1, 2, 3, 10]
print("10 in my_list:", 10 in my_list)
print("5 not in my_list:", 5 not in my_list)

print("\nIdentity Operators:")
# 7. Identity Operators
p = 5
q = 5
r = [1, 2, 3]
s = [1, 2, 3]
print("p is q:", p is q)
print("r is s:", r is s)
print("r == s:", r == s)
