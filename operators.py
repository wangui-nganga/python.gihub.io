a=30
b=10
# arithmetic operator
print("Addition of two operators",a+b)
print("Subtraction of two operators",a-b)
print("Multiplication of two operators",a*b)
print("Division of two operators",a/b)
print("Remainder of two operators",a%b)
print("Modulus of two operators",a%b)
print("Exponentiation of two operators",a**b)
print("Floor of two operators",a//b)

# comparison operator

c=50
d=12

print(f"{c} and {d} are equal {c==d}")
print(f"{c} and {d} are not equal {c!=d}")
print(f"{c} is greater {d} : {c>=d}")
print(f"{c} is less {d} : {c<=d}")

# logical operator

e=10
print(f"Is this statement true :{e>5} and {e<10}")
print(f"Is this statement false:{e>5} or {e<10}")
print(f"Each statement is true then return false and vice-versa:",(not(e>5 or e<10)))

# assignment operators
f = 10
print(f)
f += 26
print(f)