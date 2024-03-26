from gpiozero import Button
from signal import pause
import subprocess

# Define the GPIO pin for the switch. In this case GPIO 5 (Physical Pin 29) was used.
switch = Button(5) 

kismet_process = None

def start_kismet():
    global kismet_process
    if kismet_process is None or kismet_process.poll() is not None:
        print("Starting Kismet...")
        kismet_process = subprocess.Popen(['kismet'])

def stop_kismet():
    global kismet_process
    if kismet_process is not None:
        print("Stopping Kismet...")
        kismet_process.terminate()
        kismet_process = None

# Execute start_kismet when the button is pressed
switch.when_pressed = start_kismet
# Execute stop_kismet when the button is released
switch.when_released = stop_kismet

pause()
