def faktorial_for(n):
    vysledek = 1
    for x in range(1, n + 1):
        vysledek = vysledek * x
    return vysledek

def faktorial_while(n):
    vysledek = 1
    x = 1
    while x <= n:
        vysledek *= i
        n -= 1
    return vysledek

if __name__ == "__main__":


    print(faktorial_for(10))
    print(faktorial_while(10))
    
    
        