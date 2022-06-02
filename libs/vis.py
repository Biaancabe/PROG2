from plotly import express as px
from plotly.offline import plot
from flask import request
import plotly.graph_objects as go

# gibt uns ein div
# durch das Einsetzten von x, y kann man die Funktion auch für andere Werte als Anzahl & Getränke verwenden


def viz1(x, y):
    # x-Achse = x | y-Achse = y (x & y werden bei def evaluation definiert)
    fig = px.bar(x=x, y=y)
    div = plot(fig, output_type="div")
    return div


def viz2(x1, x2, y1, y2):
    getraenk1 = request.form.get("getraenk1")
    getraenk2 = request.form.get("getraenk2")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x1, y=y1, name=getraenk1, mode="lines", line=dict(color='blue', width=1)))
    fig.add_trace(go.Scatter(x=x2, y=y2, name=getraenk2, mode="lines", line=dict(color='red', width=1)))
    fig.update_layout(
        template='simple_white',
        yaxis_title='Anzahl',
        xaxis_title='Getränk',
        title='Getränke Vergleich',
        hovermode="x"
    )
    div = plot(fig, output_type="div")
    return div
