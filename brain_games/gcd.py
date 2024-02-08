from brain_games.engine import get_rnd_num, run_game


def set_rules():
    print('Find the greatest common divisor of given numbers.')


def get_gcd(num_1, num_2):
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1
    for i in range(1, num_1 + 1):
        if num_1 % i == 0 and num_2 % (num_1 / i) == 0:
            return str(int(num_1 / i))


def get_task_and_answer():
    number_1 = get_rnd_num()
    number_2 = get_rnd_num()
    task = f'{number_1} {number_2}'
    answer = get_gcd(number_1, number_2)
    return task, answer


def start():
    run_game(set_rules, get_task_and_answer)
