import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar' \
        ' coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk' \
        ' lion lizard llama mole monkey moose mouse mule newt otter owl panda' \
        ' parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep' \
        ' skunk sloth snake spider stork swan tiger toad trout turkey turtle' \
        ' weasel whale wolf wombat zebra'.split()


def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    break
