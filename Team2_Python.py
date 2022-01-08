#!/usr/bin/env python
# coding: utf-8

# In[7]:


getWord = input("Player 1 - Please enter in a word: ")
getGuesses = input ("Player 1 - Please enter a number of guesses: ")
while getGuesses.isnumeric() == False:
        getGuesses = input ("Player 1 - Please enter a number of guesses: ")
        
wordUnderscore = ""
theActualString = list(getWord)
index1 = 0
for letter in getWord:
    wordUnderscore = wordUnderscore + "_ "
    theActualString[index1] = "_"
    index1 = index1 + 1
print("WORD: " + wordUnderscore)

guessesLeft = int(getGuesses)
print("GUESSES LEFT: " + str(guessesLeft) + "\n")


updatedWord = wordUnderscore

#Player 2
while guessesLeft > 0 and  "_" in theActualString:     
    letterGuess = input("Player 2 - Please guess a letter: ")
    if letterGuess.lower() == getWord.lower():
        break
    elif letterGuess.isalpha() and letterGuess.lower() not in theActualString:
        updatedWord = ""
        index = 0
        letterPresent = "False"
        for letter in getWord:
            if letterGuess.upper() == letter.upper():
                theActualString[index] = letterGuess.lower()
                print("Correct.")
                letterPresent = "True"
                updatedWord = updatedWord + theActualString[index] + " "
            else:
                updatedWord = updatedWord + theActualString[index] + " "
            index = index + 1
        if letterPresent == "False":
            print("Incorrect. Letter is not in the word")
            guessesLeft= guessesLeft - 1
    else:
        print("Invalid input.")
    print("WORD: " + updatedWord)
    print("GUESSES LEFT: " + str(guessesLeft) + "\n")

if guessesLeft == 0:
    print("Player 2 You Lose!")
else:
    print("Player 2 You Win!")

#print("You Lose")


# In[ ]:





# In[ ]:




