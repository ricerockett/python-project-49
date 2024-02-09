from brain_games.engine import get_rnd_num, play_game
from brain_games.constants import GCD_RULE


def get_gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    while num2:
        num2, num1 = num1 % num2, num2
    return num1


def get_task_and_answer():
    num1, num2 = get_rnd_num(), get_rnd_num()
    task = f'{num1} {num2}'
    answer = get_gcd(num1, num2)
    return task, answer


def start():
    play_game(GCD_RULE, get_task_and_answer)
