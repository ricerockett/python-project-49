from brain_games.engine import get_rnd_num
from brain_games.constants import EVEN_DESCR as DESCRIPTION


def check_if_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def get_task_and_answer():
    number = get_rnd_num()
    task = f'{number}'
    answer = check_if_even(number)
    return task, answer
