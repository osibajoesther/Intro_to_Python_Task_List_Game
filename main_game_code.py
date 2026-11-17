import random
import mental_math_game
import secret_word_game

MAX_TASKS = 15

def get_tasks():
    """
    This function collects user inputs for the tasks they want to complete for the day
    Input(s):
    N/A
    Output(s):
    list; user inputted list of tasks that user wants to complete for the day
    """

    list =  input("What are the tasks that you plan to complete for the day? Please use a comma to sperate your inputs. \n ").split(",")  
                     
    return list
     
def task_scoring(difficulty):
    """
    This function computes the total possible points the user can earn for varying tasks.
    Input(s):
        difficulty = dict; tasks and user inputted difficulty level per task
    Output(s):
        total possible points = int; the number of points user can earn based on inputted difficulty for tasks
    """

    total_possible_points = 0

    for task, diff_level in difficulty.items():

        if  diff_level== "low":
            total_possible_points += 1

        elif diff_level == "medium-low":
            total_possible_points += 2
        
        elif diff_level == "medium":
           total_possible_points += 3

        elif diff_level == "medium-high":
            total_possible_points += 4
        
        else:
            total_possible_points += 5

    return total_possible_points

def sweet_treat(score, difficulty, threshold_points):
    """
    This function determines whether the player earned a sweet treat for the day. 
     Input(s): 
        score = int; the user's final score based on the tasks they have completed for the day.
       difficulty = dict; tasks and user inputted difficulty level per task
        threshold_points = float; minimum points required to earn a sweet treat.

     Side Effect(s):
      str; displays the percentage of total possible points earned  and whether the user earned a sweet treat.

        
     Output(s):
       final = str; tells the percentage of total possible points they have earned and whether they earned a sweet treat for the day or not.
    """
    total_possible_points = task_scoring(difficulty)
    
    if score < threshold_points:
        recommendation = "You have not earned a sweet treat for the day. :()"
    else:
        recommendation = "You have earned a sweet treat for the day! ;)"

    final = f"You earned {(score/total_possible_points):.1%} of total possible points. {recommendation}"

    print(final)

    return final

def validate_schedule(schedule):

    """
    This function validates the user's input for their list of tasks. 

    Input(s):
        schedule= list; user input of tasks they want to complete
    
    Side Effect(s):
     str; Tells user if they inputted too many tasks; prompts them to confirm if they input only 1 task
     str; Informs user their decision based on input (i.e. confirmed inputs or prompts to input new inputs)

    Output(s):
        Boolean; determines if input is valid. (True, if valid input and False, otherwise)
    """
    if schedule == [""]:
         print ("Please enter at least one task.")
         return False
    elif len(schedule) == 1:
            print("You have only entered 1 task. If this is correct, confirm in the next stage of the validation process. If not, make changes to list.")    
    elif len(schedule) > MAX_TASKS:
        print(f"You have exceeded the maximum limit of {MAX_TASKS} tasks.")
        return False
    elif len(schedule) < 1:
        print("Please enter at least one task.")
        return False

    string_of_tasks = ",".join(schedule)

    print(f"Your task list is : {string_of_tasks}")


    confirm = input("Confirm that the list of tasks you entered is correct. Enter 'C' to confirm that the list of tasks is accurate or 'N' to make changes to your list:\n")

    
    if confirm.capitalize() == "C":
        print("Great! You have confirmed that the list of tasks is correct.")
        return True
    elif confirm.capitalize() == "N":
        print("Please re-enter your list of tasks.")
        return False
    else:
        print("Please enter 'C' to confirm or 'N' to change your inputs.")
        return False

def validate_difficulty_input(difficulty):
    """
        This function validates the user's input for the difficulty levels of each of their tasks. 
    
        Input(s):
            difficulty= str; user input of difficulty levels for tasks they want to complete
        
        Side Effect(s):
         str; Tells user if they inputted an invalid difficulty level
    
        Output(s):
            Boolean; determines if input is valid. (True, if valid input and False, otherwise)
        """
    if difficulty.lower() != "low" and difficulty.lower() !="medium-low" and difficulty.lower() !="medium" and difficulty.lower() !="medium-high" and difficulty.lower() !="high":
        print ("This is not a valid input! Please try again. ")
        return False
    else:
         return True

def validate_threshold (threshold):
     """
     This function validates the user's input for the threshold.
        
        Input(s):
        threshold = float; user input of threshold for total points they want to earn
            
     Side Effect(s):
        str; Tells user if they inputted an invalid threshold
        
     Output(s):
        Boolean; determines if input is valid. (True, if valid input and False, otherwise)
    """
    
     if threshold < 1 or threshold > 100:
        print("This is not a valid input. Please try again!")
        return False
     else:
        return True
       
def validate_status(status):
    """
     This function validates the user's input for task completion status.
            
     Input(s):
        status = str; user input of "yes" or "no" to indicate whether they completed task or not
                
     Side Effect(s):
        str; Tells user if they inputted an invalid task completion status
            
     Output(s):
        Boolean; determines if input is valid. (True, if valid input and False, otherwise)
     """
    
    if status.capitalize() != "Yes" and status.capitalize() != "No":
          print("You have not entered a valid input. Please try again.")
          return False
    else:
          return True 

if __name__== "__main__":

    mistakes = 0

    valid_task = False
    
    while valid_task == False and mistakes < 10:
        tasks= get_tasks()

        if validate_schedule(tasks) == True:
            valid_task = True

        else:
            mistakes += 1
            print("You have entered an invalid input! Try again.")
    
    if valid_task == False:
        print("You have reached the maximum of 10 invalid input attempts. Please Play Again!")


    tasks = tuple(tasks)
    
   
    priority =[]

    for task in tasks:
        task_priority = input(f"Assign a priority level (low, medium-low, medium, medium-high, high) for {task}: \n").strip().lower()

        while validate_difficulty_input(task_priority)== False:
             task_priority = input(f"Assign a priority level (low, medium-low, medium, medium-high, high) for {task}: \n").strip().lower()
        
        priority.append(task_priority)
    
    priority = tuple(priority)


    invalid_input_count = 0
    valid_threshold = False

   
    while valid_threshold == False and invalid_input_count < 15: 
        try:
            threshold = float(input(("What percentage of tasks do you need to complete? Enter a number between 1 and 100: \n ")))

            if validate_threshold(threshold) == True:
                valid_threshold = True
            else: 
                invalid_input_count += 1
             
        except ValueError:
            print("Please enter a number.")
            invalid_input_count += 1
            
    if valid_threshold == False:
        print("You have reached the maximum of 15 invalid input attempts. Please play again.")
   

    task_list_dict={}
 
    for index in range(len(tasks)):
        key = tasks[index]
        value = priority[index]

        task_list_dict[key] = value

  

    goal = task_scoring(task_list_dict)

    threshold_points = (goal* (threshold/100))

    print(f"You can earn {goal} points by completing all your tasks for the day."
          f"You need to earn {threshold_points:.2f} of {goal} total possible points to earn a sweet treat for today!")
   

    score = 0

    for task in tasks:

        valid_status = False

        while valid_status== False:
            status = (input(f"Did you complete {task}? \n Please enter 'Yes' or 'No': "))
            if validate_status(status) == True:
                valid_status = True
            else: 
                 valid_status= False

        if status.capitalize() == "Yes":
            priority = task_list_dict[task]
            if  priority== "low":
                    score += 1
            elif priority == "medium-low":
                    score += 2
            elif priority == "medium":
                    score += 3
            elif priority == "medium-high":
                    score += 4
            else:
                    score += 5

        if status.capitalize()== "No":
        
            print(f"To recover points from not completing {task}, guess the secret word or solve mental math problems.")

            priority = task_list_dict[task]
            if  priority== "low":
                attempt = 1
            elif priority == "medium-low":
                attempt = 1
            elif priority == "medium":
                attempt = 2
            elif priority == "medium-high":
                attempt = 2
            else:
                attempt = 3

            recovered_points = 0

            for _ in range(attempt):
                if random.random() > 0.5:
                    score_game = mental_math_game.math_break()
                else:
                    score_game = secret_word_game.secret_word_()
                
                recovered_points += score_game
            
            score += recovered_points
            print(f"You have recovered {recovered_points} points from playing mini-game.")

    print(f" You have earned {score} points for the day!")
    sweet_treat(score,task_list_dict,threshold_points)
