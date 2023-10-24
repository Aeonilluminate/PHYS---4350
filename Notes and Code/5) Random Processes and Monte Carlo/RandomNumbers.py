import random as rd

print("Let's generate a sequence of 5 random numbers.  First, we'll do it twice in a row without setting a seed.")

print("First time")
for i in range(5):
    print(rd.random())

print("Second time")
for i in range(5):
    print(rd.random())
print()

print("Now let's do it again setting the seeds.")
print("Setting seed to 42:")
rd.seed(42)
for i in range(5):
    print(rd.random())

print("Setting seed to 19473:")
rd.seed(19473)
for i in range(5):
    print(rd.random())

print("Setting seed to 42 again:")
rd.seed(42)
for i in range(5):
    print(rd.random())

