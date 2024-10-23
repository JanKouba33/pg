def vrat_treti(seznam):
    if len(seznam) > 2:
        return seznam[2]
    else:
        return None


if __name__ == "__main__":
    polozky = [1,2,3]
    vysledek = vrat_treti(polozky)
    print(vysledek)