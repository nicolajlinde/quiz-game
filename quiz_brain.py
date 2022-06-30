class QuizBrain:
    def __init__(self, question_list):
        self.q_list = question_list
        self.q_number = 0
        self.score = 0

    def still_have_questions(self):
        return self.q_number < len(self.q_list)

    def next_question(self):
        current_q = self.q_list[self.q_number]
        self.q_number += 1
        usr_answer = input(f"Q.{self.q_number}: {current_q.text} (True/False)?: ").title()
        self.check_answer(usr_answer, current_q.answer)

    def check_answer(self, usr_answer, correct_answer):
        if usr_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right.")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"You're current score is {self.score}/{self.q_number}")
        print("\n")
