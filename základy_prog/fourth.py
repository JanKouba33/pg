def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    typ = figurka["typ"]
    pozice = figurka["pozice"]
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    radek, sloupec = pozice
    cil_radek, cil_sloupec = cilova_pozice


    # kontrola jestli je pozice na šachovnici
    if (1 > cil_radek > 8 and 1 > cil_sloupec < 8):
        return False

    if typ == "pěšec":
        # Pěšec - o 1 dopředu
        if cil_radek == radek + 1 and cil_sloupec == sloupec and cilova_pozice not in obsazene_pozice:
            return True
        # Pěšec - o 2 dopředu
        if radek == 2 and cil_radek == 4 and cil_sloupec == sloupec:
            prvni_skok = (radek + 1, sloupec)
            if prvni_skok not in obsazene_pozice and cilova_pozice not in obsazene_pozice:
                return True
        return False
    
    if typ == "jezdec":
        moznosti_tahu = [
        (radek + 2, sloupec + 1), (radek + 2, sloupec - 1),
        (radek - 2, sloupec + 1), (radek - 2, sloupec - 1),
        (radek + 1, sloupec + 2), (radek + 1, sloupec - 2),
        (radek - 1, sloupec + 2), (radek - 1, sloupec - 2)
        ]
        if cilova_pozice in moznosti_tahu and cilova_pozice not in obsazene_pozice:
                return True
        return False
    
    if typ == "věž":
        # Kontrola pohybu věže
        if radek != cil_radek and sloupec != cil_sloupec:
            return False
        # Řádkový pohyb
        if radek == cil_radek:
            start, end = sorted([sloupec, cil_sloupec])
            for sl in range(start + 1, end):
                if (radek, sl) in obsazene_pozice:
                    return False
        # Sloupcový pohyb
        elif sloupec == cil_sloupec:
            start, end = sorted([radek, cil_radek])
            for r in range(start + 1, end):
                if (r, sloupec) in obsazene_pozice:
                    return False
            
        if cilova_pozice in obsazene_pozice:
            return False

        return True

    if typ == "střelec":
        if abs(cil_radek - radek) != abs(cil_sloupec - sloupec):
            return False
        
        radkovy_krok = 1 if cil_radek > radek else -1
        sloupcovy_krok = 1 if cil_sloupec > sloupec else -1

        aktualni_radek, aktualni_sloupec = radek + radkovy_krok, sloupec + sloupcovy_krok

        while (aktualni_radek, aktualni_sloupec) != (cil_radek, cil_sloupec):
            if (aktualni_radek, aktualni_sloupec) in obsazene_pozice:
                return False
            aktualni_radek += radkovy_krok
            aktualni_sloupec += sloupcovy_krok
        return True
    
    if typ == "dáma":
        if cil_radek != radek and cil_sloupec != sloupec and abs(cil_radek - radek) != abs(cil_sloupec - sloupec):
            return False
        
        # Horizontální pohyb
        if cil_radek == radek:
            start, end = sorted([sloupec, cil_sloupec])
            for s in range(start + 1, end):
                if (radek, s) in obsazene_pozice:
                    return False
        # Vertikální pohyb
        elif cil_sloupec == sloupec:
            start, end = sorted([radek, cil_radek])
            for r in range(start + 1, end):
                if (r, sloupec) in obsazene_pozice:
                    return False
        # Diagonální pohyb
        else:
            radkovy_krok = 1 if cil_radek > radek else -1
            sloupcovy_krok = 1 if cil_sloupec > sloupec else -1
            aktualni_radek, aktualni_sloupec = radek + radkovy_krok, sloupec + sloupcovy_krok
            while (aktualni_radek, aktualni_sloupec) != (cil_radek, cil_sloupec):
                if (aktualni_radek, aktualni_sloupec) in obsazene_pozice:
                    return False
                aktualni_radek += radkovy_krok
                aktualni_sloupec += sloupcovy_krok
        return True
    
    if typ == "král":
        if abs(cil_radek - radek) <= 1 and abs(cil_sloupec - sloupec) <= 1:
            if cilova_pozice not in obsazene_pozice:
                return True
        return False



    


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True  