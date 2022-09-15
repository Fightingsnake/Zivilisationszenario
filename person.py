import random
from funktionen import Funktionen
import krankheiten

class Person:
    def __init__(self, vorname, nachname, geschlecht=None, mutter=None, vater=None):
        self.aktiv = True
        self.vorname = vorname
        self.nachname = nachname
        self.alterDD = 0  # 0-3 baby; 4-9 kind; 10-18 teen [geburtsfaehig w13-45/m13-57];
        self.alterMM = 0  # 19-30 junger erwachsener; 31-50 erwachsen; 51- tod senior
        self.alterYY = 0
        self.geburtstag = 0
        self.geburtsmonat = 0
        self.geschlecht = geschlecht
        self.sterbewahrscheinlichkeit = 1
        self.vergeben = False
        self.partner = None
        self.mutter = mutter
        self.vater = vater
        self.impotent = False
        self.kinder = []  # ["1": "AA", "2": "AX"]
        self.ruhm = 0  # TODO: +/- verschiedene werte (rauchen zb -1, job +2 o.ae.)
        #self.moeglichekrankheiten = [krebs(), hiv()]
        self.krankheiten = []       # krebs, aids u.ä.
        self.job = None
        self.fuehrerschein = False
        self.raucher = False
        self.rauchcountr = 0
        self.raucherSeit = 0  # Jahre des rauchens : Pro Jahr 0.1% sterbechance hinzu
        self.gestorbenDD = 0
        self.gestorbenMM = 0
        self.gestorbenYY = 0

    # ============== [ GETTER / SETTER ] ==============

    @property
    def aktiv(self):
        return self.__aktiv

    @aktiv.setter
    def aktiv(self, aktiv):
        self.__aktiv = aktiv

    @property
    def geburtstag(self):
        return self.__geburtstag

    @geburtstag.setter
    def geburtstag(self, geburtstag):
        self.__geburtstag = geburtstag

    @property
    def geburtsmonat(self):
        return self.__geburtsmonat

    @geburtsmonat.setter
    def geburtsmonat(self, geburtsmonat):
        self.__geburtsmonat = geburtsmonat

    @property
    def vorname(self):
        return self.__vorname

    @vorname.setter
    def vorname(self, vorname):
        self.__vorname = vorname

    @property
    def nachname(self):
        return self.__nachname

    @nachname.setter
    def nachname(self, nachname):
        self.__nachname = nachname

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, job):
        self.__job = job

    @property
    def vergeben(self):
        return self.__vergeben

    @vergeben.setter
    def vergeben(self, vergeben):
        self.__vergeben = vergeben

    @property
    def partner(self):
        return self.__partner

    @partner.setter
    def partner(self, partner):
        self.__partner = partner

    @property
    def alterDD(self):
        return self.__alterDD

    @alterDD.setter
    def alterDD(self, alterDD):
        self.__alterDD = alterDD

    @property
    def alterMM(self):
        return self.__alterMM

    @alterMM.setter
    def alterMM(self, alterMM):
        self.__alterMM = alterMM

    @property
    def ruhm(self):
        return self.__ruhm

    @ruhm.setter
    def ruhm(self, ruhm):
        self.__ruhm = ruhm

    @property
    def fuehrerschein(self):
        return self.__fuehrerschein

    @fuehrerschein.setter
    def fuehrerschein(self, fuehrerschein):
        self.__fuehrerschein = fuehrerschein

    @property
    def alterYY(self):
        return self.__alterYY

    @alterYY.setter
    def alterYY(self, alterYY):
        self.__alterYY = alterYY

    @property
    def geschlecht(self):
        return self.__geschlecht

    @geschlecht.setter
    def geschlecht(self, geschlecht):
        self.__geschlecht = geschlecht

    @property
    def sterbewahrscheinlichkeit(self):
        return self.__sterbewahrscheinlichkeit

    @sterbewahrscheinlichkeit.setter
    def sterbewahrscheinlichkeit(self, sterbewahrscheinlichkeit):
        self.__sterbewahrscheinlichkeit = sterbewahrscheinlichkeit

    @property
    def impotent(self):
        return self.__impotent

    @impotent.setter
    def impotent(self, impotent):
        self.__impotent = impotent

    @property
    def gestorbenDD(self):
        return self.__gestorbenDD

    @gestorbenDD.setter
    def gestorbenDD(self, gestorbenDD):
        self.__gestorbenDD = gestorbenDD

    @property
    def gestorbenMM(self):
        return self.__gestorbenMM

    @gestorbenMM.setter
    def gestorbenMM(self, gestorbenMM):
        self.__gestorbenMM = gestorbenMM

    @property
    def gestorbenYY(self):
        return self.__gestorbenYY

    @gestorbenYY.setter
    def gestorbenYY(self, gestorbenYY):
        self.__gestorbenYY = gestorbenYY

    @property
    def raucher(self):
        return self.__raucher

    @raucher.setter
    def raucher(self, raucher):
        self.__raucher = raucher

    @property
    def rauchcountr(self):
        return self.__rauchcountr

    @rauchcountr.setter
    def rauchcountr(self, rauchcountr):
        self.__rauchcountr = rauchcountr

    @property
    def raucherSeit(self):
        return self.__raucherSeit

    @raucherSeit.setter
    def raucherSeit(self, raucherSeit):
        self.__raucherSeit = raucherSeit

    # ============== [ FUNKTIONEN ] ==============

    '''def person_updater(self):
        if self.geschlecht == 'W':'''

    def sterben1(self):
        '''1 + 3
        1 + 6
        1 + 2
        ...'''
        print("einfuegen")
        for v in self.krankheiten:
            if random.random()*100 < (self.sterbewahrscheinlichkeit + v.toedlichkeit):
                print(f'tot durch {v.name}')

    def sterben2(self):
        '''
        1
        3
        6
        2
        ...
        '''
        x = random.random()*100
        if x < self.sterbewahrscheinlichkeit:
            print('tot weil herz versagte...')
        else:
            for v in self.krankheiten:
                if random.random()*100 < v.toedlichkeit:
                    print(f'tot durch {v.name}')

    def sterben3(self):
        '''
        1+3+6+2...
        '''
        su = self.sterbewahrscheinlichkeit
        for v in self.krankheiten:
            su += v.toedlichkeit
        if random.random()*100 < su:
            print('tot :(')

    def impotenz(self):
        if 13 < self.alterYY < 80:
            if 13 <= self.alterYY <= 25:
                wahrscheinlichkeit = 5
                if random.randint(1, 100) <= wahrscheinlichkeit:
                    self.impotent = True
            elif 26 <= self.alterYY <= 35:
                wahrscheinlichkeit = 10
                if random.randint(1, 100) <= wahrscheinlichkeit:
                    self.impotent = True
            elif 36 <= self.alterYY <= 55:
                wahrscheinlichkeit = 25
                if random.randint(1, 100) <= wahrscheinlichkeit:
                    self.impotent = True
            elif self.alterYY >= 56:
                wahrscheinlichkeit = 50
                if random.randint(1, 100) <= wahrscheinlichkeit:
                    self.impotent = True
            else:
                self.impotent = False
        else:
            self.impotent = True

    def altern(self, schritte):
        self.alterDD += schritte
        if self.alterDD >= 31:
            self.alterDD -= 30
            if self.alterDD <= 30:
                self.alterMM += 1
                if self.alterMM >= 13:
                    self.alterMM -= 12
                    self.alterYY += 1

    def sterben(self):  # TODO: Mehr Faktoren (Krebs zb) einfuegen. > zb 0.1 * (Krebschance + weiteres)
        if self.alterYY <= 18:
            self.sterbewahrscheinlichkeit = 0.025
        elif 19 <= self.alterYY <= 34:
            self.sterbewahrscheinlichkeit = 0.1
        elif 35 <= self.alterYY <= 50:
            self.sterbewahrscheinlichkeit = 0.25
        elif 51 <= self.alterYY <= 60:
            self.sterbewahrscheinlichkeit = 0.5
        elif 61 <= self.alterYY <= 80:
            self.sterbewahrscheinlichkeit = 1
        elif 81 <= self.alterYY <= 100:
            self.sterbewahrscheinlichkeit = 2.5
        elif self.alterYY >= 101:
            self.sterbewahrscheinlichkeit = 100
        if random.random() * 100 <= self.sterbewahrscheinlichkeit:
            self.aktiv = False
            return True
        for k in self.krankheiten:
            v = random.random()*100
            if v <= k.toedlichkeit:
                print(f'gestorben an {k.name}')
                self.aktiv = False
                return True
        else:
            return False

    def partnersuche(self):
        if 14 <= self.alterYY <= 70 and not self.vergeben:
            wahrscheinlichkeit = 50
            if random.randint(1, 100) <= wahrscheinlichkeit:
                return True
        else:
            return False

    def raucher_check(self, schritte):
        if not self.raucher:
            if self.alterYY >= 15:
                if self.geschlecht == 'M':
                    zug = 27
                else:
                    zug = 20.8
                if random.random()*100 < zug:
                    self.raucher = True
        else:
            self.rauchcountr += schritte
            if self.rauchcountr >= 360:
                self.rauchcountr -= 360
                self.raucherSeit += 1
                self.sterbewahrscheinlichkeit += 0.1

    def krank_check(self, kalender):    # Kalender fuer Saisonkrankheiten (grippe oder so)
        verzeichnis = [krankheiten.Hiv(), krankheiten.Tumor(), krankheiten.Grippe()]
        for k in verzeichnis:
            k.updater(self)
            losDesTages = random.random()*100
            if losDesTages <= k.infektChance:
                vorhanden = False
                for x in self.krankheiten:
                    if x.name == k.name:
                        vorhanden = True
                if not vorhanden:
                    self.krankheiten.append(k)
                    for aasf in self.krankheiten:
                        print(aasf.name)
            if self.krankheiten:
                for k in self.krankheiten:
                    if k.name == 'Grippe':
                        k.dauer -= 1
                        if k.dauer == 0:
                            print('ueberstandene grippe')
                            self.krankheiten.remove(k)


class Mann(Person):
    def __init__(self, vorname, nachname, geschlecht="M"):
        super().__init__(vorname, nachname, geschlecht)
        self.potent = False

    @property
    def geschlecht(self):
        return self.__geschlecht

    @geschlecht.setter
    def geschlecht(self, geschlecht):
        self.__geschlecht = geschlecht

    @property
    def potent(self):
        return self.__potent

    @potent.setter
    def potent(self, potent):
        self.__potent = potent

    def vater_werden(self):  # Wahrscheinlichkeit Vater zu werden.
        if not self.impotent:
            if 13 <= self.alterYY <= 20:
                wahrscheinlichkeit = 9
            elif 21 <= self.alterYY <= 28:
                wahrscheinlichkeit = 30
            elif 29 <= self.alterYY <= 39:
                wahrscheinlichkeit = 78
            elif 40 <= self.alterYY <= 46:
                wahrscheinlichkeit = 18
            else:
                wahrscheinlichkeit = 0
            chose = random.randint(1, 100)
            if chose <= wahrscheinlichkeit:
                return True
        else:
            return False


class Frau(Person):
    def __init__(self, vorname, nachname, geschlecht="W"):
        super().__init__(vorname, nachname, geschlecht)
        self.schwanger = False
        self.kindercounter = 0
        self.geburtsterminDD = 0
        self.geburtsterminMM = 0
        self.geburtsterminYY = 0
        self.vaterdeskindes = None

    @property
    def geschlecht(self):
        return self.__geschlecht

    @geschlecht.setter
    def geschlecht(self, geschlecht):
        self.__geschlecht = geschlecht

    @property
    def schwanger(self):
        return self.__schwanger

    @schwanger.setter
    def schwanger(self, schwanger):
        self.__schwanger = schwanger

    @property
    def geburtsterminDD(self):
        return self.__geburtsterminDD

    @geburtsterminDD.setter
    def geburtsterminDD(self, geburtsterminDD):
        self.__geburtsterminDD = geburtsterminDD

    @property
    def geburtsterminMM(self):
        return self.__geburtsterminMM

    @geburtsterminMM.setter
    def geburtsterminMM(self, geburtsterminMM):
        self.__geburtsterminMM = geburtsterminMM

    @property
    def geburtsterminYY(self):
        return self.__geburtsterminYY

    @geburtsterminYY.setter
    def geburtsterminYY(self, geburtsterminYY):
        self.__geburtsterminYY = geburtsterminYY

    def schwangerschaft(self):
        if self.vergeben and not self.impotent and self.kindercounter < 6:
            if 13 <= self.alterYY <= 20:
                wahrscheinlichkeit = (1 / (self.kindercounter + 1))
            elif 21 <= self.alterYY <= 28:
                wahrscheinlichkeit = (3 / (self.kindercounter + 1))
            elif 29 <= self.alterYY <= 39:
                wahrscheinlichkeit = (2 / (self.kindercounter + 1))
            elif 40 <= self.alterYY <= 46:
                wahrscheinlichkeit = (1 / (self.kindercounter + 1))
            else:
                wahrscheinlichkeit = 0
            chose = random.randint(1, 100)
            if chose <= wahrscheinlichkeit:
                self.schwanger = True
                self.vaterdeskindes = self.partner
                self.kindercounter += 1
                self.geburtsterminDD = self.alterDD
                x = self.alterMM
                self.geburtsterminMM = x + 9
                if self.geburtsterminMM >= 13:
                    self.geburtsterminMM -= 12
                    y = self.alterYY
                    self.geburtsterminYY = y + 1
                else:
                    self.geburtsterminYY = self.alterYY
        else:
            self.schwanger = False

    def geburt(self, personenverzeichnis, vorname, geschlecht):
        if geschlecht == 'M':
            x = Mann(vorname, self.nachname)
            x.geburtstag = self.geburtsterminDD
            x.geburtsmonat = self.geburtsterminMM
            personenverzeichnis.append(x)
        else:
            x = Frau(vorname, self.nachname)
            x.geburtstag = self.geburtsterminDD
            x.geburtsmonat = self.geburtsterminMM
            personenverzeichnis.append(x)
        x.mutter = self.vorname
        x.vater = self.partner
        self.schwanger = False
        print(f"{self.vorname} {self.nachname} hat die {self.kindercounter}. Geburt.\n")
