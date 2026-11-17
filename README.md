# Sweet Treat Task Game

This program features a game that determines whether the user earns a “sweet treat” for the day based on taks completed form user-inputted task list.

## Flow of Game 
The user is first prompted to input a comma-seperated list of tasks that they want to complete for the day. (Note:list must not exceed indicated limit of inputted tasks length indicated by constnst, MAX_TASKS  which is set to 15). Once the user submits their list of task, their inputted list is displayed for the user for review. The user is then prompted to confirm the accuracy of their list. If list is inaccurate, the user is prompted to change their inputs. 

Once task list is finalized, users are prompted to assign a "priority level" for each task. The priority levels are low, medium-low, medium, medium-high, high. The intution is tasks that are not as signifcant to the user can be assigned a "low" priority level for example and earn less points than a task that may be more signifcant  to the user and thus can yield more points for the user, if completed.

Once priority levels have been assigned for each task, the user is prompted to input a "threshold" which is simply a number (1-100) which can be interpretred as a percentage of points the user wants to use as threshold for determing when the sweet treat is earned. 

Once the threshold has been set, the user is prompted to input whether they completed each taks. For tasks the user completed, points are accrued based on difficulty: 1 point for low and up to 5 points for high.  For tasks, the user did not complete, they are offered the opportunity to recover points through mini-games. The suer may be prompted to answer a mathematical problem as part of a mental math mini game or guess a secret word given a theme and corresponding hint as part of a secret word mini-game. The user earns a point per game and can earn up to 1,2,3 points depending on the delineated difficulty level of the specific game.  To opt out, the user should follow the directions in the prompt of each given game.

Finally, the program will display total accrued points and relay to user whether they have earned a treat for the day or not. The user wins if they earn a sweet treat and loses, if they do not.


## How the game stores user state

The game stores tasks and their difficulty levels in a dictionary called task_list_dict. Each task name is a key, and its difficulty is the value. This keeps each task paired with its priority so the program can look up the right point value when you report completing it. The integer variable, score, accumulates points for completed tasks. The program also tracks the total possible points and the threshold percentage to decide whether you earned the treat.