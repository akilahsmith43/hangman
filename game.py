import random
import time
import turtle

# creating pen 
pen = turtle.Turtle()

# Defining a method to draw curve 
def curve(): 
	for i in range(200): 
		# Defining step by step curve motion 
		pen.right(1) 
		pen.forward(1) 

# Defining method to draw a full heart 
def heart(): 

	# Set the fill color to pink 
	pen.fillcolor('pink') 

	# Start filling the color 
	pen.begin_fill() 

	# Draw the left line 
	pen.left(140) 
	pen.forward(113) 

	# Draw the left curve 
	curve() 
	pen.left(120) 

	# Draw the right curve 
	curve() 

	# Draw the right line 
	pen.forward(112) 

	# Ending the filling of the color 
	pen.end_fill() 

# Defining method to write text 
def text(): 

	# Move turtle to air 
	pen.up() 

	# Move turtle to a given position 
	pen.setpos(-68, 95) 

	# Move the turtle to the ground 
	pen.down() 

	# Set the text color to black 
	pen.color('black') 

	# Write the specified text in 
	# specified font style and size 
	pen.write("  AYEE YOU WONN", font=( 
	"Times New Roman", 12, "bold"))


# # Draw a heart 
# heart() 

# # Write text 
# text() 

# # To hide turtle 
# pen.ht() 


hangman1 = [
"""
+---+
    |
    |
    |
    ===""", """
+---+
  | |
  O |
    |
    ===""", """
+---+
  | |
  O |
 /| |
    ===""", """
+---+
  | |
  O |
 /|\|
    ===""", """
+---+
  | |
  O |
 /|\|
  | | 
 /  ===""", """
+---+
  | |
  O |
 /|\|
  | | 
 / \ ===""", """
 """]



# list of random things
things = ['pizza', 'cheesecake', 'pasta', 'sushi', 'icecream','tea', 'milk', 'cow', 'horse','cat' ,'antman', 'sandy','becky','Rihanna','LeBron',
          "Mario",'Pitbull','Usher','beyonce','sleep','hangman','dog', "panda","money", "shaq", "durant", "melo", "snowfall", "power", "ghost",'incredibles',
          "elastigirl","frozone", "edna","sully", "mike","Boo","dory","nemo", "akilah", "mater", "McQueen","benjamin","ulta","sephora","franklin", "keisha","simple",
          "careless", "gmu", "hoop", "paris","onika", "microsoft", "apple", "invest", "code", "name", "pepole", "amazon", "shein", "distance", "spongebob", "daily",
          "prince","care", "worse", "package", "insiders", "available", "list","excel", "automate", "analytics", "updates", "words", "outputs", "paper","fire","ruler", "empty",
          "wow", "omg", "lol"]

# selecting a random word from things 
word = random.choice(things).lower()

# creating 2 empty list for correct or wrong t
guessed_right = []
guessed_wrong = []
tries = 6
hangman_count = -1



while tries > 0:
    output = ''
    for letter in word:
        if letter in guessed_right:
            output += letter # will add letter to output if right
        else:
            output += '_ ' # remain the same if incorrect 
    if output == word: # if word is guessed correctly then it ends
        break

    num = len(word)
    print("----------------------------------------------------------")
    print(f"Guess the word: {output} it contains {num} letters")
    print("----------------------------------------------------------")
    print(f'you have {tries} tries remaining')
    print("----------------------------------------------------------")
    response = input("Would you like to guess the full word? (y or n): ")       
    print("----------------------------------------------------------")


    if response.lower() == 'y':
        more = input("Enter the full word\n")
        print("----------------------------------------------------------")
        print("Checking to see if you guessed the whole word correctly...")
        print("----------------------------------------------------------\n")
        time.sleep(3)
        if more == word:
          print("❤--------------------------❤-----------------------------❤")
          print("WOW you did IT\nYou guessed the whole word!! AAAHH XD ")
          print("❤--------------------------❤-----------------------------❤")
          heart()
          text()
          pen.ht()
          time.sleep(6)
          exit()      
        else:
           print("✗--------------------------✗----------------------------✗")
           print("Your response is incorrect :(")
           print("✗--------------------------✗----------------------------✗\n")
           hangman_count = hangman_count + 1
           tries = tries - 1 # decresing tries
           guessed_wrong.append(guess)
           print(hangman1[hangman_count],"\n")

           continue 
    elif response.lower() == 'n':
        print(f'Enter a letter')
        guess = input().lower()
        print("----------------------------------------------------------\n")
        # one_text = input().lower() 
        print(":)------------------------:)-----------------------------:)")
        print("Checking to see if you guessed the correct letter...")
        print(":)------------------------:)-----------------------------:)\n")
        time.sleep(3)
    elif response != 'y' or 'n':
         print(f'Not a valid input')
         continue


    else:
        guess = input().lower()

    if guess in guessed_right or guess in guessed_wrong: # checking if the player has guessed a certain letter already
        print("✗--------------------------✗----------------------------✗")
        print("You already guessed", guess)
        print("✗--------------------------✗----------------------------✗\n")
    elif guess in word:
        print("✓--------------------------✓-----------------------------✓")
        print("YAY good job, you guessed a correct letter")
        print("✓--------------------------✓-----------------------------✓\n")
        guessed_right.append(guess)
    else:
        print("✗--------------------------✗----------------------------✗")
        print("OH NO! you have guessed a wrong letter :(")
        print("✗--------------------------✗----------------------------✗\n")
        hangman_count = hangman_count + 1
        tries = tries - 1 # decresing tries
        guessed_wrong.append(guess)
        print(hangman1[hangman_count],"\n")


if tries > 0:
    print("❤--------------------------❤-----------------------------❤")
    print(f'Nice you guessed the WORD you WONN <3\nThe word was {output}.')
    print("❤--------------------------❤-----------------------------❤")
    heart()
    text()
    pen.ht()
    time.sleep(6)
else:
    print(":(-------------------------:(-----------------------------:(")
    print(f"awh man, sorry you lost try again\nthe word was {word}")
    print(":(-------------------------:(-----------------------------:(")



    