import random
from handle_input import handle_input, LengthError
from read_word_list import possible_words

def print_board(game):
    for r in game:
        print(r)

target_word = possible_words[random.randint(0, len(possible_words) - 1)]
move = 0
board = []


for move in range(6):
    user_input = None
    feedback = None
    output = ""

    while True:
        user_input = input('Enter your guess: ')

        try:
            feedback = handle_input(user_input, target_word)
            break
        except ValueError:
            print('Not in words list')
        except LengthError:
            print('Length incorrect')

    for f in feedback:
        if f == 0:
            output += "⬛️"
        elif f == 1:
            output += "🟨"
        else:
            output += "🟩"

    board.append(output)
    print_board(board)

    if target_word == user_input:
        print(f'All Correct! You found the word in {move + 1} moves')
        exit(0)

print(f'You ran out of guesses. The correct word was {target_word}. Try again next time!')



