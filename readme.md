# Kivy-Designer

Ein visueller Designer für Kivy-GUI-Anwendungen mit Drag-and-Drop-Funktionalität und automatischer Code-Generierung.

## ✅ Implementierte Features
- **Drag-and-Drop** von Kivy-Widgets (Button, Label, Slider, TextInput, CheckBox, ProgressBar)
- **Automatische Generierung** von Kivy-Python-Code und .kv-Dateien
- **Toolbox** mit verfügbaren Widgets zum Hinzufügen
- **Widget-Bereich** für die visuelle Anordnung
- **Eigenschaften-Editor** für ausgewählte Widgets
- **Export-Funktionalität** für `.kv` und `.py`-Dateien
- **Echtzeit-Vorschau** der Benutzeroberfläche

## 📋 Anforderungen
- **Python:** 3.8+
- **Kivy:** 2.1.0+
- **Betriebssystem:** Windows, macOS, Linux

## 🏗️ Projektstruktur
```
KivyDesigner/
├── main.py              # Hauptanwendung - Startpunkt
├── designer.kv          # Kivy-Layout für das Hauptfenster
├── toolbox.py           # Widget-Toolbox mit Drag-and-Drop
├── widget_area.py       # Arbeitsbereich für Widget-Anordnung
├── property_editor.py   # Eigenschaften-Editor für Widgets
├── exporter.py          # Export nach .kv und .py Dateien
├── demo_layout.py       # Demo-Layout zum Testen
├── requirements.txt     # Python-Abhängigkeiten
├── setup.bat           # Windows-Setup-Skript
└── README.md           # Diese Datei
```

## 🎯 Funktionen im Detail

### Verfügbare Widgets
- **Button** - Interaktive Schaltflächen
- **Label** - Textanzeige
- **Slider** - Schieberegler mit min/max/value
- **TextInput** - Texteingabefelder
- **CheckBox** - Kontrollkästchen
- **ProgressBar** - Fortschrittsbalken

### Drag-and-Drop
1. Widget aus der Toolbox auswählen
2. In den Arbeitsbereich ziehen
3. Position und Größe anpassen
4. Eigenschaften im Property-Editor bearbeiten

### Export-Optionen
- **KV-Format**: Kivy-spezifische Layout-Dateien
- **Python-Format**: Vollständige Python-Klassen mit Widget-Definitionen

## 🧪 Test-Status (PowerShell getestet)

### ✅ Erfolgreich getestet
- Hauptanwendung startet korrekt (`python main.py`)
- Demo-Layout funktioniert (`python demo_layout.py`)
- Export-Funktionen arbeiten (`python exporter.py`)
- Kivy 2.3.1 kompatibel
- Python 3.10 kompatibel

### 📊 Test-Umgebung
- **OS**: Windows
- **Shell**: PowerShell
- **Python**: 3.10.0
- **Kivy**: 2.3.1
- **Test-Datum**: 12. Juni 2025

## 🚀 Schnellstart

### Installation (PowerShell)
```powershell
# Repository klonen
git clone <repository-url>
cd KivyDesigner

# Abhängigkeiten installieren
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Oder verwenden Sie das Setup-Skript:
.\setup.bat
```

### Anwendung starten
```powershell
python main.py
```

### Demo-Layout testen
```powershell
python demo_layout.py
```

### Export-Funktionen testen
```powershell
python exporter.py
```

## 🛠️ Entwicklung & Erweiterung

### Nächste geplante Features
- [ ] Undo/Redo-Funktionalität
- [ ] Widget-Gruppierung und -Hierarchie
- [ ] Weitere Kivy-Widgets (Image, Video, etc.)
- [ ] Layout-Container (BoxLayout, GridLayout, etc.)
- [ ] Farbauswahl und Styling-Optionen
- [ ] Widget-Alignment und Snapping
- [ ] Template-System für häufige Layouts
- [ ] Plugin-System für benutzerdefinierte Widgets

### Bekannte Einschränkungen
- Momentan nur FloatLayout-basierte Layouts
- Begrenzte Widget-Eigenschaften im Property-Editor
- Keine Unterstützung für Widget-Events/Callbacks

## 🤝 Beitragen

### Entwicklungsumgebung einrichten
```powershell
# Virtual Environment erstellen (empfohlen)
python -m venv kivy_designer_env
.\kivy_designer_env\Scripts\Activate.ps1

# Abhängigkeiten installieren
pip install -r requirements.txt

# Entwicklung starten
python main.py
```

### Code-Struktur
- **main.py**: Hauptanwendung und App-Klasse
- **toolbox.py**: Widget-Palette und Drag-Quelle
- **widget_area.py**: Drop-Zone und Widget-Management
- **property_editor.py**: Widget-Eigenschaften bearbeiten
- **exporter.py**: Code-Generation für KV und Python

## 🐛 Troubleshooting

### Häufige Probleme
1. **Import-Fehler**: Stellen Sie sicher, dass Kivy korrekt installiert ist
2. **Performance**: Für bessere Performance nutzen Sie ein Virtual Environment
3. **Windows-spezifisch**: Einige Kivy-Features benötigen Visual C++ Redistributables

### Debug-Modus
```powershell
# Verbose Logging aktivieren
$env:KIVY_LOG_LEVEL="debug"
python main.py
```

## 📝 Beispiel-Workflow

1. **Anwendung starten**
   ```powershell
   python main.py
   ```

2. **Widget hinzufügen**
   - Button aus Toolbox in den Arbeitsbereich ziehen
   - Position durch Drag-and-Drop anpassen

3. **Eigenschaften bearbeiten**
   - Widget auswählen
   - Text, Größe oder andere Eigenschaften im Property-Editor ändern

4. **Layout exportieren**
   - "Export KV" für Kivy-Layout-Dateien
   - "Export Python" für vollständige Python-Anwendungen

5. **Generierte Dateien verwenden**
   ```powershell
   # Generierte Python-Datei testen
   python layout.py
   ```

## 📄 Ausgabe-Beispiele

### KV-Format
```kv
<GeneratedLayout>:
    Button:
        pos: 100, 200
        size: 150, 50
        size_hint: None, None
        text: "Mein Button"
```

### Python-Format
```python
class GeneratedLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        button_1 = Button(
            pos=(100, 200),
            size=(150, 50),
            size_hint=(None, None),
            text="Mein Button"
        )
        self.add_widget(button_1)
```

## 🙏 Danksagungen

Dieses Projekt nutzt:
- [Kivy](https://kivy.org/) - Cross-platform Python Framework
- [Python](https://python.org/) - Programmiersprache

## 📞 Support

Bei Fragen oder Problemen:
1. Überprüfen Sie die Troubleshooting-Sektion
2. Erstellen Sie ein Issue im Repository
3. Testen Sie mit der neuesten Version

---

## 📜 Lizenz

MIT License - Siehe LICENSE-Datei für Details.

**Entwickelt mit ❤️ für die Kivy-Community**