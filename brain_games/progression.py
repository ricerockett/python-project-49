from brain_games.engine import get_rnd_num, run_game


def set_rules():
    print('What number is missing in the progression?')


def get_progression_and_answer():
    start = get_rnd_num(0, 100)
    length = get_rnd_num(5, 15)
    step = get_rnd_num(0, 10)
    index = get_rnd_num(0, length)
    progression = []
    for i in range(length + 1):
        progression.append(str(start + step * i))
    answer = progression[index]
    progression[index] = '..'
    task = ' '.join(progression)
    return task, answer


def start_game():
    run_game(set_rules, get_progression_and_answer)
