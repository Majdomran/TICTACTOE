bräda = [' ' for x in range(10)]

def sättInBokstav(bokstav, pos):
    bräda[pos] = bokstav

def platsÄrLedig(pos):
    return bräda[pos] == ' '

def skrivUtBräda(bräda):
    print('   |   |   ')
    print(' ' + bräda[1] + ' | ' + bräda[2] + ' | ' + bräda[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + bräda[4] + ' | ' + bräda[5] + ' | ' + bräda[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + bräda[7] + ' | ' + bräda[8] + ' | ' + bräda[9])
    print('   |   |   ')

def ärBrädanFull(bräda):
    if bräda.count(' ') > 1:
        return False
    else:
        return True

def ärVinnare(spelplan, symbol):
    vinnande_kombinationer = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  
        [1, 5, 9], [3, 5, 7]              
    ]

def spelarDrag():
    fortsätt = True
    while fortsätt:
        drag = input("Vänligen välj en position att placera X mellan 1 och 9\n")
        try:
            drag = int(drag)
            if drag > 0 and drag < 10:
                if platsÄrLedig(drag):
                    fortsätt = False
                    sättInBokstav('X' , drag)
                else:
                    print('Tyvärr, denna plats är upptagen')
            else:
                print('Vänligen skriv ett nummer mellan 1 och 9')

        except:
            print('Vänligen skriv ett nummer')

def datorDrag():
    möjligaDrag = [x for x , bokstav in enumerate(bräda) if bokstav == ' ' and x != 0  ]
    drag = 0

    for bokstav in ['O' , 'X']:
        for i in möjligaDrag:
            kopiaAvBräda = bräda[:]
            kopiaAvBräda[i] = bokstav
            if ärVinnare(kopiaAvBräda, bokstav):
                drag = i
                return drag

    öppnaHörn = []
    for i in möjligaDrag:
        if i in [1 , 3 , 7 , 9]:
            öppnaHörn.append(i)

    if len(öppnaHörn) > 0:
        drag = slumpmässigtVal(öppnaHörn)
        return drag

    if 5 in möjligaDrag:
        drag = 5
        return drag

    öppnaKanter = []
    for i in möjligaDrag:
        if i in [2,4,6,8]:
            öppnaKanter.append(i)

    if len(öppnaKanter) > 0:
        drag = slumpmässigtVal(öppnaKanter)
        return drag

def slumpmässigtVal(lista):
    import random
    ln = len(lista)
    r = random.randrange(0,ln)
    return lista[r]

def huvud():
    print("Välkommen till spelet!")
    skrivUtBräda(bräda)

    while not(ärBrädanFull(bräda)):
        if not(ärVinnare(bräda , 'O')):
            spelarDrag()
            skrivUtBräda(bräda)
        else:
            print("Tyvärr, du förlorar!")
            break

        if not(ärVinnare(bräda , 'X')):
            drag = datorDrag()
            if drag == 0:
                print(" ")
            else:
                sättInBokstav('O' , drag)
                print('Datorn placerade en O på position' , drag , ':')
                skrivUtBräda(bräda)
        else:
            print("Grattis, du vinner!")
            break

    if ärBrädanFull(bräda):
        print("Oavgjort")

while True:
    x = input("Vill du spela? Tryck y för ja eller n för nej (y/n)\n")
    if x.lower() == 'y':
        bräda = [' ' for x in range(10)]
        print('--------------------')
        huvud()
    else:
        break
