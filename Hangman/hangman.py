import random

loss = 0
win = 0

print("H A N G M A N")


def body():
    global win
    global loss
    words = ['python', 'java', 'swift', 'javascript']
    word = random.choice(words)
    secret_list = list('-' * len(word))
    check_set = set()
    attempts = 7

    while True:
        print()
        print("".join(secret_list))
        
        if secret_list.count("-") == 0:
            print(f"You guessed the word {word}! \nYou survived!")
            win += 1
            word = random.choice(words)
            secret_list = list('-' * len(word))
            break
        
        if attempts < 0:
            print("You lost!")
            loss += 1
            break
            
        letter = input("Input a letter: ")
        
        if len(letter) != 1:
            print("Please, input a single letter.")
        elif letter.isalpha() is False or letter.isupper():
            print("Please, enter a lowercase letter from the English alphabet.")
        elif letter in check_set:
            print("You've already guessed this letter.")
        elif letter in word and letter not in ''.join(secret_list): 
            for i in range(len(word)):
                if word[i] == letter:
                    secret_list[i] = letter
        elif letter not in word:
            print("That letter doesn't appear in the word")
            attempts -= 1
        
        check_set.add(letter)


def results():
    print(f"You won: {win} times")
    print(f"You lost: {loss} times")


def game():
    while True:
        user_input = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')

        if user_input == "play":
            body()
        elif user_input == "results":
            results()
        elif user_input == "exit":
            break
        else:
            user_input = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
            

game()