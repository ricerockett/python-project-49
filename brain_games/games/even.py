import random
from brain_games import constants


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_task_and_answer():
    number = random.randint(constants.MIN_RND, constants.MAX_RND)
    task = f'{number}'
    answer = 'yes' if is_even(number) else 'no'
    return task, answer
