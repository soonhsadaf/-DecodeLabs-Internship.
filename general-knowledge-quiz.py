# General Knowledge Quiz Game

def quiz_game():
    score = 0

    print("Welcome to the General Knowledge Quiz!\n")

    # Question 1
    answer1 = input("1. What is the capital of France? ")
    if answer1.strip().lower() == "paris":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is Paris.\n")

    # Question 2
    answer2 = input("2. Who wrote 'Romeo and Juliet'? ")
    if answer2.strip().lower() in ["william shakespeare", "shakespeare"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is William Shakespeare.\n")

    # Question 3
    answer3 = input("3. What is the largest planet in our solar system? ")
    if answer3.strip().lower() == "jupiter":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is Jupiter.\n")

    print(f"Your final score is {score}/3")

if __name__ == "__main__":
    quiz_game()
