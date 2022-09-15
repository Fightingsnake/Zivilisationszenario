from random import random as ran


class Krankheit:
    def __init__(self, name):
        #
        self.name = name
        self.infektChance = 1
        self.toedlichkeit = 1
        self.dauer = 0  # in Tagen.
        self.vererbbar = False
        self.uebertragbar = False
        self.erbChance = 0
        self.ruhmaenderung = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def infektChance(self):
        return self.__infektChance

    @infektChance.setter
    def infektChance(self, infektChance):
        self.__infektChance = infektChance

    @property
    def uebertragbar(self):
        return self.__uebertragbar

    @uebertragbar.setter
    def uebertragbar(self, uebertragbar):
        self.__uebertragbar = uebertragbar

    @property
    def toedlichkeit(self):
        return self.__toedlichkeit

    @toedlichkeit.setter
    def toedlichkeit(self, toedlichkeit):
        self.__toedlichkeit = toedlichkeit

    @property
    def vererbbar(self):
        return self.__vererbbar

    @vererbbar.setter
    def vererbbar(self, vererbbar):
        self.__vererbbar = vererbbar

    @property
    def erbChance(self):
        return self.__erbChance

    @erbChance.setter
    def erbChance(self, erbChance):
        self.__erbChance = erbChance

    @property
    def dauer(self):
        return self.__dauer

    @dauer.setter
    def dauer(self, dauer):
        self.__dauer = dauer

    def zuweisung_pruefen(self, krankheit):
        if ran() * 100 < krankheit.chance:
            print("Krankheit zufuegen/verteilen")

    def initialisieren(self, p):
        self.zuweisung_pruefen(tumor)
        self.zuweisung_pruefen(hiv)
        self.zuweisung_pruefen(grippe)
        '''nicht jede krankheit bekommt man sofort, oder ueberhaupt'''

    def updater(self, p):  # Wahrscheinlichkeit die Krankheit zu bekommen.
        print('x')


class Tumor(Krankheit):
    def __init__(self, name='Tumor'):  # TODO: infektChance an alter anpassen...
        super().__init__(name)
        self.infektChance = 5
        self.toedlichkeit = 0.05
        self.vererbbar = True
        self.erbChance = 20
        self.ruhmaenderung = 1

    def updater(self, p):
        if p.geschlecht == 'W':
            if p.alterYY < 13:
                self.infektChance = 0.01
            elif 13 <= p.alterYY <= 30:
                self.infektChance = 0.02
            elif 31 <= p.alterYY <= 50:
                self.infektChance = 0.03
            elif 51 <= p.alterYY <= 80:
                self.infektChance = 0.04
            elif p.alterYY >= 81:
                self.infektChance = 0.05
        elif p.geschlecht == 'M':
            if p.alterYY < 13:
                self.infektChance = 0.0125
            elif 13 <= p.alterYY <= 30:
                self.infektChance = 0.025
            elif 31 <= p.alterYY <= 50:
                self.infektChance = 0.033
            elif 51 <= p.alterYY <= 80:
                self.infektChance = 0.045
            elif p.alterYY >= 81:
                self.infektChance = 0.06


class Grippe(Krankheit):
    def __init__(self, name='Grippe'):
        super().__init__(name)
        self.infektChance = 0.25
        self.toedlichkeit = 0.005
        self.dauer = 17
        self.uebertragbar = True
        self.ruhmaenderung = -2

    def updater(self, p):
        if p.alterYY < 8:
            self.infektChance = 0.5 / 150
        elif 9 <= p.alterYY <= 20:
            self.infektChance = 0.3 / 150
        elif 21 <= p.alterYY <= 35:
            self.infektChance = 0.2 / 150
        elif 36 <= p.alterYY <= 59:
            self.infektChance = 0.1 / 150
        elif 60 <= p.alterYY <= 70:
            self.infektChance = 0.25 / 150
        elif 71 <= p.alterYY <= 80:
            self.infektChance = 0.4 / 150
        elif 81 <= p.alterYY <= 90:
            self.infektChance = 0.5 / 150
        elif p.alterYY >= 91:
            self.infektChance = 0.75 / 150


class Hiv(Krankheit):
    def __init__(self, name='HIV'):
        super().__init__(name)
        self.infektChance = 1 / 58800
        self.toedlichkeit = 0.018
        self.vererbbar = True
        self.erbChance = 10
        self.ruhmaenderung = -5

    def updater(self, p):
        if 26 <= p.alterYY <= 55:
            self.infektChance = 1 / 588


krankheitenVerzeichnis = [Hiv(), Tumor(), Grippe()]
