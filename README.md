# Wordle

A Wordle clone made in Python using the terminal. It utilizes the [WordsAPI](https://www.wordsapi.com) to validate words.



## Tech

This project requires two Python libraries
- requests
- python-dotenv


## Installation

Clone the repository with the following git command

```bash
git clone https://github.com/hershsaxena/Wordle.git
```

After this, create a .env file in the main directory with the following format:

```dotenv
API_KEY = "YOUR API KEY HERE"
API_HOST = "API HOST HERE"
# ex: wordsapiv1.p.rapidapi.com
```