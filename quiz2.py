import random
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def welcome_message(self):
        print("\t***Welcome to  Quiz Game!***")
       
    def quiz_questions(self):
        for index, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {index}: {question['question']}")
            if 'options' in question:
                for i, option in enumerate(question['options'], start=1):
                    print(f"{i}. {option}")
            user_answer = input("Your answer: ").strip().lower()
            self.evaluate_answer(user_answer, question['answer'])

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect.")
            print(f"The correct answer is: {correct_answer}")

    def display_results(self):
        print(f"Your score is: {self.score}/{len(self.questions)}") 
        print("\t***THANKYOU!!!***")
def play_quiz():
    questions = [
        {
            "question": "What is a baby cat called?",
            "answer": "kitten"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "answer": "Jupiter"
        },
        {
            "question": "Who wrote 'merchant of venice'?",
            "answer": "william shakespeare"
        },
        {
            "question": "What does HTML stand for?",
            "answer": "hypertext markup language"
        }
    ]
    random.shuffle(questions)
    quiz = Quiz(questions)
    quiz.welcome_message()
    quiz.quiz_questions()
    quiz.display_results()

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        play_quiz()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_quiz()
