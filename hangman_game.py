import random

def hangman():
    words = ['python', 'developer', 'hangman', 'challenge', 'programming']
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman! Guess the word letter by letter.")
    
    while attempts > 0:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print(f"Word: {display_word}")
        print(f"Attempts left: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good job! Keep going.")
        else:
            attempts -= 1
            print("Wrong guess!")
        
        if set(word).issubset(guessed_letters):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Game Over! The word was: {word}")

if __name__ == "__main__":
    hangman()
