#Hofhard -program automatyzujący denerwujące funkcje programu Inter Team Katalog

import pyperclip, time, pyautogui, sys, re, os, datetime, smtplib
pyautogui.PAUSE = 0.1




def mapujHofsoft():
    hofsoftTopLeft=pyautogui.locateOnScreen('hofsoftwin.png')
    hofsoftWorkspaceTopLeft=(hofsoftTopLeft[0], hofsoftTopLeft[1]+37)
    #hofsoftWorkspaceBottomRight=(pyautogui.locateOnScreen('hosfsoftbottomright.png')[0] + pyautogui.locateOnScreen('hosfsoftbottomright.png')[2], pyautogui.locateOnScreen('hosfsoftbottomright.png')[1] + pyautogui.locateOnScreen('hosfsoftbottomright.png')[3])
    hofsoftWorkspaceBottomRight=((hofsoftWorkspaceTopLeft[0]+1114),(hofsoftWorkspaceTopLeft[1]+854))
    return (hofsoftWorkspaceTopLeft,hofsoftWorkspaceBottomRight)

def getIntegra():
    integraIcon=pyautogui.locateOnScreen('integra.png')
    time.sleep(1)
    #print("Ikona integry: " + str(integraIcon))
    pyautogui.click(integraIcon[0], integraIcon[1])
    


def getHofsoft():
    hofsoftIcon=pyautogui.locateOnScreen('hofsoft.png')
    time.sleep(1)
    pyautogui.click(hofsoftIcon[0], hofsoftIcon[1])
    time.sleep(0.5)
    #print("Ikona hofsoftu: " + str(hofsoftIcon) + "\nOkno hofsoftu: " + str(hofsoftWindow))



def posIntegra():
    integraWindow=pyautogui.locateOnScreen('integrawin.png')
    return integraWindow
    
def posHofsoft():
    hofsoftWindow=pyautogui.locateOnScreen('hofsoftwin.png')
    return hofsoftWindow

def zrzutHofsoft():

    mapa=mapujHofsoft()
    pyautogui.moveTo(mapa[0][0], mapa[0][1])
    time.sleep(0.1)
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.dragTo(mapa[1][0], mapa[1][1], duration=0.2)
    time.sleep(0.1)
    pyautogui.mouseUp()
    return pyperclip.paste()
def powrotMenuHofsoft():
    koniecRegex=re.compile(r'(zy kończysz pracę w systemie ?)')
    mo=koniecRegex.search(zrzutHofsoft())
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(0.5)
    pyautogui.press('esc')
    time.sleep(0.5)
    pyautogui.press('esc')
    time.sleep(0.5)
    pyautogui.press('esc')
    time.sleep(0.5)


    
    while mo==None:
        pyautogui.press('esc')
        time.sleep(0.5)
        mo=mo=koniecRegex.search(zrzutHofsoft())
    else:
        pyautogui.press('esc')
        #print(10*'#')
        #print('Powrocono do menu glownego')
        #print(10*'#')
        #bla=input()

print("""Co chcesz zrobić?
[1] Skanuj towar
[2] Korekta sprzedaży
[3] [TEST] Pobierz rozchod wewnetrzny do slownika

"""
      , flush=True)

wybor=int(input())

if wybor==1:
    
    print("Zeskanuj kod: " , end='', flush=True)
    kod=input()
    if len(kod)>3:
        kod.strip(" ♪ ")
        kod.strip(' ')
        kod2="$$$"+kod+"%%%"
        pyperclip.copy(kod)
        getHofsoft()
        time.sleep(0.5)
        pyautogui.typewrite(kod2, 0.025)
    else:
        print("Błąd")
        sys.exit()
        
elif wybor==2:

    print("[1] Zeskanuj kod i wciśnij [ENTER]", flush=True)
    kod=input()
    a=0.5
    kod.strip(" ♪ ")
    kod.strip(' ')
    kod2="$$$"+kod+"%%%"
    getHofsoft()
    powrotMenuHofsoft()
    pyautogui.typewrite("31", 0.25)
    time.sleep(2)
    pyautogui.typewrite(kod2, 0.025)
    time.sleep(2)
    pyautogui.hotkey('shiftleft', 'f10')
    pyautogui.hotkey('shiftleft', 'f10')
    time.sleep(1)
    pyautogui.hotkey('shiftleft', 'f10')
    pyautogui.hotkey('shiftleft', 'f10')
    time.sleep(1)
    pyautogui.typewrite('01012015')
    time.sleep(0.5)
    pyautogui.keyDown('enter')
    time.sleep(0.1)
    pyautogui.keyUp('enter')
    time.sleep(0.1)
    pyautogui.keyDown('enter')
    time.sleep(0.1)
    pyautogui.keyUp('enter')
    time.sleep(0.1)
    pyautogui.keyDown('altleft')
    time.sleep(0.1)
    pyautogui.keyDown('tab')
    time.sleep(0.1)
    pyautogui.keyUp('altleft')
    time.sleep(0.1)
    pyautogui.keyUp('tab')
    time.sleep(0.1)
    print("wprowadz numer dokumentu")
    numerd=input()
    print("podaj typ dokumentu")
    typ=input()

            #powrot do menu
    getHofsoft()
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(0.3)
    pyautogui.press('esc')
    time.sleep(0.3)
    pyautogui.press('esc')
    time.sleep(0.3)
    pyautogui.press('esc')
    time.sleep(0.3)
              #do korekty
    pyautogui.typewrite('841', 0.25)
    time.sleep(0.3)
    pyautogui.press('insert')
    pyautogui.press('insert')
    pyautogui.press('insert')
    time.sleep(0.3)
    pyautogui.press('insert')
    time.sleep(0.3)
    pyautogui.typewrite(typ, 0.25)
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.typewrite(numerd, 0.25)
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.press('enter')

elif wybor==3:
    getHofsoft()
    powrotMenuHofsoft()
    pyautogui.typewrite('8f', 0.25)
    print('>Podświetl< RW do zaciągnięcia do lokalnej bazy danych programu, wroc do tej aplikacji i wcisnij [ENTER]')
    bla=input()
    getHofsoft()
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('pgdn', presses=10, interval=0.1)
    pyautogui.press('pgup', presses=5, interval=0.1)
    #ZRZUT EKRANU
    zrzut=zrzutHofsoft()
    regexNazwyZlecenia=re.compile(r'(Uzasadnienie: )(.{60})')
    regexRozchodu=re.compile(r'(\w{8})(\s{15})(.*?)(\s{3})(\s*?)(\d{1,4})(\s{12})')
    jmstanminzero=re.compile(r'J\.m\.                                   Stan min\.:     0   Op\.:     0')
    zrzutList=regexRozchodu.findall(zrzut)
    nazwaZlecenia=regexNazwyZlecenia.search(zrzut).group(2).replace(r"/", r"__").strip(" ")
    print(nazwaZlecenia.center(30, "*"))
    dt=datetime.datetime.now()
    data=str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day) + "__" + str(dt.hour) + "-" + str(dt.minute)
    plikTestowy=open(str(nazwaZlecenia)+"_"+str(data)+"_PLIK_POROWNAWCZY.txt", 'a')
    plikZlecenia=open(str(nazwaZlecenia)+".csv", 'w')
    #plikZlecenia.write("""Symbol magazynu;Numer Katalogowy towaru;Nazwa towaru;Ilość;Jm;Cena Zakupu Netto;CenaSprzedarzyNetto;Stawka Vat;PKWiU;Indeks;Grupa główna towaru;Podgrupa 1 towaru;Podgrupa 2 towaru;Opis towaru;Uwagi;Dostawca;Producent\n\n""")
    plikZlecenia.write("\n")
    
    rozchodTemp={}
    while jmstanminzero.search(zrzut)==None:
        zrzut=zrzutHofsoft()
        zrzutList=regexRozchodu.findall(zrzut)
        for i in range(len(zrzutList)):
            if str(zrzutList[i][0]) in rozchodTemp.keys():
                pass
            else:       
                rozchodTemp[str(zrzutList[i][0])]={}
                rozchodTemp[str(zrzutList[i][0])]['numerKat']=str(zrzutList[i][0])
                rozchodTemp[str(zrzutList[i][0])]['nazwa']=str(zrzutList[i][2])
                rozchodTemp[str(zrzutList[i][0])]['ilosc']=str(zrzutList[i][5])


    powrotMenuHofsoft()
    pyautogui.typewrite("31", 0.25)
    time.sleep(1)
    
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('f6')
    time.sleep(0.3)
    pyautogui.press('home')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.press('f7')
    time.sleep(0.3)
    pyautogui.press('home')
    time.sleep(0.3)
    pyautogui.press('down', presses=2, interval= 0.2)
    time.sleep(0.3)
    
    
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.typewrite('2')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(2)
    zrzutVat=zrzutHofsoft()
    regexVat=re.compile(r'(\+VAT           Numer katalogu)')
    if regexVat.search(zrzutVat)==None:
        time.sleep(0.2)
        pyautogui.press('enter')
    else:
        time.sleep(0.2)
        pyautogui.press('f9')
        time.sleep(0.2)
        pyautogui.press('enter')
    
    for item in rozchodTemp.keys():
        
        time.sleep(0.5)
        pyautogui.typewrite(str(item), 0.2)
        time.sleep(0.5)
        pyautogui.press('enter')
        zrzutCena=zrzutHofsoft()
        regexTextCena="(│─────────────────────────────────────────────────────────────────────────────│░\n│ )(\w{8})(.*)(\d{1,8}\.\d\d)(.*)( │░)"
        regexRozchodu=re.compile('(\w{8})(\s{15})(.*?)(\s{3})(\s*?)(\d{1,4})(\s{12})')
        #regexCena=re.compile(r"(│─────────────────────────────────────────────────────────────────────────────│░\r\n│ )(\w{8})(.*)(\s\d{1,8}\.\d\d)(.*)( │░)")
        regexCena=re.compile(r"(│─────────────────────────────────────────────────────────────────────────────│░\r\n│ )(\w{8})(.*)(\s\d{0,},?\d{1,8}\.\d\d)(.*)( │░)")
        regexNumerProducenta=re.compile(r"(.{0,2}-.{0,2}-.{0,2}-.{0,2}\s{1,})(.{25})")
        if str(item)==str(regexCena.search(zrzutCena).group(2)):
            rozchodTemp[item]['cena']=regexCena.search(zrzutCena).group(4)
            print("Znaleziono towar : " + str(item) + " (Sprawdzenie: " + str(regexCena.search(zrzutCena).group(2)) +")")
            plikTestowy.write("Znaleziono towar : " + str(item) + " (Sprawdzenie: " + str(regexCena.search(zrzutCena).group(2)) +")\n")
            rozchodTemp[item]['numerProducenta']=regexNumerProducenta.search(zrzutCena).group(2)
            
        else:
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.typewrite(str(item), 0.2)
            time.sleep(0.5)
            pyautogui.press('enter')
            zrzutCena=zrzutHofsoft()
            regexTextCena="(│─────────────────────────────────────────────────────────────────────────────│░\n│ )(\w{8})(.*)(\d{1,8}\.\d\d)(.*)( │░)"
            regexRozchodu=re.compile('(\w{8})(\s{15})(.*?)(\s{3})(\s*?)(\d{1,4})(\s{12})')
            #regexCena=re.compile(r"(│─────────────────────────────────────────────────────────────────────────────│░\r\n│ )(\w{8})(.*)(\s\d{1,8}\.\d\d)(.*)( │░)")
            regexCena=re.compile(r"(│─────────────────────────────────────────────────────────────────────────────│░\r\n│ )(\w{8})(.*)(\s\d{0,},?\d{1,8}\.\d\d)(.*)( │░)")
            rozchodTemp[item]['cena']=regexCena.search(zrzutCena).group(4)
            rozchodTemp[item]['numerProducenta']=regexNumerProducenta.search(zrzutCena).group(2).strip(' ')
            print("Znaleziono towar : " + str(item) + " (Sprawdzenie: " + str(regexCena.search(zrzutCena).group(2)) +") <---Poprawiono?")
            plikTestowy.write("Znaleziono towar : " + str(item) + " (Sprawdzenie: " + str(regexCena.search(zrzutCena).group(2)) +") <---Poprawiono?")
    lewa=50
    prawa=50
    for czesc in rozchodTemp.keys():
        print()
        plikTestowy.write("\nNumer katalogowy czesci: ".ljust(lewa, ',') + str(rozchodTemp[czesc]['numerKat']).rjust(prawa) + "\nNazwa czesci w systemie Hofsoft: ".ljust(lewa, '.') + str(rozchodTemp[czesc]['nazwa']).rjust(prawa) + "\nIlosc: ".ljust(lewa, '.') + str(rozchodTemp[czesc]['ilosc']).rjust(prawa) + "\nCENA: ".ljust(lewa, '.') + str(rozchodTemp[czesc]['cena']).rjust(prawa) + "\nNumer producenta: ".ljust(lewa, '.') + str(rozchodTemp[czesc]['numerProducenta']).strip(' ').rjust(prawa) +"\n\n")
        #plikZlecenia.write("""Symbol magazynu;Numer Katalogowy towaru;Nazwa towaru;Ilość;Jm;Cena Zakupu Netto;CenaSprzedarzyNetto;Stawka Vat;PKWiU;Indeks;Grupa główna towaru;Podgrupa 1 towaru;Podgrupa 2 towaru;Opis towaru;Uwagi;Dostawca;Producent\n""")
        plikZlecenia.write("""MG;"""+str(rozchodTemp[czesc]['numerProducenta']).strip(' ')+""";"""+str(rozchodTemp[czesc]['nazwa'])+""";"""+str(rozchodTemp[czesc]['ilosc'])+""";szt.;"""+str(rozchodTemp[czesc]['cena']).replace(".", ",").strip(' ')+""";""" +str(round((1.23)*(float(rozchodTemp[czesc]['cena'])), 2)).replace(".", ",") + """;23;0; ; ; ; ;Inter Team;Zaimportowano z użyciem programu HofHard: """ +str(data)+"""; ;\n""")
    #dodanie cen do dokumentu





        time.sleep(0.3)
    pyautogui.press('f7')
    time.sleep(0.3)
    time.sleep(0.3)
    pyautogui.press('home')
    time.sleep(0.3)
    pyautogui.press('down', presses=2, interval= 0.2)
    time.sleep(0.3)
    
    
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.typewrite('1')
    
    
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('f9')
    time.sleep(0.5)
    





    
    plikTestowy.write(2*"\n" +60*"*" + "\n"+60*"*"+"\n")
    
    plikZlecenia.close()
    plikTestowy.close()

    print("czy wyslac Email? \n\n [t]=wyslij\n[n] lub cokolwiek innego = nie wysylaj")
    bla=input()
    if bla.lower()=="t":
        TESTMAIL=open(str(nazwaZlecenia)+"_"+str(data)+"_PLIK_POROWNAWCZY.txt", 'r')
        trescMaila=TESTMAIL.read()
        obiektPoczty=smtplib.SMTP('smtp.gmail.com', 587)
        obiektPoczty.ehlo()
        obiektPoczty.starttls()
        trescGotowa=str('Subject: ' + nazwaZlecenia + '\n' + trescMaila)
        trescGotowa=trescGotowa.encode('utf-8', 'ignore')
        obiektPoczty.login('hofhard.bot@gmail.com', 'hofhard12')
        obiektPoczty.sendmail('hofhard.bot@gmail.com', 'marek@czescibrozek.pl', trescGotowa)
        obiektPoczty.sendmail('hofhard.bot@gmail.com', 'brozek@bosch-service.pl', trescGotowa)
        obiektPoczty.quit()
        TESTMAIL.close()
    else:
        pass

    
elif wybor==4:
    getHofsoft()
    koniecRegex=re.compile(r'(zy kończysz pracę w systemie ?)')
    mo=koniecRegex.search(zrzutHofsoft())
    time.sleep(1)
    while mo==None:
        pyautogui.press('esc')
        time.sleep(0.5)
        mo=mo=koniecRegex.search(zrzutHofsoft())
    else:
        pyautogui.press('esc')
        print(10*'#')
        print('Powrocono do menu glownego')
        print(10*'#')
        bla=input()

    
    

else:
    print(">>>KONIEC<<<", flush=True)
    bla=input()
    



