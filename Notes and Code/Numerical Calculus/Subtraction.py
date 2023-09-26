import math

print("x = 1, y = 1+10^(-14)*sqrt(2)")
print()
x = 1.0
y = 1.0 + (1e-14)*math.sqrt(2)

print("if we calculate 10^14*(y-x), the answer should clearly be sqrt(2)")
print("let's compare that wiht the answer Python gives us")

print("10^(14)*(y-x) = ")
print(1e14*(y-x))
print("compared to sqrt(2) = ")
print(math.sqrt(2))
print()
print("That's because the value of y is rounded to 16 digits:")
print(y)
