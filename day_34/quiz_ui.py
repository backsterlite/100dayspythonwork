from quiz_brain import QuizBrain
import tkinter as tk

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text="Score: 0", bg=THEME_COLOR, fg="white")

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.quiz_text = self.canvas.create_text(150, 125, width=280)

        true_image = tk.PhotoImage(file="./images/true.png")
        self.true_image = tk.Button(image=true_image, highlightthickness=0, command=self.press_true)

        false_image = tk.PhotoImage(file="./images/false.png")
        self.false_image = tk.Button(image=false_image, highlightthickness=0, command=self.press_false)

        self.score_label.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=15)
        self.true_image.grid(column=0, row=2)
        self.false_image.grid(column=1, row=2)

        self.next_question()

        self.window.mainloop()
    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz.")
            self.true_image.config(state="disabled")
            self.false_image.config(state="disabled")

    def press_true(self):
        self.process_result(self.quiz.check_answer("True"))

    def press_false(self):
        self.process_result(self.quiz.check_answer("False"))

    def process_result(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1500, self.next_question)


