from random import randint

import prompt


def greetings():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def main():
    name = greetings()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    answers = 0
    while answers < 3:
        secret_number = randint(1, 25)
        even_or_odd = 'no' if (secret_number % 2) else 'yes'
        question = prompt.string(f"Question: {secret_number}\n")
        if question == even_or_odd:
            print("Correct!")
            answers += 1
        else:
            print(f"'{question}' is wrong answer ;(. Correct answer was '{even_or_odd}'.\nLet's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
