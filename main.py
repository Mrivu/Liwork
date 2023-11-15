import os
from pyfiglet import figlet_format

def Bar(vertical=False,rowcount=0,material="-",endmaterial=None):
    width, height = os.get_terminal_size()
    if material == None: material="-"
    if vertical:
        if endmaterial==None: endmaterial=material
        print((material + " "*(width - 2) + endmaterial + "\t")*rowcount)
    else:
        print(material * (width - 2))

def Asciitxt(text,font,center):
    #0: left, 1: center, 2: right
    width, height = os.get_terminal_size()
    if center:
        return figlet_format(text,font=font).center(width)
    else:
        return figlet_format(text,font=font)

def Box(slots,material="-"):
    width, height = os.get_terminal_size()
    slotstring = ((" "*int((width-2-slots*10)/slots) + "[        ]")*slots)
    Bar(False,0,material)
    print(material+slotstring+material)
    Bar(False,0,material)

Box(1)
Bar(True,1,"[","]")