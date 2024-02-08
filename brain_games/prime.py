from brain_games.engine import get_rnd_num, run_game
import math


def set_rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def check_if_prime(num):
    for divider in range(2, int(math.sqrt(num)) + 1):
        if num % divider == 0:
            return 'no'
    return 'yes'


def get_task_and_answer():
    number = get_rnd_num()
    task = f'{number}'
    answer = check_if_prime(number)
    return task, answer


def start_game():
    run_game(set_rules, get_task_and_answer)
