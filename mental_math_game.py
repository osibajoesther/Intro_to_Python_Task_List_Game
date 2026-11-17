import random
def math_break ():
    """
    Conducts a mental math mini-game by randomly selecting
    a mathematical problem from a predefined problem bank.

    The user is prompted to solve the selected problem.
    The function validates numerical input and determines
    whether the user's answer is correct.

    Inputs:
        N/A

    Side Effects:
        Displays the mathematical problem and informs the
        user whether their answer is correct.

    Outputs:
        score_game = int; the number of points earned by
        correctly answering the mathematical problem.
        Returns zero if the user opts out or answers incorrectly.
    """

    math_problems_bank_dict = {"4+3":7, "2*3":6, "7-4":3, "5*2":10, "12*10":120, 
                               "8/4":2, "7*3":21, "5*3": 15, "20-3":17, "27/3": 9, "11*10": 110,
                               "96/12": 8, "36-25":11, "2*2":4, "23+17":40, "12+21": 33}
    
    score_game = 0

    problem = random.choice(list(math_problems_bank_dict.keys()))
    
    correct_answer = math_problems_bank_dict[problem]

    invalid_input = 0
    valid_input = False

    while invalid_input < 5 and valid_input == False:
        try:
            user_answer = float(input(f"Enter '-1' if you want to opt out of game. \n What is the answer to {problem}? "))
            valid_input = True
        except ValueError:
            invalid_input += 1
            print("Please enter a number.")
    if valid_input == False:
            print("You have reached the maximum of 5 invalid input attempts.")
            return score_game
    
    if user_answer == -1:
        return score_game
    elif user_answer == correct_answer:
        print("Correct!")
        score_game +=1
    else:
        print(f"Incorrect. \n The correct answer was {correct_answer}")
    return score_game
    
    
    
