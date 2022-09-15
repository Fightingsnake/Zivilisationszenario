import random


class Funktionen:
    def vornamegenerieren(self):
        namenstuecke = ['anne', 'erik', 'ingrid', 'ursula', 'olaf', 'annegret', 'neil', 'ilsa', 'oleg', 'ulf', 'erika',
                        'dirk', 'arndt', 'franz', 'mathias', 'sascha', 'astrid', 'hurensohn', 'horst', 'john', 'rick',
                        'bernhard', 'bernhold', 'bertha', 'enno', 'emmerich', 'falko', 'ferdinand', 'gerald', 'gilmar',
                        'godwin', 'gundula', 'hadrich', 'heike', 'heribald', 'hildebrand', 'ilga', 'jetta', 'landolf',
                        'lutz', 'maik', 'mombert', 'nantwig', 'odulf', 'otthein', 'radbod', 'ralf', 'richwin', 'ron',
                        'siegwald', 'siri', 'thilo', 'trutz', 'uland', 'walbert', 'wiborg', 'winhard', 'yngvar']
        namenstring = random.choice(namenstuecke)

        return namenstring

    def nachnamegenerieren(self):
        namenstuecke = ['hausen', 'schmidti', 'smith', 'schneider', 'musterman', 'junkers', 'neilson', 'hilgram',
                        'bolek', 'maulson', 'erikson', 'irre', 'arsch', 'ampel', 'madagaskar', 'sansibar', 'astrologons']
        namenstring = random.choice(namenstuecke)

        return namenstring

    def chekleiINT(self, wahrscheinlichkeit):
        if random.randint(1, 100) <= wahrscheinlichkeit:
            return True
        else:
            return False

    def chegrosINT(self, wahrscheinlichkeit):
        if random.randint(1, 100) >= wahrscheinlichkeit:
            return True
        else:
            return False

    def chekleiFLO(self, wahrscheinlichkeit):
        if random.random()*100 <= wahrscheinlichkeit:
            return True
        else:
            return False

    def chegrosFLO(self, wahrscheinlichkeit):
        if random.random()*100 >= wahrscheinlichkeit:
            return True
        else:
            return False
