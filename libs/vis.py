from plotly import express as px
from plotly.offline import plot


# gibt uns ein div
# durch das Einsetzten von x, y kann man die Funktion auch für andere Werte als Anzahl & Getränke verwenden

def viz1(x, y):
    # x-Achse = x | y-Achse = y (x & y werden bei def evaluation definiert)
    fig = px.bar(x=x, y=y)
    div = plot(fig, output_type="div")
    return div


def viz2(x1, x2, y1, y2):
    fig1 = px.line(x=x1, y=y1, markers=True)
    fig2 = px.line(x=x2, y=y2, markers=True)
    div = plot(fig1, output_type="div")
    return div
