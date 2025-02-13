def sabiranje(a, b):
    return a + b

def oduzimanje(a, b):
    return a - b

def mnozenje(a, b):
    return a * b

def deljenje(a, b):
    if b == 0:
        return "greska: delis nulom!"
    return a / b

# TODO: dodati jos operacija za nas kalkulator

if __name__ == "__main__":
    print("dobrodosli u zli kalkulator")
    while True:
        print("\nIzaberite operaciju:")
        print("1. Sabiranje")
        print("2. Oduzimanje")
        print("3. Množenje")
        print("4. Deljenje")
        print("5. Izlaz")
        
        izbor = input("Unesite broj operacije (1-5): ")
        
        if izbor == '5':
            break
            
        broj1 = float(input("Prvi broj: "))
        broj2 = float(input("Drugi broj: "))
        
        if izbor == '1':
            print(f"Rezultat: {sabiranje(broj1, broj2)}")
        elif izbor == '2':
            print(f"Rezultat: {oduzimanje(broj1, broj2)}")
        elif izbor == '3':
            print(f"Rezultat: {mnozenje(broj1, broj2)}")
            print("yes king")
        elif izbor == '4':
            print(f"Rezultat: {deljenje(broj1, broj2)}")
        else:
            print("Pogrešan izbor!")
