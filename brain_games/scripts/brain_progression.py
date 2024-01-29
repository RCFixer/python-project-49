from random import randint

import prompt


def greetings():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_logic(answer: int, name: str, values) -> bool:
    print(f"Question: {' '.join(values)}")
    question = prompt.string("Your answer: ")
    if question == answer:
        print("Correct!")
        return True
    else:
        print(f"'{question}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
        return False


def get_values(start_values: int) -> (list, int):
    result = [str(start_values)]
    difference = randint(2, 5)
    for value in range(randint(5, 10)):
        start_values += difference
        result.append(str(start_values))
    secret_value = randint(0, len(result)-1)
    answer = result[secret_value]
    result[secret_value] = '..'
    return result, answer


def main():
    name = greetings()
    print('What number is missing in the progression?')
    result = True
    for _ in range(3):
        start_value = randint(1, 25)
        values, answer = get_values(start_value)
        result = game_logic(answer, name, values)
        if result is False:
            break

    if result is True:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
