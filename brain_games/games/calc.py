import random
from brain_games import constants


DESCRIPTION = 'What is the result of the expression?'


def calculate_answer(num1, num2, operation):
    match operation:
        case '+':
            return str(num1 + num2)
        case '-':
            return str(num1 - num2)
        case '*':
            return str(num1 * num2)


def get_task_and_answer():
    num1 = random.randint(constants.MIN_RND, constants.MAX_RND)
    num2 = random.randint(constants.MIN_RND, constants.MAX_RND)
    operation = random.choice(constants.CALC_OPERATIONS)
    task = f'{num1} {operation} {num2}'
    answer = calculate_answer(num1, num2, operation)
    return task, answer
