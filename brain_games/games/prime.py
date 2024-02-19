import random
from brain_games import constants


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    for divider in range(2, int(num ** 0.5) + 1):
        if num % divider == 0:
            return False
    return True


def get_task_and_answer():
    num = random.randint(constants.MIN_RND, constants.MAX_RND)
    task = f'{num}'
    answer = 'yes' if is_prime(num) else 'no'
    return task, answer
