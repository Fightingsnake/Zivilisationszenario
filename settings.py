import random


class Settings:
    '''Class fuer die Einstellungen.'''
    # Farben fuer print()
    OK = '\033[92m'  # GREEN
    WARNUNG = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR
    def __init__(self):
        # Startbedingungen
        self.startmann = 150
        self.startfrau = 150

        # Zeiteinstellungen
        self.startmonat = 10

        self.durchlaufzyklen = 10009
        self.zwischenstaende = 12*30

        # Personeneinstellungen
        self.schritte = 1   # Schritte im Alterungsprozess > IN TAGEN <
                            # (Multiplikator; 1 tag im Kalender = x schritte aelter/person)

        # Gesellschaftseinstellungen
        self.zuzugchance = 0.015
        self.freieJobs = {'Bauer': 2, 'Mueller': 2, 'Fleischer': 1, 'Maurer': 0}  # Meister (fuer firmengruendung)

        # Krankheitseinstellungen
        self.grippeFaktor = 0.25

    @property
    def freieJobs(self):
        return self.__freieJobs

    @freieJobs.setter
    def freieJobs(self, freieJobs):
        self.__freieJobs = freieJobs
