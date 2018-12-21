a = int(input("Enter Number = "))

b = int(input("Enter Number = "))

op = str(input("Enter Operation Symbol = "))

if (op == "+" or "addition"):
    add = a + b
    print(add)
    
if (op == "-" or "subtraction"):
    sub = a - b
    print(sub)

if (op == "*" or "multiplication"):
    mult = a * b
    print(mult)
    
if (op == "/" or "division"):
    div = a / b
    print(div)
    
else: 
    print("!404 ERROR!")
