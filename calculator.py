x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = input("Do you want to * / + - : ")

if z == "*":
    print(x * y)
elif z == "/":
    print(x / y)
elif z == "+":
    print(x + y)
elif z == "-":
    print(x - y)
else:
    print("This didn't work")
