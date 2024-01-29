from random import randint

import prompt


def greetings():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_logic(answer: int, name: str, first_num: int, second_num: int) -> bool:
    print(f"Question: {first_num} {second_num}")
    question = prompt.string("Your answer: ")
    if int(question) == answer:
        print("Correct!")
        return True
    else:
        print(f"'{question}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
        return False


def find_gcd(first_num: int, second_num: int) -> int:
    while second_num != 0:
        first_num, second_num = second_num, first_num % second_num
    return first_num


def main():
    name = greetings()
    print('Find the greatest common divisor of given numbers.')
    result = True
    for _ in range(3):
        first_num = randint(1, 50)
        second_num = randint(1, 50)
        answer = find_gcd(first_num, second_num)
        result = game_logic(answer, name, first_num, second_num)
        if result is False:
            break
    if result is True:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
