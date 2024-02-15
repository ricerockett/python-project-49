import random
from brain_games import constants


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    while num2:
        num2, num1 = num1 % num2, num2
    return str(num1)


def get_task_and_answer():
    num1 = random.randint(constants.MIN_RND, constants.MAX_RND)
    num2 = random.randint(constants.MIN_RND, constants.MAX_RND)
    task = f'{num1} {num2}'
    answer = get_gcd(num1, num2)
    return task, answer
