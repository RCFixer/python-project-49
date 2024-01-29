from random import randint, shuffle

import prompt


def greetings():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_logic(first_number, second_number, answer, action, name):
    print(f"Question: {first_number} {action} {second_number}")
    question = prompt.string("Your answer: ")
    if int(question) == answer:
        print("Correct!")
        return True
    else:
        print(f"'{question}' is wrong answer ;(. Correct answer was "
              f"'{answer}'.\nLet's try again, {name}!")
        return False


def main():
    name = greetings()
    print('What is the result of the expression?')
    actions = ['+', '-', '*']
    shuffle(actions)
    result = True
    for action in actions:
        first_number = randint(1, 25)
        second_number = randint(1, 25)
        match action:
            case '+':
                answer = first_number + second_number
                result = game_logic(first_number, second_number,
                                    answer, action, name)
            case '-':
                answer = first_number - second_number
                result = game_logic(first_number, second_number,
                                    answer, action, name)
            case '*':
                answer = first_number * second_number
                result = game_logic(first_number, second_number,
                                    answer, action, name)
        if result is False:
            break
    if result is True:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
