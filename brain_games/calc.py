import random
from brain_games.engine import get_rnd_num, play_game
from brain_games.constants import calc_rule, calc_operations


def get_rnd_operation():
    return calc_operations[random.randint(0, len(calc_operations) - 1)]


def calculate_answer(first_num, second_num, operation):
    match operation:
        case '+':
            return str(first_num + second_num)
        case '-':
            return str(first_num - second_num)
        case '*':
            return str(first_num * second_num)


def get_task_and_answer():
    first_num = get_rnd_num()
    second_num = get_rnd_num()
    operation = get_rnd_operation()
    task = f'{first_num} {operation} {second_num}'
    answer = calculate_answer(first_num, second_num, operation)
    return task, answer


def start():
    play_game(calc_rule, get_task_and_answer)
