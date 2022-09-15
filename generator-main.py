from person import Mann
from person import Frau
from settings import Settings
from random import randint
from gesellschaft import Gesellschaft
from ausgaben import Ausgabe
from funktionen import Funktionen


class Generator:
    def __init__(self):
        self.settings = Settings()
        self.gesellschaft = Gesellschaft()
        self.ausgabe = Ausgabe()
        self.funktionen = Funktionen()
        self.kalender = [1, 1, 1]

    @property
    def kalender(self):
        return self.__kalender

    @kalender.setter
    def kalender(self, kalender):
        self.__kalender = kalender


    def initialisieren(self):
        m = 0
        f = 0
        while m < self.settings.startmann:
            self.gesellschaft.lebendePersonen.append(Mann(self.funktionen.vornamegenerieren(), self.funktionen.nachnamegenerieren()))
            m += 1
        while f < self.settings.startfrau:
            self.gesellschaft.lebendePersonen.append(Frau(self.funktionen.vornamegenerieren(), self.funktionen.nachnamegenerieren()))
            f += 1

    def run_generator(self):
        self.initialisieren()
        i = 0
        while True:
            if i % self.settings.zwischenstaende == 0:
                print(self.kalender)
                self.zwischenstaende()


            for p in self.gesellschaft.lebendePersonen:
                if p.aktiv:
                    # ===== [ geburt ] =====
                    if p.geschlecht == 'W' and p.schwanger is True:
                        if p.alterYY == p.geburtsterminYY:
                            if p.alterMM == p.geburtsterminMM:
                                if randint(1, 10) >= 6:
                                    c = 'M'
                                else:
                                    c = 'W'
                                p.geburt(self.gesellschaft.lebendePersonen, self.funktionen.vornamegenerieren(), c)


                    # ===== [ alltag Mensch ] =====
                    p.altern(self.settings.schritte)
                    #p.sterben2()
                    if p.partnersuche():
                        self.gesellschaft.partnersuche(p)
                    if p.sterben():
                        self.gesellschaft.wird_beerdigt(p)
                    p.krank_check(self.kalender)
                    p.raucher_check(self.settings.schritte)
                    if p.geschlecht == 'W':
                        p.schwangerschaft()

            # ===== [ alltag Gesellschaft ] =====
            """Hier dinge wie:
            gesellschaft.zuziehen (leute generieren)
            gesellschaft.ereignis usw..."""
            self.gesellschaft.zuziehen()
            self.gesellschaft.ereignisse(self.kalender)

            # ===== [ alltag Krankheiten ] =====
            # Hier soll rein:
            # Wenn es monat 10 - 3 ist, soll der faktor der grippe hoeher sein
            if 1 <= self.kalender[1] <= 3:
                self.settings.grippeFaktor *= 3
            elif self.kalender[1] == 4:
                self.settings.grippeFaktor *= 2
            elif 5 <= self.kalender[1] <= 8:
                self.settings.grippeFaktor *= 1
            elif self.kalender[1] == 9:
                self.settings.grippeFaktor *= 2
            elif 10 <= self.kalender[1] <= 12:
                self.settings.grippeFaktor *= 3



            self.kalenderup(1)

            i += 1
            if i > self.settings.durchlaufzyklen:
                break

    def zwischenstaende(self):
        while True:
            a = self.ausgabe.abfrage()
            if a == 1:
                self.gesellschaft.print_lebende()
            elif a == 2:
                self.gesellschaft.print_toten()
            elif a == 3:
                self.gesellschaft.statistiken()
            else:
                break

    def kalenderup(self, schritte):
        self.kalender[2] += schritte
        if self.kalender[2] >= 31:
            self.kalender[2] -= 30
            if self.kalender[2] <= 30:
                self.kalender[1] += 1
                if self.kalender[1] >= 13:
                    self.kalender[1] -= 12
                    self.kalender[0] += 1

gen = Generator()
gen.run_generator()
