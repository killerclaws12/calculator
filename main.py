num1 = float(input("Enter Number 1 >> "))
num2 = float(input("Enter Number 2 >> "))
app = input("Enter Opperation {+, -, * or /} >>")

if app == "+":
    total = str(num1 + num2)
elif app == "-":
    total = str(num1 - num2)
elif app == "*":
    total = str(num1 * num2)
elif app == "/":
    total = str(num1 / num2)
else:
    total = str("Unknown Opperation Or Number")

print(total)