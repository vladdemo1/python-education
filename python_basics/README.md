# Info about hangman program

---

In this program u can play in hangman. Write one letter at the beginning.

If u guess the letter, u will only see the hidden word and the positions 
where the guessed letter stands.

Otherwise, u will see the gallows with one life spent.

Only 6 lives per try.

After the game, u can view old words, start a new one or exit the game.

Good luck and have fun.

---

### Functions

---

##### get_something_word() - Return something random word from file words.txt

---
##### print_word_to_file() - After game write current word to file past_words.txt

---
##### read_old_words() - Return old words for view if player want to this

---
##### create_dict_for_word() - Dictionary for current position (index) letters in word

---
##### get_hangman_condition() - Return current state a hangman from file states.py

---
##### main_interface() - Shows the current state about game. Word, guess, misses.

---
##### correct_added_letter() - Fills underscores with a guessed letters

---
##### game_request() - After the game asks for a choice (Play, show past words or exit)

---
##### check_for_win_loss() - Check for game win or lose. Return False if player want to exit

---
##### gameplay() - Game process and asks for the next letter input

---
##### default_values() - Return default values for new game

---
##### game_work() - Gets default values and calls gameplay function

---