import prompt
import random


def greet():
    print('Welcome to the Brain Games!')


def get_user_name_and_welcome():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def get_rnd_num(start=0, end=100):
    return random.randint(start, end)


def ask_question(given_data):
    print(f'Question: {given_data}')


def get_player_answer():
    return prompt.string('Your answer: ')


def compare_answers_and_print_result(correct_answer, player_answer, name):
    if correct_answer == player_answer:
        print('Correct!')
        return True
    else:
        print(f'"{player_answer}" is wrong answer ;(. '
              f'Correct answer was "{correct_answer}". \n'
              f'Let\'s try again, {name}!')
        return False


def run_game(rules, task_and_answer):
    greet()
    name = get_user_name_and_welcome()
    rules()
    for i in range(3):
        task, answer = task_and_answer()
        ask_question(task)
        player_answer = get_player_answer()
        if not compare_answers_and_print_result(answer, player_answer, name):
            break
    else:
        print(f'Congratulations, {name}!')
