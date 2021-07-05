import os.path

if os.path.isfile("/usr/bin/customapp"):
    print("\xE2\x9C\x85 Required software is installed")
else:
    print("\xE2\x9D\x8C The required software is not installed. \xE2\x9D\x8C")
    print("Please install customapp before running this tool.")
    quit()

print("Program continues to run")