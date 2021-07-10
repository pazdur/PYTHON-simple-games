import random, os

textHangMan = '''
ooooo   ooooo                                                                          
`888'   `888'                                                                          
 888     888   .oooo.   ooo. .oo.    .oooooooo ooo. .oo.  .oo.    .oooo.   ooo. .oo.   
 888ooooo888  `P  )88b  `888P"Y88b  888' `88b  `888P"Y88bP"Y88b  `P  )88b  `888P"Y88b  
 888     888   .oP"888   888   888  888   888   888   888   888   .oP"888   888   888  
 888     888  d8(  888   888   888  `88bod8P'   888   888   888  d8(  888   888   888  
o888o   o888o `Y888""8o o888o o888o `8oooooo.  o888o o888o o888o `Y888""8o o888o o888o 
                                    d"     YD                                          
                                    "Y88888P'                                                                                                                              
        '''

HANGMANPICS = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']


def creationWord(allowCharacters):
    print(textHangMan)
    while True:
        wordIsCorrect = True
        word = input("Enter your word: ")
        for i in word:
            if i not in allowCharacters:
                wordIsCorrect = False
        if wordIsCorrect: break
    return word

def drawText(arrayGuess, life, usedCharacter, *communicat):
    text = ''
    for i in arrayGuess: text += i + ' '
    print(textHangMan)
    print(HANGMANPICS[life])
    print("You have %d/6 life" % (life))
    print("Used character: %s" % (usedCharacter))
    print("Word: %s" % (text))
    if communicat: print(communicat[0])


def guessWord(arrayGuess: list, arrayWord: list, allowCharacters: str, usedCharacters: str, life: int):
    guessLetter = ''
    errorText = ''
    while (len(guessLetter) != 1 or guessLetter not in allowCharacters):

        guessLetter = ''
        guessLetter = input("Enter character: ")

        if guessLetter in usedCharacters:
            errorText = "This character is used!"
            guessLetter = ''
            break
        elif len(guessLetter) != 1:
            errorText = "You must enter only one character!"
            guessLetter = ''
            break
        elif guessLetter not in allowCharacters:
            errorText = "Not allowed character!"
            guessLetter = ''
            break
        elif guessLetter not in arrayWord:
            errorText = "You not guess!"
            usedCharacters += guessLetter + ' '
            guessLetter = ''
            life += 1
            break
        else:
            usedCharacters += guessLetter + ' '
            for i in range(arrayWord.count(guessLetter)):
                findIndexLetter = arrayWord.index(guessLetter)
                arrayGuess[findIndexLetter] = guessLetter
                arrayWord[findIndexLetter] = "_"

    if errorText != '':
        return life, usedCharacters, errorText
    else:
        return life, usedCharacters

def checkWon(arrayWord, life):
    if arrayWord.count("_") == len(arrayWord):
        print("\n\n")
        print("""
oooooo   oooo                                                                   
 `888.   .8'                                                                    
  `888. .8'    .ooooo.  oooo  oooo       oooo oooo    ooo  .ooooo.  ooo. .oo.   
   `888.8'    d88' `88b `888  `888        `88. `88.  .8'  d88' `88b `888P"Y88b  
    `888'     888   888  888   888         `88..]88..8'   888   888  888   888  
     888      888   888  888   888          `888'`888'    888   888  888   888  
    o888o     `Y8bod8P'  `V88V"V8P'          `8'  `8'     `Y8bod8P' o888o o888o 
        """)
        print("\n\n")
        input("Press enter to exit...")
        return False
    elif life == 6:
        print("\n\n")
        print("""
oooooo   oooo                            ooooo                                     
 `888.   .8'                             `888'                                     
  `888. .8'    .ooooo.  oooo  oooo        888          .ooooo.   .oooo.o  .ooooo.  
   `888.8'    d88' `88b `888  `888        888         d88' `88b d88(  "8 d88' `88b 
    `888'     888   888  888   888        888         888   888 `"Y88b.  888ooo888 
     888      888   888  888   888        888       o 888   888 o.  )88b 888    .o 
    o888o     `Y8bod8P'  `V88V"V8P'      o888ooooood8 `Y8bod8P' 8""888P' `Y8bod8P'                                            
            """)
        print("\n\n")
        input("Press enter to exit...")
        return False
    else:
        return True


def game():
    clear = lambda: os.system("cls")
    allowCharacters = 'aąbcćdeęfghijklłmnńoóprsśtuwzźż'
    createWord = creationWord(allowCharacters)
    word = []
    wordGuess = []
    life = 0
    usedCharacter = ''
    error = ''
    result = True

    for i in createWord: word.append(i)
    for i in range(len(word)): wordGuess.append("_")

    clear()

    drawText(wordGuess, life, usedCharacter)

    while result:
        guess = guessWord(wordGuess, word, allowCharacters, usedCharacter, life)
        if(len(guess) == 3):
            life = guess[0]
            usedCharacter = guess[1]
            error = guess[2]
            clear()
            drawText(wordGuess, life, usedCharacter, error)
            result = checkWon(word, life)
        else:
            life = guess[0]
            usedCharacter = guess[1]
            clear()
            drawText(wordGuess, life, usedCharacter)

            result = checkWon(word, life)
game()