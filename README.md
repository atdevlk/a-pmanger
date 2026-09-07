# 🔐 a-pmanger

A simple, beginner-friendly, open-source **password manager** for your terminal — built with Python.

Works on **Linux** and **Termux (Android)**.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Termux-brightgreen.svg)](#-installation)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg)](#-contributing)

---

## ✨ Features

- 🔒 Store your passwords securely in one place
- 💻 Simple command-line interface — no complicated setup
- 🐧 Works on Linux
- 📱 Works on Termux (Android)
- 🆓 100% free and open source
- 🌱 Beginner friendly — great for anyone new to CLI tools

---

## 📦 Requirements

- Python 3.8 or higher
- `git`
- `pip`

---

## 🚀 Installation

### 🐧 Linux

```bash
# 1. Clone the repository
git clone https://github.com/atdevlk/a-pmanger.git

# 2. Move into the project folder
cd a-pmanger

# 3. Install the required dependencies
pip install -r requirements.txt --break-system-packages

# 4. Run the app
python3 run.py
```

> 💡 Note: On newer Linux distros (Debian/Ubuntu based), `pip` blocks system-wide installs by default — `--break-system-packages` is needed to bypass that.

### 📱 Termux (Android)

```bash
# 1. Update Termux packages
pkg update && pkg upgrade

# 2. Install git and python
pkg install git python -y

# 3. Clone the repository
git clone https://github.com/atdevlk/a-pmanger.git

# 4. Move into the project folder
cd a-pmanger

# 5. Install the required dependencies
pip install -r requirements.txt

# 6. Run the app
python3 run.py
```

---

## 🧭 Usage

After installation, simply run:

```bash
python3 run.py
```

Follow the on-screen menu to:

- ➕ Add a new password
- 📋 View saved passwords

> 💡 Tip: Never share your master password with anyone.

---

## 🆕 What's New in v1.1

- 🐛 Fixed SHA256 hashing bug
- 🐛 Fixed Key-related bug
- 🔄 Changed `python` to `python3`

---

## 🗺️ Roadmap

- [ ] Master password encryption
- [ ] Export / Import passwords
- [ ] Password generator
- [ ] Auto-lock after inactivity
- [ ] GUI version (future)

---

## 🤝 Contributing

Contributions are welcome and appreciated! 🎉

1. Fork this repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -m "Add: your feature"`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Open a Pull Request

If you find a bug or have a feature request, feel free to [open an issue](https://github.com/atdevlk/a-pmanger/issues).

---

## 📄 License

This project is licensed under the **MIT License** — a simple, permissive license that lets anyone use, modify, and distribute this project freely, even commercially, as long as the original license is included.

See the [LICENSE](LICENSE) file for full details.

---

## 👤 Author

**atdevlk**
GitHub: [@atdevlk](https://github.com/atdevlk)

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub — it really helps!
