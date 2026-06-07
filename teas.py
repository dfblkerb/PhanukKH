# Smart Quiz Game

questions = [
    {
        "question": "What is the capital of France?",
        "answer": "paris"
    },
    {
        "question": "Which language is used for AI and Data Science?",
        "answer": "python"
    },
    {
        "question": "What is 5 + 7?",
        "answer": "12"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "mars"
    }
]

def start_quiz():
    score = 0

    print("\n===== Welcome to Smart Quiz Game =====\n")

    for q in questions:

        print(q["question"])
        user_answer = input("Your answer: ").lower()

        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong!")
            print("Correct answer:", q["answer"], "\n")

    print("Quiz Finished!")
    print("Your score:", score, "/", len(questions))

# Main Loop
while True:

    start_quiz()

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thank you for playing!")
        break