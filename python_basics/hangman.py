"""Simple game about hangman"""

import os
import random
import states


def get_something_word():
    """Return something random word from file"""
    f = open('words.txt', 'r')
    words = f.readlines()
    random_id = random.randrange(len(words))
    random_word = words[random_id]
    return random_word.replace('\n', '')


def print_word_to_file(word):
    """After game write current word to file"""
    f = open('past_words.txt', 'a')
    f.write(word + "\n")


def read_old_words():
    """Return old words for view"""
    f = open('past_words.txt', 'r')
    words = f.readlines()
    if len(words) == 0:
        return False
    return words


def create_dict_for_word(word):
    """Dict for current position letters in word"""
    dict_for_word = dict()
    for i in range(len(word)):
        if word[i] not in dict_for_word.keys():
            dict_for_word[word[i]] = [i]
        else:
            dict_for_word[word[i]].append(i)
    return dict_for_word


def get_hangman_condition(id_state):
    """Return current state a hangman on a picture"""
    return "Current state:\n" + states.states[id_state]


def main_interface(secret, guess, misses):
    """Shows the current state about game"""
    print(f"Word: {secret}")
    print(f"Guess: {guess}")
    print("Misses: ", end='')
    print(*misses)


def correct_added_letter(secret, letter, current_dict):
    """Fills underscores with a guessed letters"""
    len_word = len(secret)
    for i in range(len(current_dict[letter])):
        id_position = current_dict[letter][i]
        if id_position == 0:
            secret = letter + secret[1:]
        elif id_position == len_word - 1:
            secret = secret[:-1] + letter
        else:
            secret = secret[:id_position] + letter + secret[id_position+1:]
    return secret


def game_request():
    """After the game asks for a choice"""
    answer = input("Want to play more? 'Yes' or 'No' or 'View' to see old words -> ")
    if answer.lower() == "no":
        return False
    elif answer.lower() == "view":
        words = read_old_words()
        if words:
            print("Words: ", end=' ')
            [print(i.replace('\n', ''), end=' ') for i in words]
        else:
            print("No history")
        input("\nPress 'Enter' to continue -> ")
        # want to play again
        game_request()
    return True


def check_for_win_loss(secret, wrong_answers, current_word):
    """Check for game win or lose. Return False if player want to exit"""
    if secret.isalpha() or wrong_answers == 6:
        # print current word to file
        print_word_to_file(current_word)
        print("\nYou Won!") if secret.isalpha() else print("\nYou Lost!")
        game_status = game_request()
        if game_status:
            game_work()
        return game_status
    return True


def gameplay(game_status, wrong_answers, current_word, secret, dict_letters, incorrect_letters):
    """Game process and asks for the next letter input"""
    print("\nWelcome to the game Hangman. \nIf u want to exit - input 'Exit'")
    while game_status:
        next_letter = input("\nPrint next letter -> ").lower()
        # check letter to correct word
        if next_letter.isalpha() and len(next_letter) == 1:
            if next_letter in dict_letters.keys():
                secret = correct_added_letter(secret, next_letter, dict_letters)
            else:
                incorrect_letters.append(next_letter)
                wrong_answers += 1
                print(get_hangman_condition(wrong_answers))

            # show main info
            main_interface(secret, next_letter, incorrect_letters)
            # check current state game
            game_status = check_for_win_loss(secret, wrong_answers, current_word)

        elif next_letter.lower() == "exit":
            break
    print("Thanks for the play in this game!")


def default_values():
    """0 - game_status, 1 - wrong_answer, 2 - current_word, 3 - secret, 4 - dict_letters, 5 - incorrect_letters"""
    game_status = True
    # for func where pictures steps
    wrong_answers = 0
    current_word = get_something_word()
    secret = "_" * len(current_word)
    dict_letters = create_dict_for_word(current_word)
    incorrect_letters = []
    return game_status, wrong_answers, current_word, secret, dict_letters, incorrect_letters


def game_work():
    """Gets default values and calls gameplay func"""
    values = default_values()
    os.system('clear')
    gameplay(values[0], values[1], values[2], values[3], values[4], values[5])


if __name__ == "__main__":
    game_work()
