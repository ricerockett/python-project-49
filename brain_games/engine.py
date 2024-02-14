import prompt
import random


def get_user_name_and_welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def get_rnd_num(start=0, end=100):
    return random.randint(start, end)


def ask_question(given_data):
    print(f'Question: {given_data}')


def get_player_answer():
    return prompt.string('Your answer: ')


def play_game(game_module):
    name = get_user_name_and_welcome()
    print(game_module.DESCRIPTION)
    for _ in range(3):
        task, correct_answer = game_module.get_task_and_answer()
        ask_question(task)
        player_answer = get_player_answer()
        if correct_answer == player_answer:
            print('Correct!')
        else:
            print(f'"{player_answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}". \n'
                  f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations, {name}!')
