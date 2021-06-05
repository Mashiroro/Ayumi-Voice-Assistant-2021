import speech_recognition as sr
import os
import datetime
import calendar
#import random
#import wikipedia
import pyaudio
import webbrowser
import re
import time
import subprocess
import getpass
import glob
import random
from pytz import timezone
from time import gmtime, strftime

username = getpass.getuser()
user = getpass.getuser()
userid ="C:\\Users\\"
cdrive ="C:\\"

def ayumimenuforwake(): #listen and begins the menu 
    print("Ayumi: How can i Help you?") 
    r = sr.Recognizer()
    r.listen_in_background(sr.Microphone(), callback)
    while True: time.sleep(0.3) 

def wakeup(recognizer, audio):
    trigger = "hi"
    reg = sr.Recognizer() # this is called from the background thread
    try:
        text = reg.recognize_google(audio)
        if (bool(re.findall(trigger, text))):
            print("You said " + text)  # received audio data, now need to recognize it
            ayumimenuforwake()
    except LookupError:
        print("Oops! Didn't catch that")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Request Errpr!; {0}".format(e))


def callback(recognizer, audio):
    reg = sr.Recognizer() # this is called from the background thread
    try:
        texts = reg.recognize_google(audio)
        text = texts.lower()
        print("You said " + text)  # received audio data, now need to recognize it
        function(text)
    except LookupError:
        print("Oops! Didn't catch that")
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Request Error!; {0}".format(e))

 
def function(text):
    ############################################################################################################
    #                                         Ayumi 
            
    def ayumimenu(): #listen and begins the menu 
        print("Ayumi: How can i Help you?") 
        r = sr.Recognizer()
        r.listen_in_background(sr.Microphone(), callback)
        while True: time.sleep(0.3) 
        
    def ayumisleep(): #ayumi will listen in the background
        r = sr.Recognizer()
        r.listen_in_background(sr.Microphone(), wakeup)
        while True: time.sleep(0.1)
        
    sleepwords = "sleep|nothing|go to sleep" #when the triggeredm, ayumi will go to listen in background mode
    if (bool(re.findall(sleepwords, text))):
            print("Going back to sleep")
            ayumisleep()   
            
    exitwords = "exit" #when the triggeredm, ayumi will go to listen in background mode
    if (bool(re.findall(exitwords, text))):
            print("Shutting down")
            exit()     
            
    ############################################################################################################
    #                                         Broswer 
    #open google.com
    browserwords = "browser|open browser"
    if (bool(re.findall(browserwords, text))):
            print("Opened browser")
            webbrowser.open('https://www.google.com/', new=2)
            ayumimenu()
             
    #google search words        
    googlesearch = "google search"
    if (bool(re.findall(googlesearch, text))):
                        
        request = (re.findall('search.+',text))
        request2 = request.pop(0) #removes the []
        replaceword = request2.replace("search","") #replace the word search with ""
        final = replaceword.lstrip() #removes all any first space
        
        webbrowser.open("http://google.com/search?q="+str(final), new=1) 
        ayumimenu()
    
    bingsearch = "bing search"
    if (bool(re.findall(bingsearch, text))):
                        
        request = (re.findall('search.+',text))
        request2 = request.pop(0) #removes the []
        replaceword = request2.replace("search","") #replace the word search with ""
        final = replaceword.lstrip() #removes all any first space
        
        webbrowser.open("http://bing.com/search?q="+str(final), new=1) 
        ayumimenu()
        
    #yahoo search words    
    yahoosearch = "yahoo search"
    if (bool(re.findall(yahoosearch, text))):
                        
        request = (re.findall('search.+',text))
        request2 = request.pop(0) #removes the []
        replaceword = request2.replace("search","") #replace the word search with ""
        final = replaceword.lstrip() #removes all any first space
        
        webbrowser.open("http://search.yahoo.com/search?p="+str(final), new=1)
        ayumimenu()
        
    #open youtube.com
    youtube = "youtube|youtube.com|you tube"
    if (bool(re.findall(youtube, text))):
            webbrowser.open("https://www.youtube.com/", new=1)
            ayumimenu()
    
    #opens yotuube.com and search 
    youtubesearch = "youtube search"
    if (bool(re.findall(youtubesearch, text))):
                        
        request = (re.findall('search.+',text))
        request2 = request.pop(0) #removes the []
        replaceword = request2.replace("search","") #replace the word search with ""
        final = replaceword.lstrip() #removes all any first space
        
        webbrowser.open("https://www.youtube.com/results?search_query="+str(final), new=1) 
        ayumimenu()

    #open outlook email website
    outlook = "outlook|open outlook|hotmail|open hotmail|outlook.com"
    if (bool(re.findall(outlook, text))): 
            webbrowser.open("https://outlook.live.com/mail/", new=1)
            ayumimenu()

    #open gmail email website
    gmail = "gmail|open gmail|gmail.com"
    if (bool(re.findall(gmail, text))):    
            webbrowser.open("http://accounts.google.com/", new=1)
            ayumimenu()
    
    websearch = "\\.com|\\.net|\\.sg|\\.io|\\.to"
    if (bool(re.findall(websearch, text))):
        webbrowser.open("https://"+str(text), new=1)
        ayumimenu()


    ############################################################################################################
    #                                       Date   
    date = (datetime.datetime.now())
    year = date.strftime("%Y")
    month = date.strftime("%m") #month number
    monthalpha = date.strftime("%B") #month in alphabets
    day = date.strftime("%d") #day number
    dayalpha = date.strftime("%A") #day in alphabets
    hour = date.strftime("%I")
    minute = date.strftime("%M")
    AMPM = date.strftime("%p")
    timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzname()
    UTCgmtime = strftime("%z", gmtime())
    
    #display current date
    currentdate = "today|date|current date|what is today?"
    if (bool(re.search(currentdate, text))):
        print("Today is a "+str(dayalpha)+" "+str(day)+"/"+str(month)+"/"+str(year)+" and the time is "+str(hour)+":"+str(minute)+str(AMPM.lower()))
        ayumimenu()

    #display current timezone
    currenttimezone = "timezone|what is my timezone"
    if (bool(re.findall(currenttimezone, text))):
        print("The currrent timezone is: "+str(timezone)+" "+str(UTCgmtime))
        ayumimenu()

    #display current time
    currentclock = "clock|what time|what time is it now|current time|current clock"
    if (bool(re.findall(currentclock, text))):
        print("The time is: "+str(hour)+":"+str(minute)+str(AMPM.lower()))
        ayumimenu()

    #display current year    
    currentyear = "what is the year|current year|year"
    if (bool(re.findall(currentyear, text))):
        print("The Year is: "+str(year))
        ayumimenu()

    #display current month
    currentmonth = "month|what is the month|current month"
    if (bool(re.findall(currentmonth, text))):
        print("the Month is: "+str(monthalpha))
        ayumimenu()

    ############################################################################################################
    #                                       Birthday
    x = "11/9/2001"
    date = (datetime.datetime.now())
    year = date.strftime("%Y")
    month = date.strftime("%m") 
    day = date.strftime("%d") 

    splitx = x.split("/")
    dayday = splitx[0].lstrip()
    monthmonth = splitx[1].lstrip()
    yearyear = splitx[2].lstrip()
    thatmonthyear = calendar.monthrange(int(yearyear),int(monthmonth))[1]

    def yearagecheck():
        if monthmonth > month:
            currentyearage = (int(year) - int(yearyear) - 1)
            return currentyearage
        elif monthmonth <= month:
            currentyearage = (int(year) - int(yearyear))
            return currentyearage

    def monthagecheck():
        if dayday > day:
            currentmonthage = (int(month) - int(monthmonth) - 1)
        elif dayday <= day:
            currentmonthage = (int(month) - int(monthmonth))
        if currentmonthage <0:
            currentmonthage3 = 12 + int(currentmonthage)
            return currentmonthage3
        else:
            return currentmonthage
            
    def dayagecheck():
        currentdayage = int(day) - int(dayday)
        if currentdayage <0:
            currentdayage = thatmonthyear + currentdayage
            return currentdayage
        elif currentdayage >= 0:
            return currentdayage
    
    birthdate = "how old"
    if (bool(re.findall(birthdate, text))):
        print(str("Your current age is ")+str(yearagecheck())+str(" Years, ")+str(monthagecheck())+str(" Months and ")+str(dayagecheck())+str(" Days old"))
        
    ############################################################################################################
    #                                    Create Files / Folder
    def audiostart(): 
        reg = sr.Recognizer()
        with sr.Microphone() as source:
            audio = reg.listen(source)
            try:
                input1 = reg.recognize_google(audio)
                return input1     
                
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print("error; {0}".format(e))


    def createnewfile(): #asks for the name of file
        # obtain audio from the microphone
        print("Name of File: ")
        text1 = audiostart()
        print("Answer: ",text1)
        if text1 in ("exit","cancel"):
            exitfilecreate()
        else:
            addcontentfile(text1)

        
    def addcontentfile(text1): #asks for the content of file
        # obtain audio from the microphone
        print("Content of File: ")
        text2 = audiostart()
        print("Answer: ",text2)
        createfilelocation(text1,text2)        
        
            
    def createfilelocation(text1,text2): #asks for the location of file
        print("""Location of file: \n1. Desktop \n2. Documents \n3. Downloads \n4. Music \n5. Pictures \n6. Videos""")
        text3s = audiostart()
        print("Answer: ",text3s)
        
        if text3s in ("1","one","desktop","Desktop","number one"):
            location = '\\Desktop\\'
            text3 = str(userid) + str(username) + str(location)
            finalfilecreate(text1,text2,text3)
            
        elif text3s in ("2","two","documents","Documents","number two"):
            location = '\\Documents\\'
            text3 = str(userid) + str(username) + str(location)
            finalfilecreate(text1,text2,text3)
            
        elif text3s in ("3","three","downloads","Downloads","number three", "download"):
            location = '\\Downloads\\'
            text3 = str(userid) + str(username) + str(location)
            finalfilecreate(text1,text2,text3)
                            
        elif text3s in ("4","four","music","Music","number four"):
            location = '\\Music\\'
            text3 = str(userid) + str(username) + str(location)
            finalfilecreate(text1,text2,text3)
                            
        elif text3s in ("5","five","pictures","Pictures","number five"):
            location = '\\Pictures\\'
            text3 = str(userid) + str(username) + str(location)
            finalfilecreate(text1,text2,text3)
                
        elif text3s in ("6","six","videos","Videos","number six"):
            location = '\\Videos\\'
            text3 = str(userid) + str(username) + str(location)
            finalfilecreate(text1,text2,text3)
        
        elif text3s in ("exit"):
            exitfilecreate()
        
        else:
            print("Invalid")
            createnewfile()
            
                
    def finalfilecreate(text1,text2,text3): 
        totalfile = str(text3) + str(text1)
        if os.path.exists(totalfile):
            print("This file exists! \nRestarting!")
            createnewfile()
        
        elif not os.path.exists(totalfile):
            print(str(totalfile)+" file has been created") 
            f = open((str(totalfile)+'.txt'), "w+")   
            f.write(str(text2))
            f.close
        
    def exitfilecreate():
        print('Do you want to exit? Yes/No: ')
        exitfilevoice = audiostart()
        if exitfilevoice in ("yes","Yes"):
            ayumimenu()
        elif exitfilevoice in ("no","No"):
            createnewfile()
        else:
            exitfilecreate()
    
    ########Folder########
    
    def createnewfolder(): #asks for the name of file
        # obtain audio from the microphone
        print("Name of folder: ")
        text1 = audiostart()
        print("Answer: ", text1)
        if text1 in ("exit","cancel"):
            exitfoldercreate()
        else:
            createfolderlocation(text1)
                
            
    def createfolderlocation(text1): #asks for the location of file
        # obtain audio from the microphone
        print("""Location of folder: \n1. Desktop \n2. Documents \n3. Downloads \n4. Music \n5. Pictures \n6. Videos \n7. C-drive""")
        text3s = audiostart()
        print("Answer: ",text3s)
        
        if text3s in ("1","one","desktop","Desktop","number one"):
            location = '\\Desktop\\'
            text3 = str(userid) + str(username) + str(location)
            finalfoldercreate(text1,text3)
            
        elif text3s in ("2","two","documents","Documents","number two"):
            location = '\\Documents\\'
            text3 = str(userid) + str(username) + str(location)
            finalfoldercreate(text1,text3)
            
        elif text3s in ("3","three","downloads","Downloads","number three", "download"):
            location = '\\Downloads\\'
            text3 = str(userid) + str(username) + str(location)
            finalfoldercreate(text1,text3)
                            
        elif text3s in ("4","four","music","Music","number four"):
            location = '\\Music\\'
            text3 = str(userid) + str(username) + str(location)
            finalfoldercreate(text1,text3)
                            
        elif text3s in ("5","five","pictures","Pictures","number five"):
            location = '\\Pictures\\'
            text3 = str(userid) + str(username) + str(location)
            finalfoldercreate(text1,text3)
                
        elif text3s in ("6","six","videos","Videos","number six"):
            location = '\\Videos\\'
            text3 = str(userid) + str(username) + str(location)
            finalfoldercreate(text1,text3)
            
        elif text3s in ("7","seven","see drive","drive","number seven"):
            text3 = cdrive
            finalfoldercreate(text1,text3)
                                
        elif text3s in ("exit"):
            exitfoldercreate()

        else:
            print("Invalid")
            createnewfolder()     
        
                
    def finalfoldercreate(text1,text3):
        totalfolder = str(text3) + str(text1)
        if os.path.exists(totalfolder):
            print(str(totalfolder)+" Folder exist!")
            exitfoldercreate()
            
        elif not os.path.exists(totalfolder):
            os.makedirs(totalfolder, mode=0o777, exist_ok=False)
            print(str(totalfolder)+" folder has been created") 
            exitfoldercreate()
            
        else:
            print("Invalid!")
            exitfoldercreate()

    def exitfoldercreate():
        print("exiting...")
        ayumimenu()


    createtextfile = "create text file"
    if (bool(re.findall(createtextfile, text))):
        createnewfile()
        
    createtextfile = "create folder"
    if (bool(re.findall(createtextfile, text))):
        createnewfolder()
    
    #word
    #powerpoint
    #excel
    #.bat
    #python

    ############################################################################################################
    #                                         Calculator
    division = "\\/|divided by|divide|divided"
    mulltiplication = "\\*|time|times"
    addition = "\\+|add|addition"
    subtraction = "\\-|subtract|minus|remove"
    exponent = "\\^|power|power of"
    clear = "clear"
    goback = "exit","leave"

    totaloperator = str(division )+ str("|") + str(exponent)+ str("|") +  str(subtraction)+ str("|") + str(mulltiplication) + str("|") + str(addition)

    def audiocalulator(): 
        reg = sr.Recognizer()
        with sr.Microphone() as source:
            audio = reg.listen(source)
            try:
                input1 = reg.recognize_google(audio)
                return input1     
                
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print("error; {0}".format(e))


    def maincalulator(x,y):
        try:
            if (re.findall(addition, text)):
                z = float(y[0]) + float(y[1])     
                return z
                
            elif (re.findall(subtraction, text)):
                z = float(y[0]) - float(input2[1])
                return z
                
            elif (re.findall(mulltiplication, text)):
                z = float(y[0]) * float(input2[1])
                return z
                
            elif (re.findall(division, text)):
                z = float(y[0]) / float(input2[1])   
                return z
                
            elif (re.findall(division, text)):
                z = float(y[0]) / float(input2[1])
                return z
                
            elif (re.findall(exponent, text)):
                z = float(y[0]) ** float(input2[1])
                return z
            
            else:
                print("Error!")
                calculator1()
                
        except ValueError:
            print("Invalid")
            calculator1()


    def calculator1():
        print("Calulcator: ")
        input1 = audiocalulator() #speech to text
        if input1 in goback: #checks if the input is under goback
            ayumimenu()
        print(input1)
        input2 = (re.findall('\\d+', input1)) #ouputs only digits
        calanswer = maincalulator(input1, input2)
        calculator2(calanswer)
        

    def calculator2(x):
        print(x)
        input1 = audiocalulator() #speech to text
        if input1 in goback: #checks if the input is under goback
            ayumimenu()
        print(input1)
        input2 = (re.findall('\\d+', input1))

        try:
            if (re.findall(addition, input1)):
                y = float(x) + float(input2[0])     
                calculator2(y)
                
            elif (re.findall(subtraction, input1)):
                y = float(x) - float(input2[0])
                calculator2(y)
                
            elif (re.findall(mulltiplication, input1)):
                y = float(x) * float(input2[0])
                calculator2(y)
                
            elif (re.findall(division, input1)):
                y = float(x) / float(input2[0])
                calculator2(y)   
                
            elif (re.findall(division, input1)):
                y = float(x) / float(input2[0])
                calculator2(y)
                
            elif (re.findall(exponent, input1)):
                y = float(x) ** float(input2[0])
                calculator2(y)
                
            elif input1 or input2 in clear:
                print("Cleared!")
                calculator1()
            else:
                print("Error!")
                calculator1()
                
        except ValueError:
            print("Invalid")
            calculator1()


    calculatorsummon = "calculator|mathematics|maths"
    if (bool(re.findall(calculatorsummon, text))):
        calculator1() 
        
    if (bool(re.findall(totaloperator, text))):
        input2 = (re.findall('\\d+', text))
        print("Answer: ",maincalulator(text,input2)) 
        ayumimenu()      

    ############################################################################################################
    #                                       Open Applications
    desktopdir = str(userid) + str(user) + "\\Desktop\\"

    def lnkfind():
        x = (glob.glob(str(desktopdir) + "*.lnk"))
        return x
        
    def lnkfind2():
        x = (glob.glob("C:\\Users\\Public\\Desktop\\*.lnk"))
        return x

    def urlfind():
        x = (glob.glob(str(desktopdir) + "*.url"))
        return x
                
    def apprefmsfind():     
        x = (glob.glob(str(desktopdir) + "*.appref-ms"))
        return x

    shortcut = (str(urlfind()) + str(lnkfind()) + str(lnkfind2()) + str(apprefmsfind()))
    short1 = shortcut.lower()

    def shortcutopen(requestlower):
        if bool(re.findall(str(requestlower), str(short1))):
            lnkfindlower1 = str(lnkfind())
            lnkfindlower2 = lnkfindlower1.lower()
            
            lnkfind2lower1 = str(lnkfind2())
            lnkfind2lower2 = lnkfind2lower1.lower()
            
            urlfindlower1 = str(urlfind)
            urlfindlower2 = urlfindlower1.lower()
            
            try:
                if bool(re.findall(str(requestlower), str(lnkfindlower2))):
                    print("opening",requestlower)
                    os.system(str(desktopdir) + str(requestlower) + ".lnk")
                    ayumimenu()
                    
                elif bool(re.findall(str(requestlower), str(lnkfind2lower2))):
                    print("opening",requestlower)
                    subprocess.Popen(("C:\\Users\\Public\\Desktop\\" + str(requestlower) + ".lnk"), shell=True)
                    ayumimenu()
                    
                elif bool(re.findall(str(requestlower), str(urlfindlower2))):
                    print("opening",requestlower)
                    os.system(str(desktopdir) + str(requestlower) + ".url")
                    ayumimenu()
            except:
                print("Error!")
                ayumimenu()
                
    applicationtrigger = "launch"
    if (bool(re.findall(applicationtrigger, text))):
        requestfind = (re.findall('(?<=launch\\s).+',text))
        request = requestfind[0]
        requestlower = request.lower()
        shortcutopen(requestlower)
 
    ############################################################################################################
    #                                       Windows Function
   
    convo1 = "i love you"
    if (bool(re.findall(convo1, text))):
        print("i don't love you!")
        ayumimenu() 

    convo2 = "how are you"
    if (bool(re.findall(convo2, text))):
        HRU = "I am well", "I am doing good!", "i am Fine"
        print(random.choice(HRU))
        ayumimenu() 

    convo3 = "i am lonely"
    if (bool(re.findall(convo3, text))):
        HRU = "you an always talk to me"
        print(random.choice(HRU))
        ayumimenu() 

 
    else: 
        print("Ayumi: Sorry There is no function for: ",text)
        ayumimenu()

    

    
r = sr.Recognizer()
r.listen_in_background(sr.Microphone(), wakeup)
while True: time.sleep(0.1) 
    
