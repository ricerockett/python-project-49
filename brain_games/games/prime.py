from brain_games.engine import get_rnd_num
import math
from brain_games.constants import PRIME_RULE as RULE


def check_if_prime(num):
    for divider in range(2, int(math.sqrt(num)) + 1):
        if num % divider == 0:
            return 'no'
    return 'yes'


def get_task_and_answer():
    num = get_rnd_num()
    task = f'{num}'
    answer = check_if_prime(num)
    return task, answer
