import random, os, time

#funkcja odpowiedzialna za czyszczenie konsoli
clear = lambda: os.system("cls")

symbol = ['O', "X"]
players = {}

#Tablica przechowujaca ruchy
game = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# True - koniec gry, ktoś wygrał lub remis, False - nikt nie wygrał
Win = False

#Rysuje plansze
def drawGameBoard(arrayGame):
    print("-------")
    print("|%s|%s|%s|" % (arrayGame[0][0], arrayGame[0][1], arrayGame[0][2]))
    print("-------")
    print("|%s|%s|%s|" % (arrayGame[1][0], arrayGame[1][1], arrayGame[1][2]))
    print("-------")
    print("|%s|%s|%s|" % (arrayGame[2][0], arrayGame[2][1], arrayGame[2][2]))
    print("-------")

#Jeżeli w każdym wierszu nie ma wolnych miejsc a nikt nie wygrał to remis
def checkDraw(arrayGame):
    count = 0
    for i in arrayGame:
        if not ' ' in i:
            count += 1
    if count == 3:
        return True
    else:
        return False

#sprawdza czy ktoś wygrał w poziomie
def horizontallyWin(arrayGame):
    for i in range(len(arrayGame)):
        if len(set(arrayGame[i])) == 1 and arrayGame[i][0] != ' ':
            return True
    return False

#sprawdza czy ktoś wygrał na krzyż
def crossWin(arrayGame):
    if arrayGame[1][1] == ' ':
        return False
    else:
        if arrayGame[0][0] == arrayGame[1][1] == arrayGame[2][2]:
            return True
        elif arrayGame[0][2] == arrayGame[1][1] == arrayGame[2][0]:
            return True

#sprawdza czy ktoś wygrał w pionie
def verticalWin(arrayGame):
    if arrayGame[0][0] == arrayGame[1][0] == arrayGame[2][0] and arrayGame[0][0] != ' ':
        return True
    elif arrayGame[0][1] == arrayGame[1][1] == arrayGame[2][1] and arrayGame[0][1] != ' ':
        return True
    elif arrayGame[0][2] == arrayGame[1][2] == arrayGame[2][2] and arrayGame[0][2] != ' ':
        return True
    else:
        return False

#losuje losowy symbol dla gracza po czym wyrzuca z tablicy wylosowany symbol
def randomSymbol(symbol):
    randomSymbol = random.choice(symbol)
    indexSymbol = symbol.index(randomSymbol)
    return symbol.pop(indexSymbol)

#dodaje gracza do rozgrywki
def addPlayer(player, arrayPlayer, option):
    symbolPlayer = randomSymbol(symbol)
    if player == 'Bot' and option == 2:
        print("Symbol bota to %s \n" % (symbolPlayer))
    else:
        print("Cześć %s twój wylosowany symbol to: %s\n" % (player, symbolPlayer))
    arrayPlayer[player] = symbolPlayer

#funkcja odpowiedzialna za zapisanie ruchu gracza do tablicy
def drawMove(player, arrayPlayer, arrayGame):
    while True:
        cordinate = input("Podaj wspolrzedne x oraz y (x y): ")
        splitCordinate = cordinate.split(' ')
        try:
            x = int(splitCordinate[0])
            y = int(splitCordinate[1])
            if arrayGame[x][y] != ' ':
                print("Bład: To pole jest zajęte!")
                continue
            else:
                arrayGame[x][y] = arrayPlayer[player]
                break
        except:
            print("Program osbsługuje tylko wartości liczbowe i mogą przyjmować one tylko wartośći od 0 do 2")

#funkcja sprawdza czy padła wygrana lub remis
def checkCollision(player, arrayGame, option):
    if horizontallyWin(arrayGame):
        if player == 'Bot' and option == 2:
            print("Przegrałeś z botem!")
        else:
            print("Gracz %s wygrał!" % (player))
        input("Aby zakończyć kliknij klawisz Enter")
        return True
    elif verticalWin(arrayGame):
        if player == 'Bot' and option == 2:
            print("Przegrałeś z botem!")
        else:
            print("Gracz %s wygrał!" % (player))
        input("Aby zakończyć kliknij klawisz Enter")
        return True
    elif crossWin(arrayGame):
        if player == 'Bot' and option == 2:
            print("Przegrałeś z botem!")
        else:
            print("Gracz %s wygrał!" % (player))
        input("Aby zakończyć kliknij klawisz Enter")
        return True
    elif checkDraw(arrayGame):
        print("Remis")
        input("Aby zakończyć kliknij klawisz Enter")
        return True

def bot(arrayGame, arrayPlayer):
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if arrayGame[x][y] == ' ':
            arrayGame[x][y] = arrayPlayer['Bot']
            print("Ruch bota x: %s y: %s" % (x, y))
            break

#
#   Gra w kólko i krzyżyk
#   Opcja 1 - Gra z graczem
#   Opcja 2 - Gra z botem
#
print("-= Witaj w grze kółko i krzyżyk [Tryb konsolowy] =-")
print("Wybierz tryb gry:")
print("1. Graj z drugim graczem")
print("2. Graj z botem")
while True:
    option = input("Wprowadź opcje (1 lub 2): ")

    if option == '1' or option == '2':
        break
    else:
        print("Nie prawidłowa opcja")

option = int(option)
if option == 1:
    name = input("Wprowadź nazwę pierwszego gracza: ")
    addPlayer(name, players, option)

    player_1_Name = name

    while True:
        name = input("Wprowadź nazwę drugiego gracza: ")
        if player_1_Name != name:
            addPlayer(name, players, option)
            break
        else:
            print("Nazwa gracza drugiego musi być inna niż gracza pierwszego")

    playerNameList = list(players.keys())  # lista która przechowuje klucze tablicy
    player1 = playerNameList[0]  # pobranie klucza jako nazwy gracza
    player2 = playerNameList[1]  # pobranie klucza jako nazwy gracza

    drawGameBoard(game)

    # Pętla się wykonuje dopóki ktoś nie wygra Win = true
    while not Win:
        print("\n--= Ruch gracza %s =--" % (player1))
        drawMove(player1, players, game)
        clear()
        drawGameBoard(game)

        Win = checkCollision(player1, game, option)
        if Win:
            continue

        print("\n--= Ruch gracza %s =--" % (player2))
        drawMove(player2, players, game)
        clear()
        drawGameBoard(game)

        Win = checkCollision(player2, game, option)
        if Win:
            continue
else:
    while True:
        name = input("Wprowadź nazwę pierwszego gracza: ")
        if name != "Bot":
            break
        else:
            print("Nazwa 'Bot' jest zarezerwowana!")
    addPlayer(name, players, option)
    addPlayer('Bot', players, option)

    playerNameList = list(players.keys())  # lista która przechowuje klucze tablicy
    player = playerNameList[0]  # pobranie klucza jako nazwy gracza

    drawGameBoard(game)

    while not Win:
        print("\n--= Ruch gracza %s =--" % (player))
        drawMove(player, players, game)
        clear()
        drawGameBoard(game)

        Win = checkCollision(player, game, option)
        if Win:
            continue

        print("\n--= Ruch bota =--")
        time.sleep((0.5))
        bot(game, players)
        time.sleep((1))
        clear()
        drawGameBoard(game)
        Win = checkCollision('Bot', game, option)
        if Win:
            continue





