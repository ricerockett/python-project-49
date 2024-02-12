from brain_games.engine import get_rnd_num, play_game
from brain_games.constants import LOW_TRESHOLD, TOP_TRESHOLD
from brain_games.constants import PROGRESSION_RULE, MIN_PROGR_LEN
from brain_games.constants import MAX_PROGR_LEN, MAX_PROGR_STEP


def get_progression_and_answer():
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


def start():
    play_game(PROGRESSION_RULE, get_progression_and_answer)
