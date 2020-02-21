# This script will shutdown you PC

import os

yourChoice = int(input("After how many seconds you want to turn off your system : "))

os.system(f"shutdown /s /t {yourChoice}")

