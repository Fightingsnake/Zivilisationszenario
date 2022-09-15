import random
from person import Frau
from person import Mann
from funktionen import Funktionen
from settings import Settings


class Gesellschaft:
    def __init__(self):
        self.funktionen = Funktionen()
        self.settings = Settings()
        self.lebendePersonen = []
        self.totePersonen = []
        self.freieJobs = {'Bauer': 2, 'Mueller': 1, 'Fleischer': 1, 'Maurer': 1, 'Schmied': 1, 'Bergarbeiter': 4}
        self.vergebeneJobs = {}
        self.mann = 0           # Anzahl Maenner in der Gesellschaft
        self.frau = 0           # Anzahl Frauen in der Gesellschaft
        self.ehemann = None     # Gerade auf dem 'Markt'
        self.ehefrau = None     # Wie Tinder mit nur einem weiteren Menschen

    def partnersuche(self, p):  # p = Person, die untersucht wird
        if self.ehemann is None and p.geschlecht == 'M':
            self.ehemann = p
        elif self.ehefrau is None and p.geschlecht == 'W':
            self.ehefrau = p
        elif self.ehefrau is not None and self.ehemann is not None:
            self.ehefrau.partner = self.ehemann.vorname
            self.ehemann.partner = self.ehefrau.vorname
            self.ehemann.vergeben = True
            self.ehefrau.vergeben = True
            self.ehemann = None
            self.ehefrau = None

    def wird_beerdigt(self, p):
        self.totePersonen.append(p)
        for i in self.lebendePersonen:
            if i.nachname == p.nachname:
                self.lebendePersonen.remove(i)
        p.gestorbenYY = p.alterYY
        p.gestorbenMM = p.alterMM
        p.gestorbenDD = p.alterDD

    def job_zuweisen(self, p):
        print("Da fehlt noch was.")
        # TODO: Job auswaehlen / Job der Person zuweisen / Job verschieben +/-

    def print_lebende(self):
        print("\n---------- [ LEBT ] ----------\n")
        for m in self.lebendePersonen:
            print(f"({m.vorname.capitalize()} {m.nachname.capitalize()}):\n"
                  f"Alter: {m.alterYY} Jahre ( {m.alterDD} Tage / {m.alterMM} Monate)")
        print(f"Gesamt Anzahl: {len(self.lebendePersonen)}"
              "\n========== [ ENDE ] ==========\n")

    def print_toten(self):
        print("\n---------- [ TOTE ] ----------\n")
        for n in self.totePersonen:
            if n.geschlecht == "M":
                t = 'männlich'
            else:
                t = 'weiblich'
            print(f"{n.nachname.capitalize()} ( {n.vorname.capitalize()}, {t}):")
            print(f"Gestorben mit {n.gestorbenYY} Jahren ( {n.gestorbenDD} Tagen / {n.gestorbenMM} Monaten)")

        print(f"Gesamt Anzahl: {len(self.totePersonen)}"
              "\n========== [ ENDE ] ==========\n")

    def zuziehen(self):
        intlen = int(len(self.lebendePersonen)/4)
        menge = random.randint(1, intlen)
        if random.random() < self.settings.zuzugchance:
            i = 0
            while i < menge:
                if random.randint(1, 10) >= 6:
                    m = Mann(self.funktionen.vornamegenerieren(), self.funktionen.nachnamegenerieren())
                    m.alterYY = random.randint(18, 70)
                    m.geburtstag = random.randint(1, 30)
                    m.geburtsmonat = random.randint(1, 12)
                    self.lebendePersonen.append(m)
                    i += 1
                else:
                    f = Frau(self.funktionen.vornamegenerieren(), self.funktionen.nachnamegenerieren())
                    f.alterYY = random.randint(18, 70)
                    f.geburtstag = random.randint(1, 30)
                    f.geburtsmonat = random.randint(1, 12)
                    self.lebendePersonen.append(f)
                    i += 1

    def ereignisse(self, kalenderiat):
        monat = kalenderiat[1]
        tag = kalenderiat[2]
        jahr = kalenderiat[0]
        for p in self.lebendePersonen:
            self.geburtstage(kalenderiat, p)
        if monat == 12:
            if tag == 24:
                print("Weihnachten")
            if tag == 30:
                print("Silvester")

    def geburtstage(self, kalender, p):
        i = 0
        aktuellerMM = kalender[1]
        aktuellerDD = kalender[2]
        if aktuellerMM == p.geburtsmonat:
            if aktuellerDD == p.geburtstag:
                e = random.randint(1, 10)
                if e == 3 or e == 5 or e == 7 or e == 10:
                    print(f'{p.nachname} hatte einen ruhigen Geburtstag.')
                elif e == 1 or e == 2 or e == 6 or e == 9:
                    wv = random.randint(1, 4)
                    while i < wv:
                        self.zuziehen()
                        i += 1
                else:
                    wv = random.randint(1, 2)
                    print(f'{p.nachname} hat eine wilde Party gehabt. {wv} Person/en sind gestorben.')
                    while i < wv:
                        self.wird_beerdigt(random.choice(self.lebendePersonen))
                        i += 1
                    p.ruhm -= 4


    def statistiken(self):
        print("Was möchtest du erfahren?\n"
              "( 1 ) Personenstatistik\n"
              "( 2 )")
        wa = input("Wähle: ")
        if wa == '1':
            stufe0 = 0  # 0 - 3 Jahre
            stufe1 = 0  # 4 - 9 Jahre
            stufe2 = 0  # 10-18 Jahre
            stufe3 = 0  # 19-34 Jahre
            stufe4 = 0  # 35-54 Jahre
            stufe5 = 0  # 55-79 Jahre
            stufe6 = 0  # 80+
            tot = 0
            kranke = 0
            for lebt in self.lebendePersonen:
                if lebt.geschlecht == 'M':
                    self.mann += 1
                elif lebt.geschlecht == 'W':
                    self.frau += 1
                if lebt.alterYY < 3:
                    stufe0 += 1
                elif 4 < lebt.alterYY < 9:
                    stufe1 += 1
                elif 10 < lebt.alterYY < 18:
                    stufe2 += 1
                elif 19 < lebt.alterYY < 34:
                    stufe3 += 1
                elif 35 < lebt.alterYY < 54:
                    stufe4 += 1
                elif 55 < lebt.alterYY < 79:
                    stufe5 += 1
                elif lebt.alterYY < 80:
                    stufe6 += 1
                for x in lebt.krankheiten:
                    kranke += 1
            for top in self.totePersonen:
                tot += 1

            print(f"{stufe0} Personen sind 0 - 3 Jahre alt.\n"
                  f"{stufe1} Personen sind 4 - 9 Jahre alt.\n"
                  f"{stufe2} Personen sind 10-18 Jahre alt.\n"
                  f"{stufe3} Personen sind 19-34 Jahre alt.\n"
                  f"{stufe4} Personen sind 35-54 Jahre alt.\n"
                  f"{stufe5} Personen sind 55-79 Jahre alt.\n"
                  f"{stufe6} Personen sind über 80 Jahre alt.\n"
                  f"Es leben momentan {self.mann} Männer und {self.frau} Frauen.\n"
                  f"{kranke} Personen haben Krankheiten.\n"
                  f"{tot} Personen sind hier gestorben.")
            print("==========================================================================\n")

