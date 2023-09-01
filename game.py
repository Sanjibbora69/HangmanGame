#Hangman Gam
import hangman_art
print(hangman_art.logo)#we can also do import of logo this way "from hangman_art import logo" #to import the logo from hangmant_art module
import hangmanwords                             #to import the word list from the module saves as hangmanwords
import random
chosen_word=random.choice(hangmanwords.word_list)#randomly selecting word from the imported word_list from module hangmanword
#print(chosen_word)                             #printing the chosen word
display=[]                                      #Empty list has been createdtt
for each_letter in chosen_word:                 #here we are checking for each letter in chosen word so that we can create the required blank space to display for the user on the screen
    display+="_"                                #every time the letter is checked "_" is added
life=6                                          #variable life is created to keep the track of the life left, live is set to 6
end_of_game=False                               #setting condition which will help to come out of while loop
while not end_of_game:
    blank_dash=print(f'{" ".join(display)}')    #this is to display blank_dash requried & way to join all the elements in the list and convert them into string
    guess=input("Guess a letter: ").lower()     #asking the user to guess a letter and coverting it in lower case 
    if guess in display:                        #this is the condition for same letter already guessed by the user
        print(f"You have already guessed the letter {guess}, please guess different letter") #if guessed letter is already guessed this will be printed
    for position in range(len(chosen_word)):    #here will check for the position of letters in chosen_word one by one
          letter=chosen_word[position]          #here letter is a variable for assign the letter a particular postion
          if letter ==guess:                    #comparison if letter from chosen word is equal to gussed letter
             display[position]=letter           #if matched than display in particula position
    if "_" not in display:                      # when "_" finishes from display we need to come out of while loop
        end_of_game=True                        #coming out of whle loop
        print("You win. ")                      #game won
        print(f'{" ".join(display)}')           #last print the word if guessed correctly
    if guess not in chosen_word:                #if the guess letter is not matched with letter in chosen_word 1 life is lost
        print(f"You guessed the wrong letter, lost a life!! more {life-1} chances left")
        life-=1                                 #lost of a life from total life 6
        print(hangman_art.stages[life])         #every time the user guesses wrong letter life of hangman loses by one and this ascii art get printed sequentially
        if life==0:                             #when life is 0 we will come out of while loop 
            end_of_game=True                    #coming out of while loop
            print("You Lose")                   #game lost
            print(f"The answer was: {chosen_word}")
print("THANK YOU")


