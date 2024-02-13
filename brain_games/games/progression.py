from brain_games.engine import get_rnd_num
from brain_games.constants import LOW_TRESHOLD, TOP_TRESHOLD
from brain_games.constants import PROGRESSION_DESCR as DESCRIPTION
from brain_games.constants import MIN_PROGR_LEN
from brain_games.constants import MAX_PROGR_LEN, MAX_PROGR_STEP


def get_task_and_answer():
    start = get_rnd_num(LOW_TRESHOLD, TOP_TRESHOLD)
    progr_length = get_rnd_num(MIN_PROGR_LEN, MAX_PROGR_LEN)
    step = get_rnd_num(LOW_TRESHOLD, MAX_PROGR_STEP)
    index = get_rnd_num(LOW_TRESHOLD, progr_length)
    progression = []
    for i in range(progr_length + 1):
        progression.append(str(start + step * i))
    answer = progression[index]
    progression[index] = '..'
    task = ' '.join(progression)
    return task, answer
