# McSearchy - Portable WiFi Analysis Tool
A little tool to help with wardriving. It runs 4 x Alfa cards. Kismet is configured to run automatically using these 4 data sources and is toggled on/off via a switch. Runtime with 2 x Makita 6a (18v) batteries is just over 12 hours. The Rpi4 hosts and logs everything using Kismet.

# Hardware
- [`Alfa AWUS036ACH`](https://www.alfa.com.tw/) - USB WiFi Adater 2.4Ghz/5Ghz x2
- [`Alfa AWUS036AXML`](https://www.alfa.com.tw/) - USB WiFi Adater 2.4Ghz, 5Ghz & 6Ghz (Tri-Band) x2
- [`RPi4`](https://www.raspberrypi.com/) - Raspberry Pi 4b Single Board Computer (RasPi OS - Jammy)
- [`2 x Step Down Regs`](https://www.pololu.com/product/4091) - Makita Battery Step Down Regs
- [`2 x Makita Battery Terminal`](https://www.amazon.com/Makita-643838-6-Terminal-Replacement-Part/dp/B01014GPZS) - Makita Battery Termianl Part number: 6438386
- [`Mbeat USB Hub`](https://www.ple.com.au/Products/665182/mbeat-4-port-usb-a-30-hub-with-dc-port) - Mbeat or similar USB HUB. Needs to be able to inject DC. I also modded the USB-A to NOT include the power pins.
- [`USB GPS`](https://www.amazon.com/GlobalSat-BU-353N5-GNSS-Receiver-Black/dp/B0B1W1YBZC?th=1) - USB GPS reciever. These come in many flavours. As long as it works with GPSD your in buiness.

# 3D Design Files
- [`Body 1.2024 STL`](https://github.com/deeeblack/McSearchy/blob/d8a8ad45816862e5c889b6f45955ff5700517497/Body%201.2024.stl) - This design will hold 4 x Alfa Cards in the slots.
- [`Front 1.2024 STL`](https://github.com/deeeblack/McSearchy/blob/d8a8ad45816862e5c889b6f45955ff5700517497/Front%201.2024.stl) - This top lid for the box. Aligns with antennas and holds cards in tight.
- [`Makita Battery Mount`](https://www.thingiverse.com/thing:352094) - Makita Battery Mount. You can find many of these that suit the battery terminal above.

# Software
- [`RaspiOS Bookworm`](https://www.raspberrypi.com/software/) - Latest RaspiOS, because it just works well with the Pi4 and you can still install all your fav repos.
- [`Kismet`](https://www.kismetwireless.net/) - Kismet is a sniffer, WIDS, and wardriving tool for Wi-Fi, Bluetooth, Zigbee, RF, and more, which runs on Linux and macOS
- [`Kismet Packages (Nightly Build)`](https://www.kismetwireless.net/packages/) - These repositories are maintained on the Kismet server, and contain the latest Kismet releases and nightly package builds.
- [`Kismet_Control Switch.py`](https://github.com/deeeblack/McSearchy/blob/b38a719ff690216369c0e0bfd0405533536866a5/kismet_control_switch.py) - This is a physical switch that will start and stop Kismet. Its basically pulling a GPIO pin high and low and starting/stopping kismet.

# Kismet Control Switch (Python, SupervisorD, GPIO and a Switch!)
  ```
  sudo apt update
  sudo apt install python3-gpiozero
  sudo nano kismet_control_switch.py # Paste contents from repo file above.
  sudo chmod -x kismet_control_switch.py
  sudo python3 kismet_control_switch.py
  ```
- Ensure you wire as per python script. GPIO5 and GND. You can alter as required.
- If you want to get adventurous and use supervisorD, use the repo supervisorD file as an example.
- I placed the python file in /home/db/ Feel free to change directory, but alter the conf files as needed.

# SupervisorD
- [`kismet-switch-supervisorD.conf`](https://github.com/deeeblack/McSearchy/blob/32067634b13588a34a37c96f3404a9ec4581c5ec/kismet-switch-supervisorD.conf) - Manual switch conf file runs up the python code automatically.
- [`mcsearchy-supervisorD-4cards.conf`](https://github.com/deeeblack/McSearchy/blob/32067634b13588a34a37c96f3404a9ec4581c5ec/mcsearchy-supervisorD-4cards.conf) - This conf file could be used to push the data sources to a remote server (NUC or similar. At present I am not using this in McSearchy)

  ```
  sudo apt update
  sudo apt install supervisor

  # Place supervisorD conf files here:
  /etc/supervisor/conf.d

  # Run the following commands to refresh/start/stop supervisorD
  sudo supervisorctl reread
  sudo supervisorctl update
  sudo supervisorctl status all
  sudo supervisorctl stop kismet-switch-supervisorD.conf # Example use.
  ```


(This version does not have the switches installed. I have since added a power and IO switch to toggle Kismet.)
![McSearchy](https://github.com/deeeblack/McSearchy/assets/18100269/81bff66e-1ad5-4d25-af21-203acf6bb14b)
