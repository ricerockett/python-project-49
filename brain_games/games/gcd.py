from brain_games.engine import get_rnd_num
from brain_games.constants import GCD_DESCR as DESCRIPTION


def get_gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    while num2:
        num2, num1 = num1 % num2, num2
    return str(num1)


def get_task_and_answer():
    num1, num2 = get_rnd_num(), get_rnd_num()
    task = f'{num1} {num2}'
    answer = get_gcd(num1, num2)
    return task, answer
