from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

q_bank = []
for i in question_data:
    q_answer = i["answer"]
    q_text = i["text"]
    new_q = Question(q_text, q_answer)
    q_bank.append(new_q)

q = QuizBrain(q_bank)
while q.still_have_questions() is not False:
    q.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {q.score}/{q.q_number}")