import random

class Wordle:
    def __init__(self): # Initialises the game with a random target word.
       
        self.words = ["apple", "grape", "peach", "berry", "melon"]
        self.target_word = random.choice(self.words)
        self.attempts = 6

    def check_guess(self, guess): # Checks the guess against the target word
        
        result = []
        for i, letter in enumerate(guess): # Check each letter in the guess
            if letter == self.target_word[i]: # If the letter is in the correct position, mark it as green
                result.append((letter, "green"))
            elif letter in self.target_word:
                result.append((letter, "yellow"))
            else:
                result.append((letter, "gray"))
        return result

    def play(self): # This function starts the game
        
        print("Welcome to Wordle!")
        print("Guess the 5-letter word. You have 6 attempts.")
        
        while self.attempts > 0: # COunts the attempts left
            guess = input(f"\nAttempts left: {self.attempts}. Enter your guess: ").lower() # Prompts to enter guess
            