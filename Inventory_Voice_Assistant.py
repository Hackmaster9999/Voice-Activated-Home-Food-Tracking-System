#Test
import os.path
from os import path 
import speech_recognition as sr
import pyttsx3

def respond(msg):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    
    engine.setProperty('voice',voices[1].id)
    print(msg)
    engine.say(msg)
    engine.runAndWait()

def addItem(itemName,qt=1):
    inventoryFile = open('inventory.csv','r+')
    inventoryFile.seek(0)
    lines = inventoryFile.readlines()
    inventoryFile.close()
    #print(lines)
    found = False
    for index in range(len(lines)):
        if itemName in lines[index]:
            #print(lines[index])
            temp = lines[index].split(',')
            temp2= temp[1]
            oldQ=int(temp2)
            lines[index]=itemName+','+str(int(qt+oldQ))+'\n'
            found = True
            break
    if(not found):
        lines.append(itemName+','+str(qt)+'\n')
    inventoryFile = open('inventory.csv','w+')
    inventoryFile.seek(0) 
    inventoryFile.write("".join(lines))

def removeItem(itemName, qt=1):
    inventoryFile = open('inventory.csv','r+')
    inventoryFile.seek(0)
    lines = inventoryFile.readlines()
    inventoryFile.close()
    #print(lines)
    found = False
    for index in range(len(lines)):
        if itemName in lines[index]:
            #print(lines[index])
            temp = lines[index].split(',')
            temp2= temp[1]
            oldQ= int(temp2)
            found= True
            if oldQ-qt >0:
                lines[index]=itemName+','+str(oldQ-int(qt))+'\n'
            else:
                lines.remove(index)
            #found = True
            break
    if(not found):
        respond(itemName + ' not found')
    inventoryFile = open('inventory.csv','w+')
    inventoryFile.seek(0) 
    inventoryFile.write("".join(lines))
    respond('Remove Item')    



def main():
    # If inventory.csv does not exist, create the file
    if (not path.exists("inventory.csv")):
        inventoryFile = open('inventory.csv','w')
        inventoryFile.close()

    r = sr.Recognizer()
    text = "default"
    while(not "stop" in text.lower().strip()):            
        with sr.Microphone() as source:     
            respond("Speak Anything :")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source) 
        try:
            text = r.recognize_google(audio)    
            respond("You said : {}".format(text))
        except:
           respond("Sorry could not recognize your voice")
        if text.lower().strip() =='add item':
            addItem('milk',1)
        if text.lower().strip() =='remove item':
            removeItem('milk',1)
    
    respond("exiting")
main()
