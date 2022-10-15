import random
from replit import clear
from hangman_words import word_list
from hangman_art import logo,stages

# chosing a random word from the list
chosen_word=random.choice(word_list)

# printing welcome logo
print(logo)

#Displaying the dashes
display=[]
for letter in chosen_word:
  display+="_"
print(f"{' '.join(display)}")

#checking if the guess matches the word
#lives
lives=6
flag=False

while lives>0 and flag==False:

  #Guessing a letter
  guess=input("Guess a letter: ").lower()
  
  #clearing the screen each time
  clear()

  # To see if the letter is already guessed
  if guess in display:
    print(f"You have already guessed {guess}")
  
  # swapping the dash with guess if guess matches
  for i in range(0,len(chosen_word)):
    if chosen_word[i]==guess:
      display[i]=guess
  print(f"{' '.join(display)}")
  
  # if guess not in word draw hangman
  if guess not in chosen_word:
    lives-=1
    print(f"You guessed {guess}, that is not in the word.You lose a life.")
    if lives==0:
      print("YOU LOSE")

  #if every dash has been guessed correctly
  if "_"not in display:
    print("YOU WIN")
    flag=True
  
  print(stages[lives])
  

    
  
   
  
    
