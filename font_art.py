import os
from pyfiglet import Figlet 
c_text = Figlet(font="slant")
os.system("cls")
os.system("mode con: cols=75 lines=30")
print(c_text.renderText("Ashutosh"))