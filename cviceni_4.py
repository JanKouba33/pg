class Zvire:
    def __init__(self, jmeno) :
        self.jmeno = jmeno
        print (f"Zvire {self.jmeno} bylo vytvoreno")

class Pes(Zvire) :
    def __init__(self, jmeno, rasa) :
        self.rasa = rasa
        print(f"Pes rasy {self.rasa} byl vytvoren")

if __name__ == "__main__":
    pes = Pes("Alik", "jezevcik")
