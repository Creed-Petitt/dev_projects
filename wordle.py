import random
FILE_PATH = "C:/Users/highs/OneDrive/Desktop/dev_projects/wordlist.txt"


def getWord(filename):
    try:
        with open(filename, "r") as file:
            words = file.read().splitlines()
            word = random.choice(words)
            print(word)
        
    except:
        print("File was not found")


def compareWord(word, guess):
    pass

def main():
    getWord(FILE_PATH)



if __name__ == "__main__":
    main()