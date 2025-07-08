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