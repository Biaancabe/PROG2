from datetime import datetime
import json

# Alle Informationen in der Klammer werden in Json Datei gespeichert.
# Man öffnet Json Datei und schreibt diese Informationen hinein. Datei steht für json-datei
def speichern(datei, key, value, zeitpunkt, datum):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}
    datei_inhalt[str(zeitpunkt)] = {"getraenk": key, "anzahl": value, "datum": datum}
    # print(datei_inhalt), w steht für write - also bearbeiten
    with open(datei, "w") as open_file:
        # json.dump wandelt ein Python-Objekt in einen json-String um
        json.dump(datei_inhalt, open_file)



def eingabebestaetigung(getraenk, anzahl):
    datei_name = "datenspeicher.json"
    zeitpunkt = datetime.now()
    datum = datetime.now().date()
    datum = str(datum)
    # In Kalmmer erwähnte Informationen werden gemäss in def speichern()
    # erwähnte Informationen in der Klammer gespeichert.
    speichern(datei_name, getraenk, anzahl, zeitpunkt, datum)
    return getraenk, anzahl, zeitpunkt, datum


# Inhalte in Json-Datei werden geladen und können dann ausgewertet werden
def drinks_laden():
    datei_name = "datenspeicher.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt
