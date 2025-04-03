# Circuit Playground WebSerial Console

A WebSerial-based proof-of-concept frontend for uploading and running Python code on the Adafruit Circuit Playground Express (CPX) using CircuitPython.

This project allows students to write and execute CircuitPython code from a browser-based editor with no local setup, using WebSerial to communicate directly with the device.

## 🚀 Features

- Connect to a CPX board via WebSerial
- Upload and run CircuitPython files
- Auto-detect and reconnect to devices after a reset
- Cleanly disconnect and release resources
- Live REPL output display
- Button-based UI for common actions:
  - Upload code
  - Run file
  - List files
  - Clean up non-read-only files
- REPL prompt detection and execution flow
- Connection status bar with dynamic button enable/disable
- Graceful error handling and stream cancellation

## 🧠 Why This Project?

This tool is a proof-of-concept replacing Code.org's JavaScript/firmata based Circuit Playground tool and uses CircuitPython directly. It's designed to support a classroom workflow where:

- Students write small programs in-browser
- The code is sent to the CPX and executed
- No driver installation, software download, or file copy/paste is required

## 🧪 Proof of Concept Goals

- Demonstrate seamless browser → device interaction using CircuitPython and WebSerial
- Explore how to isolate student code execution and output
- Provide a basis for more robust tools like a classroom dashboard, multi-file editor, or library loader

## 🧰 Technologies

- HTML / JavaScript
- Web Serial API
- CircuitPython 9.2.7+
- Adafruit Circuit Playground Express (tested)

## 🧱 How It Works

1. The browser requests permission to use a USB serial device.
2. Once connected, it establishes a read/write pipeline using `TextEncoderStream` and `TextDecoderStream`.
3. The code editor text is uploaded line-by-line to a temporary file on the CPX.
4. The program is executed via `exec(open("filename.py").read())`.
5. Output is streamed back to the terminal display.

The frontend handles all serial control characters required for CircuitPython REPL (Ctrl-A, Ctrl-B, etc.).

## 📦 File Structure

- /index.html // Main frontend and all JS logic 
- /boot.py    // Minimal boot.py for CPX that hides the CIRCUITPY drive


## 🔐 Permissions and Setup

When first connecting to a CPX device:
- You'll be prompted to select the board from a browser popup.
- The browser must support Web Serial (Chrome, Edge, Chromium-based).

Once authorized, the board can reconnect automatically on page load.

## 🔧 Planned Features / Stretch Goals

- ⬆️ Multiple file upload and tabbed editing
- 📂 Visual file explorer for CPX internal storage
- 📦 Auto-download required CircuitPython libraries
- 🧹 Auto-cleanup of temp files between runs

## 🧠 Author Notes

Built as a classroom tool by a computer science educator using CircuitPython in high school settings. Inspired by the need for a simplified, student-friendly development flow.

## 📝 License

MIT License
