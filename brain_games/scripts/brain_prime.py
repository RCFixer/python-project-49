from random import randint

import prompt


def greetings():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_logic(answer: int, name: str, number: int) -> bool:
    print(f"Question: {number}")
    question = prompt.string("Your answer: ")
    answer = 'yes' if answer is True else 'no'
    if question == answer:
        print("Correct!")
        return True
    else:
        print(f"'{question}' is wrong answer ;(. Correct answer was"
              f" '{answer}'.\nLet's try again, {name}!")
        return False


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    name = greetings()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    result = True
    for _ in range(3):
        number = randint(1, 25)
        answer = is_prime(number)
        result = game_logic(answer, name, number)
        if result is False:
            break

    if result is True:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
