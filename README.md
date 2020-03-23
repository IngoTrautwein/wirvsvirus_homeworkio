# Introduction

Im Kontext des Hackathons [wirvsvirus](https://www.bundesregierung.de/breg-de/themen/coronavirus/wir-vs-virus-1731968) stellt dieses Repository die Code-Basis für die Challange "E-Learning. Wie können wir Weiterbildungsmöglichkeiten/Online-Learning anbieten im spez. Hausaufgabenverwaltung". Hier das dazugehörige [Devpost](https://devpost.com/software/019_e-learning_homework-io)

## Hinweis

Der entwickelte Code enthält noch einige Fehler, daher kann keine Fehlerfreie Verwendung garantiert werden.

## Inhalt

Dieses Repository enthält den Quellcode für das Backend sowie das Datenbankschema.
Das dazugehörige: [Repository Frontend](https://github.com/Social-Developers-Club/homework.io) - entwickelt von [Dominik Sasse](https://github.com/DominikSasse) & [Julia Heidinger](https://github.com/juliaaheidinger)

## Entwickler Backend

- [Ingo Trautwein](https://github.com/IngoTrautwein)
- [Marcel Pleyer](https://github.com/Marcel-Pleyer)

## Installationsanleitung (Backend)

Die Anwendung wurde mit Python Version 3 entwickelt.
- Python 3.x installieren

Zur Ausführung der Anwendung müssen externe Bibliotheken installiert werden:
- Abhängigkeiten mit pip3 installieren: ```pip3 install -r requirements.txt```

src-Ordner als ```Sources Root``` deklarieren

Die MySQL-Datenbank kann importiert werden via ```homeworkio.sql```

Der folgende Befehl startet die Anwendung: ```python3 rest_service.py```
