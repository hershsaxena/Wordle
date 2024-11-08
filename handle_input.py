import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_HOST = os.getenv('API_HOST')

class LengthError(Exception):
    pass


def validate_word(word):
    url = f'https://wordsapiv1.p.rapidapi.com/words/{word}/definitions'

    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': API_HOST
    }

    response = requests.get(url, headers=headers)

    return not response.status_code == 404

def give_feedback(user_input, target):
    letters_in_target = list(target)
    res = []

    for i in range(len(user_input)):
        c = user_input[i]
        if c not in letters_in_target:
            res.append(0)
        else:
            if c == target[i]:
                res.append(2)
            else:
                res.append(1)

    return res

def handle_input(user_input, target):
    if not validate_word(user_input):
        raise ValueError
    elif len(user_input) != 5:
        raise LengthError
    else:
        return give_feedback(user_input, target)