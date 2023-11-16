import os
import math
#from pyfiglet import figlet_format

def Bar(material=None,thickness=1):
    width, height = os.get_terminal_size()
    if material == None: material="-"
    print((material * math.floor(width/len(material)))*thickness)
    
def VBar(rowcount,material="-",endmaterial=None,thickness=1):
    width, height = os.get_terminal_size()
    if endmaterial==None: endmaterial=material
    print((material*thickness + " "*(width - 2*thickness) + endmaterial*thickness + "\t")*rowcount)

def Box(boxtext=[],material="-",boxSizeByLargestString=True):
    width, height = os.get_terminal_size()
    largestString = 0
    for text in boxtext:
        if len(text) > largestString: largestString = len(text)
    slotstring = ""
    looper = 0
    for text in boxtext:
        divideAdd = 0
        if (largestString/2)%1 != 0 and len(boxtext[looper]) != largestString and (len(boxtext[looper])/2)%1 == 0:
            divideAdd = 1
        if boxSizeByLargestString:
            slotstring += (("-"*((int((width-len(boxtext)*(largestString+len(material)*2))/(len(boxtext)+1)))) + "["+int((largestString-len(boxtext[looper]))/2)*" "+boxtext[looper]+int((largestString-len(boxtext[looper]))/2)*" "+divideAdd*" "+"]"))
        else:
            slotstring += (("-"*((int((width-len(boxtext)*(largestString+len(material)*2))/(len(boxtext)+1)))) + "["+boxtext[looper]+"]"))
        looper += 1
    #PrintBox
    Bar(material)
    print(slotstring+material*(width-len(material)-len(slotstring))+material)
    Bar(material)

#def Asciitxt(text,font,center):
    #0: left, 1: center, 2: right
    #width, height = os.get_terminal_size()
    #if center:
        #return figlet_format(text,font=font).center(width)
    #else:
        #return figlet_format(text,font=font)

Box(["ability 1: slash", "ability 259: 'Press w to activate'"],"-",True)
Bar("w",1)
VBar(2,"[","]",1)