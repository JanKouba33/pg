def vrat_treti(seznam):
    if len(seznam) > 2:
        return seznam[2]
    else:
        return None

def udelej_prumer(cisla):
    return sum(cisla) / len(cisla)


def naformatuj_text(student):
    jm = student["jmeno"]
    zn = student["znamky"]
    prumer = udelej_prumer(zn)
    print(f"jmeno: {jm}, prumer znamek: {prumer}")


if __name__ == "__main__":
    polozky = [1,2,10,15]
    vysledek = vrat_treti(polozky)
    print(vysledek)

    seznam_cisel = [1,2,3,4,5]
    prumer = udelej_prumer(seznam_cisel)
    print(prumer)

    data = {
        "jmeno": "Bob",
        "znamky": [1,2,1,1,2,3]
    }