from Question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for q in question_data:
    qtext=q["text"]
    qanswer=q["answer"]
    new_question=Question(qtext, qanswer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
quiz.final()