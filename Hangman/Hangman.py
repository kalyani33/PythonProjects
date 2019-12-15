import random
# library that we use in order to choose
# on random words from a list of words

#Lets create a list of colors i.e wordsList
wordsList = ["green", "blue", "white", "yellow", "orange", "black", "red"]
# Function will choose one random
# word from this list of words
secretWord=random.choice(wordsList)

#attempts for user to guess the word
#are length of secret word plus five
chances=5

display=[]
#used contains all the letters in the secret word
#this will be taken away as user guesses each
used=[]

#extend will spit the word into individual letter
#in the list eg: yes become y,e,s
display.extend(secretWord)

#this will copies the list of letters from display into 'used'
#this will enable us to workout if a letter has been used or not
used.extend(display)

#iterate through the list 'display'
for i in range(len(display)):
    #replaces each index with'-'
    display[i]='-'

print(("Let\'s play a game of Hangman. "
       "The word has {} letters in it. \n You get {} guesses.")
      .format(len(secretWord), chances))
print("You have to Guess the color ")

#the join command puts a space in between each '-'
print(" ".join(display))
print()

#counter stops once all the guesses have been guessed
count=0

#keep asking until all the letters guessed
while count<len(secretWord) and chances>0:
    #print("Your guessed letters:",display)
    guess=input("guess the letter of a color: ")
    guess.lower()
        #print(count)
    #iterates through the letters in secrectWord
    for i in range(len(secretWord)):
        #if guessed letter matches a letter
        #in the 'secretWord'
        if guess==secretWord[i] and guess in used:
            #replace the index of that guess with
            #the actuall letter they guessed
            display[i]=guess
            count+=1
            #print(used)
            used.remove(guess)
    if guess not in display:
        chances-=1
        print("sorry..! it's a wrong guess,you have",chances,"chances left")
    print("you have guessed: ",count,"correct letters.")
    print("you have: ",chances,"chances left")

    #print out the new string with guessed letters in
    print(" ".join(display))
    print()


if count==len(secretWord):
#once count is greater than length of word then
    print("Well done!! you guessed the word")
    print("YAY!  Thanks for playing!!")
else:
    print("oh sorry !! you ran out of goes")










