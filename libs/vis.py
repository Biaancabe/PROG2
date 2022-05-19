from plotly import express as px
from plotly.offline import plot


def viz1(x, y):
    # x-Achse = x | y-Achse = y (x & y werden bei def evaluation definiert)
    fig = px.bar(x=x, y=y)
    div = plot(fig, output_type="div")
    return div


def viz2(x, y):
    dr = px.data.gapminder().query("getraenk=='getraenk'")
    fig = px.line(df, x=x, y=y, colour="getraenk")
    div = plot(fig, output_type="div")
    return div