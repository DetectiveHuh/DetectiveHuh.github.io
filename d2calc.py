# Simple Calculator
# Branching,Booleans

print("+: Addition\n: Subtraction\n*: Multiplication\n/: Division\n%: Modulus\n**: Exponent\n//: Floor Division")
operation = input("Enter an operator: ")
a = int(input())
b = int(input())

if operation == "+":
    print("Addition: ")
    result = a + b
    print(str(a) + "+" + str(b) + "=" +str(result))
elif operation == "-":
    print("Subtraction:")
    result= a-b
    print(str(a) + " - " + str(b) + "=" + str(result))
elif operation == "*":
    print("Multiplication:")
    result = a * b
    print(str(a) + "*" + str(b) + "=" + str(result))
elif operation == "/":
    print("Division:")
    result= a / b
    print(str(a) + "/" + str(b) + " = " + str(result))
elif operation == "%":
    print("Modulo Operation:")
    result = a % b
    print(str(a)+ " % " + str(b)+ " = " +str(result))
elif operation == "**":
    print("Exponents:")
    result = a ** b
    print(str(a) + " ** " + str(b) + " = " + str(result))
elif operation == "//":
    print("Floor Division:")
    result = a // b
    print(str(a) + " // " + str(b) + " = " + str(result))
else:
    print("Operator not recognized")
