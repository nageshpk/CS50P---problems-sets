from pyfiglet import Figlet
import sys
from random import choice



figlet = Figlet()
font_list = figlet.getFonts()



if len(sys.argv) < 2:
    user = input("Input: ")
    print(figlet.renderText(user))
elif sys.argv[1] != "-f" or sys.argv[2] not in font_list:
    sys.exit("Invalid usage")
else:
    user = input("Input: ")
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(user))