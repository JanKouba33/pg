def operace(typ, a, b):
    matematicka_operace = None
    if typ == "+":
        matematicka_operace = a + b
    elif typ == "-":
        matematicka_operace = a - b
    elif typ == "*":
        matematicka_operace = a * b
    elif typ == "/":
        matematicka_operace = a / b
    else:
        return ("Není možné vypsat")
    return matematicka_operace

if __name__ == "__main__":
    print(operace("+", 1, 2))  # 3
    print(operace("-", 2, 1))  # 1
    print(operace("*", 0, 5))  # 0
    print(operace("/", 4, 2))
    print(operace("A", 4, 2))  # 2