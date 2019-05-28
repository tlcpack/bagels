import random
import time

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)

def isOnlyDigits(num):
    if num =='':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    
    return True

print(f"I am thinking of a {NUM_DIGITS}-digit number. Try and guess what it is.")
time.sleep(2)
print("The clues I give are...")
time.sleep(2)
print("When I say:     That means:")
print('  Bagels        None of the digits are correct')
print('  Pico          One digit is correct but in the wrong position.')
print('  Fermi         One digit is correct and in the right position.')

while True:
    secretNum = getSecretNum()
    print(f"I have thought of a number. You have {MAX_GUESS} guesses to get it.")

    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print(f"Guess #{guessesTaken}: ")
            guess = input()

        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print(f"You ran out of guesses. The answer was {secretNum}.")
        
    print("Do you want to play again? (yes or no)")
    if not input().lower().startswith('y'):
        break
