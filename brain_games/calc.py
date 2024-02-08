import random
from brain_games.engine import get_rnd_num, run_game


def set_rules():
    print('What is the result of the expression?')


def get_rnd_operation():
    operations = ['+', '-', '*']
    return operations[random.randint(0, 2)]


def calculate_answer(first_num, second_num, operation):
    match operation:
        case '+':
            return str(int(first_num) + int(second_num))
        case '-':
            return str(int(first_num) - int(second_num))
        case '*':
            return str(int(first_num) * int(second_num))


def get_task_and_answer():
    first_num = get_rnd_num()
    second_num = get_rnd_num()
    operation = get_rnd_operation()
    task = f'{first_num} {operation} {second_num}'
    answer = calculate_answer(first_num, second_num, operation)
    return task, answer


def start():
    run_game(set_rules, get_task_and_answer)
