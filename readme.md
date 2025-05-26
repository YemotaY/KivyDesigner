# Kivy-Designer

## 1. Zielsetzung und Konzeptualisierung
### Ziel
_Einen Kivy-Designer erstellen, mit dem Benutzer visuell und interaktiv Kivy-GUI-Elemente anordnen, konfigurieren und die resultierenden Python-Skripte generieren können._

## Features
- **Drag-and-Drop** von Kivy-Widgets (Buttons, Labels, Sliders, etc.)
- **Automatische Generierung** von Kivy-Python-Code für die Anordnung der Widgets
- **Widgets konfigurieren** (Eigenschaften wie Text, Größe, Farbe, etc.)
- **Vorschau der Benutzeroberfläche** in Echtzeit
- **Speichern** der generierten Layouts als `.kv`-Dateien oder Python-Skripte

## Technologie-Auswahl
- **Kivy:** Für die grafische Oberfläche und Interaktivität
- **Python:** Als Programmiersprache
- **JSON oder KV-Dateien:** Zum Speichern von Layouts und Widget-Eigenschaften

---

## Projektstruktur
- `main.py` – Startpunkt der Anwendung
- `designer.kv` – Kivy-Layout für das Hauptfenster
- `toolbox.py` – Toolbox-Logik (Widget-Auswahl)
- `widget_area.py` – Bereich für Drag-and-Drop und Widget-Anordnung
- `property_editor.py` – Eigenschaften-Editor für ausgewählte Widgets
- `exporter.py` – Export-Logik für `.kv` und `.py`-Dateien

## TODOs / Nächste Schritte
- [ ] Drag-and-Drop-Mechanismus für Widgets implementieren
- [ ] Eigenschaften-Editor mit Live-Update für ausgewählte Widgets
- [ ] Exportfunktion für `.kv` und `.py`-Dateien vervollständigen
- [ ] Vorschau-Funktion für das aktuelle Layout
- [ ] Unterstützung für weitere Kivy-Widgets (z.B. TextInput, CheckBox, etc.)
- [ ] Verbesserte Benutzeroberfläche und Usability
- [ ] Unit-Tests für Kernfunktionen

## Beispiel: Schnellstart
```bash
python main.py
```

## Hinweise
- Die Anwendung befindet sich im Prototyp-Stadium. Viele Funktionen sind als Platzhalter/TODO markiert.
- Für die Entwicklung wird empfohlen, ein virtuelles Python-Environment zu nutzen und die Abhängigkeiten (z.B. Kivy) zu installieren.

## Lizenz
Siehe Haupt-README oder LICENSE-Datei im Projekt.