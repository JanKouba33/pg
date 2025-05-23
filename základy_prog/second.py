def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    ostatni = ["jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
  
    if cislo < 0 or cislo > 100:
        return "Číslo není v množině 0 až 100"
    if cislo == 100:
        return "sto"
    
    
    if 0 <= cislo <= 9:
        return jednotky[cislo]
    
    if 11 <= cislo <= 19:
        return ostatni[cislo-11]
    
    desitka = cislo // 10
    jednotka = cislo % 10
    
    
    if jednotka == 0:
        return desitky[desitka]
    
    return f"{desitky[desitka]} {jednotky[jednotka]}"




if __name__ == "__main__":
    cislo = input("Zadej číslo:")
    text = cislo_text(int(cislo))
    print(f"Zadané číslo je:{text}")