import random
def secret_word_ ():
 """
 Conducts a secret word mini-game by randomly selecting
 a theme and a corresponding secret word from predefined
 word banks.
 
 The user receives a hint associated with the selected
 word and is prompted to guess the correct answer.
 
 Inputs:
        N/A

    Side Effects:
        Displays the selected theme and corresponding hint.
        Informs the user whether their guess is correct and
        reveals the secret word when the guess is incorrect.

    Outputs:
        score_game = int; the number of points earned by
        correctly guessing the secret word. Returns zero
        if the user opts out or guesses incorrectly.
    """
   
 word_bank_dict = {"Country":["China", "Haiti","Honduras", "Brazil"], "Color":["Red", "Black", "Gray", "White", "Yellow"], "Holy Cross": ["Kimball", "Holding the door", "Crusaders", "Montserrat"]}
 hints_bank_dict= {"China":"This country is home to the Great Wall.", "Haiti": "This country shares the island of Hisponiola with the Dominican Republic.", "Honduras":"This country's capital is Tegucigalpa.", "Brazil":"This country popularized the music genre funk carioca.",
                      "Red": " This color is not visible to bulls.", "Black":"This color is associated with evil, death, etc.", "Gray":"This color is the color that hair turns as people age.", "White":"This color is associated with mourning, grief and funerals in many Asian cultures.", "Yellow":"This color is associated with Taxis.",
                      "Kimball":"This is the sole dining hall at the College of the Holy Cross","Holding the Door": "This is a long-standing social norm at the College of the Holy Cross", "Crusaders":"This is the mascot for the College of the Holy Cross", "Montserrat": "This is the course that every first-year student at Holy Cross must take." }

 score_game = 0
   
 theme = random.choice(list(word_bank_dict.keys()))

 correct_answer = random.choice(word_bank_dict[theme])
    
 hint = hints_bank_dict[correct_answer]
    
 print(f"The theme of the secret word is {theme}.")

 print(f"Hint: {hint}")


 user_answer= input("Enter 'X' if you want to opt out of game. \n Enter your guess: \n ")
 if user_answer.upper() == "X":
    return score_game
 elif user_answer.capitalize() == correct_answer:
        score_game += 1
        print("You have correctly guessed the secret word!")
 else:
    print(f"You have not guessed the secret word. : (  \n The secret word was: {correct_answer}")
 return score_game
  

    