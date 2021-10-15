from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(350, 400)
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="#fff", font=("Arial", 10))
        self.score.grid(column=1, row=0)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="#fff", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # canvas text
        self.question_text = self.canvas.create_text(150,125 , text="Amazon acquired Twitch in Auguest....", fill="black", font=("Arial", 20, "italic"),  width=280)

        # buttons
        false_image = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_image, highlightthickness=0, command=self.false)
        self.false_btn.grid(column=1, row=2)

        true_image = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_image, highlightthickness=0, command=self.true)
        self.true_btn.grid(column=0, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score.config(text=f"Score:{self.quiz.score}")
            q_text =self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true(self):

        self.give_feedback(self.quiz.check_answer("True"))

    def false(self):

        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question )