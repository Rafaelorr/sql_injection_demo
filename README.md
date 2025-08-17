**English version:**
# Flask SQL Injection Demos

A collection of intentionally vulnerable Flask web applications designed to demonstrate and practice SQL injection attacks. Perfect for educational, testing, and research purposes. Self-hostable with Docker.

---

## 🚨 Disclaimer

> **This project is for educational and legal penetration testing purposes only. Do not deploy or expose these applications to the public internet. Use in controlled, isolated environments only.**

---

## Features

- Multiple vulnerable Flask apps, each showcasing different SQL injection scenarios.
- Simple, modular structure for easy extension and customization.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Available Vulnerable Apps](#available-vulnerable-apps)
- [Usage](#usage)
- [Extending the Playground](#extending-the-playground)
- [Answers](#answers)
- [Contributing](#contributing)
- [License](#license)

---

## Getting Started

### Prerequisites

python3 and flask or docker (untested)

### Quick Start

```bash
git clone https://github.com/Rafaelorr/sql_injection_demo.git
cd sql_injection_demo
cd SCENARIO_NAME
python3 app.py
```

---

## Available Vulnerable Apps

| App Name      | Description                         
|:-------------:|:-----------------------------------:|
| `login bypass`| Basic SQL injection (login bypass)  |
| `drop attack` | Drop the *users* table with the sign up form |
| `xss test`    | Insert javascript in the comments|

---

## Usage

- Interact with each vulnerable app using your browser or tools like `curl`.
- Try different SQL injection techniques on the forms and parameters.

---

## Extending the Playground

Want to add a new vulnerable app?

1. Copy the test_skeleton folder as a template
2. Implement your new vulnerability as a Flask app.
3. Update this README.

---

## Answers

This section contains suggested answers and explanations for each vulnerable scenario.  
Use these to check your understanding or for educational walkthroughs.

| App Name       | Example Attack/Input            | Expected Result/Explanation                   |
|:--------------:|:-------------------------------:|-----------------------------------------------|
| login bypass   | `admin' --`                     | Bypasses authentication; logs in as admin.    |
| drop attack    | `test'); DROP TABLE users; -- ` | Deletes the *users* table from the database.  |
| xss test       | `<script>alert(1)</script>`     | Excute *alert(1)* when the page is loaded.    |

---

## Contributing

Contributions are welcome! Please open pull requests or issues for:

- New vulnerable apps
- Bug fixes
- Documentation improvements

---

## License

GPL-3.0 License. See [LICENSE](LICENSE) for details.

---

**Nederlandse versie:**
# Flask SQL-injectiedemo's

Een verzameling opzettelijk kwetsbare Flask-webapplicaties, ontworpen om SQL-injectieaanvallen te demonstreren en te oefenen. Perfect voor educatieve, test- en onderzoeksdoeleinden. Zelf te hosten met Docker.

---

## 🚨 Disclaimer

> **Dit project is uitsluitend bedoeld voor educatieve en juridische penetratietests. Implementeer of stel deze applicaties niet bloot aan het openbare internet. Gebruik ze alleen in gecontroleerde, geïsoleerde omgevingen.**

---

## Features

- Meerdere kwetsbare Flask-apps, elk met verschillende SQL-injectiescenario's.
- Eenvoudige, modulaire structuur voor eenvoudige uitbreiding en aanpassing.

---

## Inhoudsopgave

- [Aan de slag](#aan-de-slag)
- [Beschikbare kwetsbare apps](#beschikbare-kwetsbare-apps)
- [Gebruik](#gebruik)
- [Uitbreiden](#uitbreiden)
- [Antwoorden](#antwoorden)
- [Bijdragen](#bijdragen)
- [License](#licentie)

---

## Aan de slag

### Vereisten

python3 en flask of docker (niet getest)

### Snel starten

```bash
git clone https://github.com/Rafaelorr/sql_injection_demo.git
cd sql_injection_demo
cd SCENARIO_NAME
python3 app.py
```

---

## Beschikbare kwetsbare apps

| App-naam      | Beschrijving                                        |
|:-------------:|:---------------------------------------------------:|
| `login bypass`| Eenvoudige SQL-injectie (login bypass)              |
| `drop attack` | Verwijder de tabel *users* met het aanmeldformulier |
| `xss test`    | Voeg javascript toe aan de comments                 |

---

## Gebruik

- Interactie met elke kwetsbare app via je browser of tools zoals `curl`.
- Probeer verschillende SQL-injectietechnieken op de formulieren en parameters.

---

## Uitbreiden

Wil je een nieuwe kwetsbare app toevoegen?

1. Kopieer de map test_skeleton als sjabloon.
2. Implementeer je nieuwe kwetsbaarheid als een Flask-app.
3. Werk de README bij.

---

## Antwoorden

Deze sectie bevat voorgestelde antwoorden en uitleg voor elk kwetsbaar scenario.

Gebruik deze om je begrip te testen of voor educatieve walkthroughs.

| App-naam        | Voorbeeldaanval/invoer          | Verwacht resultaat/uitleg                    |
|:---------------:|:-------------------------------:|:--------------------------------------------:|
| login bypass    | `admin' --`                     | Omzeilt authenticatie; logt in als admin.    |
| drop attack     | `test'); DROP TABLE users; -- ` | Verwijdert de tabel *users* uit de database. |
| xss test        | `<script>alert(1)</script>`     | Voeg *alert(1)* uit wanneer de pagina laadt. |

---

## Bijdragen

Bijdragen zijn welkom! Open pull requests of issues voor:

- Nieuwe kwetsbare apps
- Bugfixes
- Verbeteringen in de documentatie

---

## Licentie

GPL-3.0-licentie. Zie [LICENSE](LICENSE) voor details.

---