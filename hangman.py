import random

words = ["apple", "banana", "grape", "mango", "peach"]
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

while wrong_guesses < max_wrong:
    display = ""
    
    print("\nGuessed letters:", guessed_letters)

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)

    if display.replace(" ", "") == word:
        print("🎉 You won!")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Enter only one letter!")
        continue

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        print("❌ Wrong!")
        wrong_guesses += 1
        print("Remaining chances:", max_wrong - wrong_guesses)

if wrong_guesses == max_wrong:
    print("💀 Game Over! The word was:", word)