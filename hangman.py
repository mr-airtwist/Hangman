# Write your code here
import random

menu = ''
print("H A N G M A N")
win = 0
lost = 0
while menu != "exit":
    menu = input('''Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ''')
    words = ("python", "java", "swift", "javascript")
    random_word = random.choice(words)
    open_char = list(random_word)
    hide_char = '-' * len(random_word)
    hide_temp = list(hide_char)
    user_input = set()
    lives = 8
    if menu == "play":
        while lives > 0:
            print()
            guess = input(f"{hide_char}\n"
                          f"Input a letter: ")
            if len(guess) != 1:
                print('Please, input a single letter.')
                continue
            elif not guess.isalpha() or not guess.islower() or not guess.isalnum():
                print('Please, enter a lowercase letter from the English alphabet.')
                continue
            if guess in random_word:
                while guess in open_char:
                    index = open_char.index(guess)
                    open_char[index] = "-"
                    hide_temp[index] = guess
                    hide_char = "".join(hide_temp)
                if guess in user_input:
                    print("You've already guessed this letter.")
                user_input.update(guess)
                if hide_char == random_word:
                    win += 1
                    print()
                    print(f"You guessed the word {random_word}!")
                    print("You survived!")
                    break
            else:
                lives -= 1
                print("That letter doesn't appear in the word.")
        if hide_char != random_word:
            print()
            print("You lost!")
            lost += 1
    elif menu == "results":
        print(f'You won: {win} times.\nYou lost: {lost} times.')
