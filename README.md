# 🔍 Simple Python Port Scanner

This is a basic multithreaded TCP port scanner written in Python. It scans a target host for the availability of common service ports such as HTTP, HTTPS, SSH, DNS, and SMTP.

## ✅ Features

- Scans selected common ports: 22 (SSH), 25 (SMTP), 53 (DNS), 80 (HTTP), 443 (HTTPS)
- Multithreaded for faster scanning
- Uses only the Python standard library
- Clearly labeled output with service names
- Handles connection errors gracefully

## 🚀 How to Use

### 1. Clone the repository (or copy the script)

```bash
git clone https://github.com/Smisugi/simple-port-scanner.git
cd simple-port-scanner
```

### 2. Run the script

```bash
python main.py
```

You will be prompted the enter the host IP you want to scan.

Feel free to modify the list of scann ports in the script.

### 🔧 Requirements

Python 3.6+
No external libraries required
