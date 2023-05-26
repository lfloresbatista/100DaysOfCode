from question_model import Question
from data import question_data
from quiz_brain import  QuizBrain


question_bank = []
for x in question_data:
    q_text = x["question"]
    q_answer = x["correct_answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")