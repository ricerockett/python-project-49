from brain_games.engine import get_rnd_num, play_game
import math
from brain_games.constants import prime_rule


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


def start():
    play_game(prime_rule, get_task_and_answer)
