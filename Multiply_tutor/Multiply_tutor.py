from random import randrange as ranrange
from time import time as timer

# get the ammount of questions the user wants to be asked
def amount_of_questions():
    number_of_questions = int(input("How many questions should be asked?: "))
    return number_of_questions
# get the range of mulitplcations
def range_of_mulitple():
    max_number = int(input("what should the max number be?: "))
    return max_number

def user_answer(num1,num2):
    user_answer_in = int(input(f'{num1} X {num2} = '))
    return user_answer_in

# logic for the mulitplecations to happen

def Game(number_of_questions,range_number,):
    score = 0
    answer_list = []
    start = timer()

    for i in range (number_of_questions):
        num1 = ranrange(1,range_number+1)
        num2 = ranrange(1,range_number+1)
        correct_answer = calculate_correct_answer(num1,num2)
        user_answered = user_answer(num1,num2)
        answer_list.append(f'{num1} X {num2} = {correct_answer} you: {user_answered}')
        if user_answered == correct_answer:
            score += 1
        end = timer()

    print(f'Thank you for playing! \nYou got {score} out of {number_of_questions} ({round(score/number_of_questions*100)}%) correct in {round(end-start,1)} seconds ({round((end-start)/number_of_questions,1)}seconds/question)')
    for answer in answer_list:
        print(answer)

def calculate_correct_answer(num1,num2):
    return num1 * num2

if __name__ == "__main__":
    Game(amount_of_questions(),range_of_mulitple())