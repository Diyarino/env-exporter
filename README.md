
# 📦 env-exporter

A lightweight and handy Python script to **export your current environment dependencies** into configuration files.  
Supports both **pip** (`requirements.txt`) and **conda** (`environment.yml`) environments.

---

## 🚀 Features

- 🔹 Exports `pip` dependencies to `requirements.txt`
- 🔹 Exports `conda` environment to `environment.yml`
- 🔹 Logs status updates using Python's built-in `logging` module
- 🔹 Easy to integrate into any Python project

---

## 🛠️ Usage

### 1. Clone or download the repo

```bash
git clone https://github.com/your-username/env-exporter.git
cd env-exporter
````

### 2. Run the script

```bash
python export_env.py
```

This will generate:

* `requirements.txt` for `pip`
* `environment.yml` for `conda`

Both files will be saved in the current directory.

---

## 📁 Output Files

| File               | Description                                       |
| ------------------ | ------------------------------------------------- |
| `requirements.txt` | Pip dependencies (`pip freeze`)                   |
| `environment.yml`  | Conda environment definition (`conda env export`) |

---

## 📋 Example Log Output

```text
2025-07-14 13:45:01 - INFO - Conda environment successfully exported to 'environment.yml'.
2025-07-14 13:45:01 - INFO - Package list successfully exported to 'requirements.txt'.
```

---

## 📦 Dependencies

Only built-in libraries are used:

* `subprocess`
* `logging`

✅ No installation required.

---

## 👨‍💻 Author

**Diyar Altinses, M.Sc.**

---

## 📜 License

This project is open source.

---

## 🙌 Contributing

Feel free to fork the repo and submit pull requests if you want to improve or extend this utility!

```

