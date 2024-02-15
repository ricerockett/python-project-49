import prompt
from brain_games import constants


def get_user_name_and_welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def get_player_answer():
    return prompt.string('Your answer: ')


def play_game(game_module):
    name = get_user_name_and_welcome()
    print(game_module.DESCRIPTION)
    for _ in range(constants.TASK_QTY):
        task, correct_answer = game_module.get_task_and_answer()
        print(f'Question: {task}')
        player_answer = get_player_answer()
        if correct_answer == player_answer:
            print('Correct!')
        else:
            print(f'"{player_answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}". \n'
                  f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
