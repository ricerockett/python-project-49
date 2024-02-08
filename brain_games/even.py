from brain_games.engine import get_rnd_num, run_game


def set_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def check_if_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def get_task_and_answer():
    number = get_rnd_num()
    task = f'{number}'
    answer = check_if_even(number)
    return task, answer


def start():
    run_game(set_rules, get_task_and_answer)
