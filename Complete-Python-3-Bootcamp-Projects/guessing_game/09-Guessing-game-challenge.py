from random import randrange
import sys

random_int = randrange(0, 100)
print(random_int)

count = 0
print('count value : ', count)

guessed_numbers = []


while True:
    player_input = input("Guess a number from 0 to 100 : ")
    if player_input == 'e' or player_input == 'exit':
        sys.exit()

    converted_input = int(player_input)

    guessed_numbers.append(converted_input)
    # print('guessed nums : ', guessed_numbers)

    if converted_input == random_int:
        print('Correct guess!!')
        print(f'You got the right answer in {len(guessed_numbers)} guesses!')
        break

    if count == 0:
        print("WARM!") if 11 > abs(converted_input - random_int) > 0 else print("COLD!")
        count += 1
        continue

    if count > 0:
        previous_number = guessed_numbers[-2]
        print('previous_number : ', previous_number)

        if abs(previous_number - random_int) < abs(converted_input - random_int):
            print('COLDER!')
        else:
            print('WARMER!')

