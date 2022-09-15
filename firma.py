import random


class Firma:
    def __init__(self, name, arbeitsplaetze):
        self.name = name
        self.benoetigtesguthaben = 0
        self.inhaber = None
        self.arbeitsplaetze = arbeitsplaetze
        self.mitarbeiter = []
        self.jobs = []  # JOB: RUHM, JOB: RUHM
        self.ruhm = []

    @property
    def mitarbeiter(self):
        return self.__mitarbeiter

    @mitarbeiter.setter
    def mitarbeiter(self, mitarbeiter):
        self.__mitarbeiter = mitarbeiter

    @property
    def inhaber(self):
        return self.__inhaber

    @inhaber.setter
    def inhaber(self, inhaber):
        self.__inhaber = inhaber

    @property
    def jobs(self):
        return self.__jobs

    @jobs.setter
    def jobs(self, jobs):
        self.__jobs = jobs

    @property
    def ruhm(self):
        return self.__ruhm

    @ruhm.setter
    def ruhm(self, ruhm):
        self.__ruhm = ruhm

    def firma_gruenden(self, inhaber):
        self.inhaber = inhaber
        inhaber.firma = self.name
        inhaber.job = self.jobs[0]
        inhaber.ruhm += self.ruhm[0]

    def mitarbeiter_leben_check(self, tag):     # Leben die Mitarbeiter noch?
        if tag == 4:
            for ma in self.mitarbeiter:
                if not ma.aktiv:
                    print('inaktiver mitarbeiter')

    def mitarbeiter_gesucht_check(self):    # Sind genug Leute eingestellt?
        if len(self.mitarbeiter) < self.arbeitsplaetze:
            return True
        else:
            return False

    def mitarbeiter_einstellen(self, neuerarbeiter):    # Arbeiter xy einstellen.
        self.mitarbeiter.append(neuerarbeiter)
        neuerarbeiter.job = self.jobs[len(self.mitarbeiter)+1]
        neuerarbeiter.ruhm += self.ruhm[len(self.mitarbeiter)+1]


class Fleischerei(Firma):
    def __init__(self, arbeitsplaetze=random.randint(1, 4)):
        super().__init__('Fleischerei XY', arbeitsplaetze)
        self.jobbies()
        self.benoetigtesguthaben = 1000

    def jobbies(self):  # Teilt die Jobs : Ruhm zu
        i = 1
        while i <= self.arbeitsplaetze:
            if i == 1:
                self.jobs.append('Fleischermeister')
                self.ruhm.append(3)
            elif i == 2:
                self.jobs.append('Metzger')
                self.ruhm.append(2)
            elif i == 3:
                self.jobs.append('Verkaeufer')
                self.ruhm.append(1.5)
            elif i == 4:
                self.jobs.append('Auszubildender')
                self.ruhm.append(1)
            i += 1


class Mueller(Firma):   # Getreidemahler
    def __init__(self, arbeitsplaetze=random.randint(2, 4)):
        super().__init__('Bauernhof Heidewitzka', arbeitsplaetze)
        self.jobbies()
        self.benoetigtesguthaben = 500

    def jobbies(self):  # Teilt die Jobs : Ruhm zu
        i = 1
        x = 1
        while i <= self.arbeitsplaetze:
            if i == 1:
                self.jobs.append('Bauer')
                self.ruhm.append(2.5)
            elif i == 2:
                self.jobs.append('Frau')
                self.ruhm.append(1.5)
            elif i >= 2:
                self.jobs.append(f'Kind{x}')
                self.ruhm.append(1)
                x += 1
            i += 1


'''class Bauernhof(Firma):
class Maurer(Firma):
class Schmied(Firma):
class Schuerferei(Firma):'''
