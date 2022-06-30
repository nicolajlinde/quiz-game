from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

q_bank = []
for i in question_data:
    q_answer = i["answer"]
    q_text = i["text"]
    new_q = Question(q_text, q_answer)
    q_bank.append(new_q)

quiz = QuizBrain(q_bank)
while quiz.still_have_questions() is not False:
    quiz.next_question()
