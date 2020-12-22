# answer = input("What is the air-speed velocity of an unladen swallow? ")
# print(answer)

counts = 2
print("I have ", counts, " counts.")

n = 5
if n < 5:
    print("n is less than five")
elif n == 5:
    print("n is equal to five")
else:
    print("n is bigger than five")

def add(num1, num2):
    result = num1 + num2
    return result

cal1 = add(10, 40)
print(cal1)

def say_hello():
    print("hello")

say_hello()