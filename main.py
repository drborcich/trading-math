
'''
Author: Declan R. Borcich
Date: 11/2/2021
Description:

To Do: 

1. get_operator() and int_game()
    - convert random in into operator symbol,
    -get expected (correct) answer
    -check against guess
'''


import random as rand
import time
MAX_NUM = 150
MAX_TIME = 120

def int_game(): # integers only
    print("no")
    return 0

''' 
  integer game - up to 150, rand ints and operations
  no floating point arithmetic
  game will allow for final guess past the alloted time, as
  current implementation does not have multithreading
'''

# game type - string indicates play whether
# regular arithmetic, or float division only
def play_game(game_type): # include float division, bool
    max_time = 120
    print("max_time: ", max_time)

    begin = input("Press enter to begin")

    start_time = time.time()
    #print(start_time)
    max_time += start_time
    #print(max_time)

    current_time = time.time()
    correct_answer = True # bool check for new answer
    quit = False

    tot_questions = 0
    final_score = 0

    while time_check(current_time, max_time) == True and quit == False:
        if correct_answer == True:
            tot_questions +=1 
            # get new
            rand.seed() # new seed
            sym_operator = get_operator(game_type) # string
            num_tuple = get_new_nums()
            lesser_int = num_tuple[0]
            greater_int = num_tuple[1]
            answer = get_answer(sym_operator, num_tuple)
            answer = round(float(answer),2)

        print(greater_int, " ", sym_operator, " ", lesser_int, "\n")

        guess = input("Guess: ")
        print("\n")
        if guess == "quit" or guess == "q":
            quit = True
            print("Quitting \n")
        elif guess == "skip":
            print("Skipped: answer == ", answer)
            correct_answer = True

        else:
            guess = round(float(guess),2)
            if guess != answer:
                correct_answer = False # new loop
                print("INCORRECT ... \n")
            elif guess == answer:
                final_score += 1
                correct_answer = True
                print("Correct \n")
        
        current_time = time.time()

    return (final_score, tot_questions)

# get new rand operator, return as string
# game_type =  string, "float" or "int"
def get_operator(game_type):
    if game_type == "float":
        return "/"
    # else
    rand.seed()
    operator = rand.randint(0,3)
    if operator == 0:
        sym_operator = "/"
    if operator == 1:
        sym_operator = "*"
    if operator == 2:
        sym_operator = "-"
    if operator ==3:
        sym_operator = "+"
    return sym_operator

# get new rand operands, return as tuple
def get_new_nums():
    nums = (0,0) # tuple
    greater = rand.randint(1,MAX_NUM)
    # nums must be distinct
    lesser = rand.randint(1,greater-1) 
    nums = (lesser,greater)
    return nums

# take current and end times, in machine scale
# print current time in human secs
def time_check(current, end):
    print("Time left: ", round(end-current,2))
    if current < end:
        # thus continue
        return True
    print("Done")
    return False

# take operator string, nums
# return correct algebraic answer
def get_answer(sym_operator, num_tuple):
    lesser_int = num_tuple[0]
    greater_int = num_tuple[1]

    if sym_operator == "/":
        answer = greater_int / lesser_int 
        round(answer,2) # round to 2 dec places
    if sym_operator == "*":
        answer = greater_int * lesser_int
    if sym_operator == "-":
        answer = greater_int - lesser_int
    if sym_operator == "+":
        answer = greater_int + lesser_int
    return answer

def main():
    game_type = input("float only (f)? or regular/int only (i)")
    final_score = 0

    if game_type == "i":
        game_type = "int"
        final_scores = int_game(game_type)
    if game_type == "f":
        game_type = "float"
        final_scores = play_game(game_type)
    
    print(final_scores[0], "correct of ", final_scores[1])
    return

if __name__ == '__main__':
    main()