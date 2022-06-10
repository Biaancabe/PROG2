<h1>ReadMe Bianca Bernasconi</h1>

<h3>Problembeschreibung/Motivation</h3>
*Warum dieses Projekt*
<br> Ich arbeite in einer Bar und möchte meinen Chef schon lange überzeugen ein gewisses Getränk in die Karte aufzunehmen.
Um ihm zu zeigen, dass das Getränk gut laufen wird, möchte ich ihm aufzeigen, welches Getränk wie gut ankommt und wann wie oft verkauft wird. 

*Welches Problem löst das Projekt*
<br> Dank dem Projekt können täglich oder monatlich Daten ausgewertet werden. Es wird gezeigt welches Getränk im allgemeinen am Besten läuft. 
Es können ausserdem weitere Auswertungen generiert werden wie beispielsweise an welchem Tag läuft "Bier" am Besten. Anhand diesen Angaben kann der Lagerbestand
kontrolliert werden und anhand der Nachfrage können Anpassungen beim Preis gemacht werden.

*Was macht das Projekt*
<br> In einer Bar ist oft nicht klar, welche Getränke am Besten laufen, welche am meisten Umsatz generieren, etc.
Das Projekt soll diese Problem lösen. Durch das tägliche eintragen von den verkauften Getränken soll Ende Monat ersichtlich werden,
welches Getränk am Besten lief, welche Abende brachten den höchsten Umsatz, gibt es Trends welche Getränke zu welchen Zeiten / Tagen konsumiert werden. Und noch viele weitere Datenauswertungen sind möglich.


<h3>Betrieb</h3>
Damit die Applikation korrekt funktioniert, müssen folgende Module importiert werden:
<br> - Flask (Flask, render_template, request)
<br> - Plotly
<br> - Datetime


*Welch Datei muss ausgeführt werden*
<br> **main.py**


<h3>Benutzung</h3>
<h4>Home</h4>
Dank der Navigation kann man sich durch die verschiedenen Seiten klicken. 
<br>Die Home- / Startseite dient als Einstieg in das Projekt und hat keine Funktion.

<h4>Drinks Sale</h4>
Mit dem Dropdown-Menü kann man das Getränk auswählen. Es stehen die Getränke zur Auswahl, welche auch in der Bar verkauft werden.
Anschliessend gibt man an, wie oft dieses Getränk verkauft wurde. 
<br> **Wichtig**: Am Ende des Tages wird es 1 x ausgefüllt. Die Daten werden anhand des Datums gespeichert.
<br> durch das Klicken auf "Bestätigen" gelangt man zu Eingabebestätigungs-Seite, welche zeigt, dass die Eingabe geklappt hat. Hier kann man zurück navigieren und kommt wieder
auf die Drinks Sale - Seite, oder man geht über die Navigation auf eine andere Seite.

<h4>Drinks Overview</h4>
Diese Seite gibt eine Übersicht über die verkauften Getränke. Man kann ein Getränk auswählen und dann
wird eine Liste gezeigt, wann dieses Getränk wie oft verkauft wurde.
Falls man Nichts auswählt, dann wird einfach eine Liste mit der ganzen Übersicht gezeigt.

<h4>Evaluation</h4>
Die Evaluationsseite dient zur Grafischen Darstellung von Berechnungen. 
Man kann das Datum auswählen und ein Balkendiagramm zeigt dann an, welches Getränk an diesem Tag wie oft verkauft wurde.
Somit bekommt man ein Überblick, welches Getränk am Abend am besten performt hat und welches am schlechtesten.

<h4>Relation</h4>
Hier besteht die Möglichkeit, zwei Getränke miteinander zu vergleichen.
Man wählt dafür zwei Getränke aus und anschliessend wird für jedes Getränk ein Graph generiert,
welcher den Verlauf zeigt. Die Y-Achse zeigt die Anzahl und die X-Achse den Tag.


<h3>Architektur</h3>
![Diagramm](./static/pictures/Ablaufdiagramm_Projekt_Pythonbaby.png)



<h3>Ungelöste/unbearbeitete Probleme</h3>
- Wenn man ein Getränk bei "Sales" eingibt, und dabei kein Getränk auswählt und keine Anzahl eingibt, wird es 
trotzdem in die Datenbank eingefügt und dadurch kommt es zu Fehlermeldungen da Anzahl = "" ist.

- Wenn man bei "Evaluation" ein Datum auswählt, bei dem Nichts eingetragen ist. 
Könnte man eine Meldung bekommen dass Nichts verkauft wurde, anstelle des Diagramms.


