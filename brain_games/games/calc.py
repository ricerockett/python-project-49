import random
from brain_games.engine import get_rnd_num
from brain_games.constants import CALC_DESCR as DESCRIPTION
from brain_games.constants import CALC_OPERATIONS


def get_rnd_operation():
    return random.choice(CALC_OPERATIONS)


def calculate_answer(num1, num2, operation):
    match operation:
        case '+':
            return str(num1 + num2)
        case '-':
            return str(num1 - num2)
        case '*':
            return str(num1 * num2)


def get_task_and_answer():
    num1, num2 = get_rnd_num(), get_rnd_num()
    operation = get_rnd_operation()
    task = f'{num1} {operation} {num2}'
    answer = calculate_answer(num1, num2, operation)
    return task, answer
