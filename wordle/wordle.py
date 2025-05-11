import random
FILE_PATH = "C:/Users/highs/OneDrive/Desktop/dev_projects/wordlist.txt"


def getWord(filename):
    try:
        with open(filename, "r") as file:
            words = file.read().splitlines()
            word = random.choice(words)
            return word
        
    except:
        print("File was not found")


def compareWord(word, guess):
    result = ['X'] * 5

    if word == guess:
        return "!!!!!"
       

    for i in range(0, len(word)):
        if guess[i] == word[i]:
            result[i] = '!'
    
    for i in range(0, len(word)):
        if guess[i] in word and result[i] != '!':
            result[i] = '*'
    res = ''.join(result)   
    return res

        
def main():
   
    guesses = 0
    MAX_GUESSES = 5
    
    getWord(FILE_PATH)
    word = getWord(FILE_PATH).upper()

    var = 0
    for i in range(guesses, MAX_GUESSES):
    
        print("******************************")
        print(f"You have {5 - i} guesses remaining")
        print("------------------------------")
        
        while True:
            print("GUESS A 5 LETTER WORD")
            print("------------------------------")
           
            guess = input().upper()
            print()

            if(len(guess) == 5 and guess.isalpha()):
                break
            else:
                print("Enter a valid 5 letter word")
                print("------------------------------")
        

        print(compareWord(word, guess))
        
        if compareWord(word, guess) == '!!!!!':
            print(f"You guessed correctly! The word was {word}")
            break
        
        
        print()
        var += 1
        if var >= MAX_GUESSES:
            print(f"You lost! The word was {word}")
    


if __name__ == "__main__":
    main()