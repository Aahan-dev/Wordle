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
            
            if len(guess) != 5:
                print("Please enter a 5-letter word.") # Checks if the word is 5 letters
                continue
           
            self.attempts -= 1 # Reduces the attempts left after each guess
            result = self.check_guess(guess)
           
            for letter, color in result:
                if color == "green": # If the letter is in the correct position, mark it as green
                    print(f"{letter} (Correct!)", end=" ")
                elif color == "yellow": # If the letter is in the wordd but in the wrong position, mark it as yellow
                    print(f"{letter} (Wrong position)", end=" ")
                else:
                    print(f"{letter} (Not in word)", end=" ") # If letter not in word, mark it as gray
            print()

            if guess == self.target_word: # If the guess is correct, end the game
                print("Congratulations! You've guessed the word!")
                return

        print(f"Sorry, you've run out of attempts. The word was: {self.target_word}.") # If the usr runs out of attempts, end the game

def main(): # This function runs the game
   
    game = Wordle()
    game.play()

if __name__ == "__main__":
    main()  # Run the main function
