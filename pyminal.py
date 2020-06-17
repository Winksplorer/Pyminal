from commands.plano import *
from commands.about import *
from commands.licenseofterm import *

print('Gordae Pyminal [Version 0.1]')

while True:
    command = input('>>>')


    if command == "help":
        help()

    if command == "about":
        aboutmin()

    if command == "license":
        licenseoftermin()
