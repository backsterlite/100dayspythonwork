from quiz_brain import QuizBrain
from data import question_data
from question_model import Question
from quiz_ui import QuizInterface

question_list = []
for question in question_data:
    question_list.append(Question(question['question'], question['correct_answer']))

quiz = QuizBrain(question_list)
qi = QuizInterface(quiz)
# while quiz.still_has_question():
#     quiz.next_question()
#
# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
