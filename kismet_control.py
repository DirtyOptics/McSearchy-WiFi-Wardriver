import RPi.GPIO as GPIO
import subprocess
import time

# Use GPIO numbers not pin numbers
GPIO.setmode(GPIO.BCM)

# Set up pin 17
pin_number = 17
GPIO.setup(pin_number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Initialize Kismet process variable
kismet_process = None

try:
    while True:
        # Check if the switch is ON
        if GPIO.input(pin_number) == GPIO.HIGH:
            if kismet_process is None or kismet_process.poll() is not None:
                # Start Kismet
                print("Starting Kismet...")
                kismet_process = subprocess.Popen(['kismet'])
        else:
            if kismet_process is not None:
                # Stop Kismet
                print("Stopping Kismet...")
                kismet_process.terminate()
                kismet_process = None
        
        # Debounce and reduce CPU usage
        time.sleep(0.5)
except KeyboardInterrupt:
    # Clean up GPIO and terminate Kismet process gracefully on script exit
    GPIO.cleanup()
    if kismet_process is not None:
        kismet_process.terminate()
