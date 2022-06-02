from flask import Flask
from flask import render_template
from flask import request
from libs import daten
from libs.vis import viz1, viz2

# __name__ steht für den Namen des Anwendungspakets (z.B. Flask) & wird von Flask verwendet,
# um Ressourcen wie Vorlagen, Assets, etc. zu identifizieren.
# Python setzt die Varialbe __name__ auf den Modulname,

app = Flask(__name__)


# Einen Routendekorator erstellen (Endung hinter URL wäre hier: ".../"
@app.route("/")
def index():
    # return um eine Ausgabe aus einer Vorlagendatei zu generieren (hier index.html),
    # welche auf Jinja2 basiert + sich im templates-Ordner der Anwendung befindet
    return render_template("index.html")


@app.route("/drinks-sale")
def drinks():
    return render_template("drinks_sale.html")


@app.route("/eingabebestaetigung", methods=["POST", "GET"])
# get = eine GET-Nachricht wird gesendet + der Server gibt die libs zurück -> um Informationen vom Webserver abzurufen
# post = um Informationen an Webserver zu senden. Zum Abrufen von Formulardaten
def eingabebestaetigung():
    # request.method = Art der Anfrage, die an Webserver gestellt wird
    # Bei Formular ausfüllen, senden wir Informationen an Webserver, also POST
    if request.method == "POST":
        getraenk = request.form.get("getraenk")
        anzahl = request.form.get("anzahl")
        daten.eingabebestaetigung(getraenk, anzahl)
        return render_template("eingabebestaetigung.html")
    # Falls das Formular nicht ausgefüllt & abgeschickt wird, soll einfach die Seite drinks_sale.html erscheinen
    return render_template("drinks_sale.html")


@app.route("/drinks-overview", methods=["POST", "GET"])
def overview():
    # ab hier sollte "Sortieren" kommen, aber es kommt FehlerMeldung
    # neue Leere Getränkeliste erstellen, in die dann die libs reingeschrieben werden
    if request.method.lower() == "post":
        getraenke_name = request.form.get("getraenk_wahl")
        # Hier wird der Datenspeicher geladen und die geladenen libs als getraenke definiert
        getraenke = daten.drinks_laden()
        # Leere Liste um das Datum und Anzahl von dem ausgewählten Getränk in die Liste zu schreiben.
        sortieren_liste = []
        for key, value in getraenke.items():
            if getraenke_name == value["getraenk"]:
                # Dictionary in Liste hinzufügen mit den libs welche zum ausgewählten Getränk gehören
                sortieren_liste.append({"datum": value['datum'],
                                        "getraenk": value['getraenk'],
                                        "anzahl": value['anzahl']})
        # "liste = sortieren_liste" heisst dass die liste, welche im HTML drinks_overview erwähnt wird
        # hier die sortieren_liste ist
        summe = total_berechnen(sortieren_liste)
        return render_template("drinks_overview.html", liste=sortieren_liste, summe=summe)
    else:
        getraenke = daten.drinks_laden()
        getraenke_liste = []
        for key, value in getraenke.items():
            getraenke_liste.append({"datum": value['datum'], "getraenk": value['getraenk'], "anzahl": value['anzahl']})
        summe = total_berechnen(getraenke_liste)
        return render_template("drinks_overview.html", liste=getraenke_liste, summe=summe)


# Total berechnung:
def total_berechnen(getraenke):
    alle_anzahl = 0
    for item in getraenke:
        alle_anzahl += int(item["anzahl"])
    return alle_anzahl


# Daten Visualisieren:

# Basic Balkendiagramm anhand allen libs (unsortiert)
# Funktion, die libs ausrechnet und die sollen dann dargestellt werden --> libs dynamisch generiert

# Evaluation anhand Datum:
@app.route("/evaluation", methods=["POST", "GET"])
def evaluation():
    if request.method == "POST":
        date = request.form.get("date")
        getraenk, anzahl = datum_wahl()
        div = viz1(getraenk, anzahl)
        return render_template("evaluation.html", viz_div=div, date=date)
    else:
        return render_template("evaluation.html")


def datum_wahl():
    getraenke2 = daten.drinks_laden()
    getraenk2 = []
    anzahl2 = []
    date = request.form.get("date")
    for key, value in getraenke2.items():
        if str(date) in str(key):
            getraenk2.append(value["getraenk"])
            anzahl2.append(int(value["anzahl"]))
    if getraenk2 == []:
        getraenk2.append("Leider kein Getränk verkauft")
        anzahl2 = [0]
    viz1(getraenk2, anzahl2)
    return getraenk2, anzahl2


# Vergleich von zwei Getränken:
@app.route("/relation", methods=["POST", "GET"])
def relation():
    if request.method == "POST":
        getraenk1 = request.form.get("getraenk1")
        getraenk2 = request.form.get("getraenk2")
        anzahl1, anzahl2, datum1, datum2 = getraenk_vergleich()
        anzahl2 = anzahl1 + anzahl2
        div = viz2(datum1, datum2, anzahl1, anzahl2)
        return render_template("relation.html",
                               viz_div=div,
                               getraenk1=getraenk1,
                               getraenk2=getraenk2)
    else:
        return render_template("relation.html")


def getraenk_vergleich():
    getraenke2 = daten.drinks_laden()
    anzahl1 = []
    anzahl2 = []
    datum1 = []
    datum2 = []
    getraenk1 = request.form.get("getraenk1")
    getraenk2 = request.form.get("getraenk2")
    for key, value in getraenke2.items():
        if getraenk1 == value["getraenk"]:
            anzahl1.append(int(value['anzahl']))
            datum1.append(value['datum'])
        if getraenk2 == value["getraenk"]:
            anzahl2.append(int(value['anzahl']))
            datum2.append(value['datum'])
    return anzahl1, anzahl2, datum1, datum2


# Create Custom Error Pages
# Invalid URL
@app.errorhandler(404)
def page_not_found():
    return render_template("404.html"), 404


# Internal Server Error
@app.errorhandler(500)
def page_not_found():
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
