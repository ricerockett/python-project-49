import random
from brain_games import constants


DESCRIPTION = 'What number is missing in the progression?'


def get_task_and_answer():
    start = random.randint(constants.MIN_RND, constants.MAX_RND)
    progr_length = random.randint(constants.MIN_PROGR_LEN,
                                  constants.MAX_PROGR_LEN)
    step = random.randint(constants.MIN_RND,
                          constants.MAX_PROGR_STEP)
    index = random.randint(constants.MIN_RND, progr_length)
    progression = []
    for i in range(progr_length + 1):
        progression.append(str(start + step * i))
    answer = progression[index]
    progression[index] = '..'
    task = ' '.join(progression)
    return task, answer
