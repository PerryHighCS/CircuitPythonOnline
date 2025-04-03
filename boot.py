import usb_cdc
import storage
import os

# Default: REPL, no CIRCUITPY
enable_repl = True
enable_drive = False

# Check for REPL flag file
try:
    with open("/msc.on") as f:
        enable_drive = True
        os.remove("/msc.on")
except OSError:
    pass  # File not found — use default behavior

usb_cdc.enable(console=enable_repl, data=False)

if enable_drive:
    storage.enable_usb_drive()
else:
    storage.disable_usb_drive()
