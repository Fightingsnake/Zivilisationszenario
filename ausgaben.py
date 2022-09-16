class Ausgabe:
    def __init__(self):
        print("hallo")

    def abfrage(self):
        while True:
            print("( 1 ) : Übersicht Menschen\n"
                  "( 2 ) : Übersicht Tote\n"
                  "( 3 ) : Statistiken\n"
                  "( q ) : weiter")

            wahl = input("Was möchtest du tun?")
            if wahl == '1':
                return 1
            elif wahl == '2':
                return 2
            elif wahl == '3':
                return 3
            elif wahl == 'q':
                break
            print("Versuch es noch Mal.")

