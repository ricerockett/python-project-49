from brain_games.engine import get_rnd_num, play_game
from brain_games.constants import even_rule


def check_if_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def get_task_and_answer():
    number = get_rnd_num()
    task = f'{number}'
    answer = check_if_even(number)
    return task, answer


def start():
    play_game(even_rule, get_task_and_answer)
