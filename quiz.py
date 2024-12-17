import random

# Funny questions and answers
questions = [
    {
        "question": "What would you do if you found a talking cat?",
        "options": ["A. Adopt it", "B. Run away screaming", "C. Ask for the lottery numbers",
                    "D. Start a podcast with it"],
        "correct": "C",
        "funny_response": "Correct! That cat might be your ticket to early retirement! 🐱💰"
    },
    {
        "question": "If you could eat only one thing forever, what would it be?",
        "options": ["A. Pizza", "B. Broccoli", "C. Ice cream", "D. Batteries (please don't pick this)"],
        "correct": "A",
        "funny_response": "Good choice! A pizza a day keeps the sadness away... or so we think. 🍕"
    },
    {
        "question": "What superpower would you like to have?",
        "options": ["A. Invisibility", "B. Super strength", "C. Talking to plants", "D. Summon chickens at will"],
        "correct": "D",
        "funny_response": "Chickens are unstoppable. Imagine a chicken army at your command! 🐔🐔🐔"
    },
    {
        "question": "What's the best way to win an argument?",
        "options": ["A. State facts", "B. Yell louder", "C. Use interpretive dance",
                    "D. Say 'You're right!' and run away"],
        "correct": "C",
        "funny_response": "Correct! Interpretive dance is the universal answer to all life's arguments. 💃"
    }
]

# Result messages based on score
results = [
    "Are you a potato? 🥔 Better luck next time!",
    "You're slightly funny, like a squirrel doing yoga. 🐿️🧘",
    "You're officially the class clown! 🤡 Nice work!",
    "You are the king of comedy! Bow down, peasants! 👑😂"
]


# Main Game Function
def silly_quiz_game():
    print("🎉 Welcome to the Silly Quiz Game! 🎉")
    print("Answer these funny questions, and let's see how silly you are!\n")

    score = 0  # Initialize score

    # Loop through questions
    for index, q in enumerate(questions, start=1):
        print(f"Q{index}: {q['question']}")
        for option in q["options"]:
            print(option)

        # Get user input
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        # Check if answer is correct
        if answer == q["correct"]:
            print(q["funny_response"])
            score += 1
        else:
            print("Oops! That was silly... but it's okay! 😅")
        print()

    # Final Result
    print("🎭 Game Over! 🎭")
    print(f"Your total score: {score}/{len(questions)}")

    if score == 0:
        print(results[0])
    elif score == 1 or score == 2:
        print(results[1])
    elif score == 3:
        print(results[2])
    else:
        print(results[3])
    print("\nThanks for playing! Keep being silly! 🤪")


# Start the game
if __name__ == "__main__":
    silly_quiz_game()
