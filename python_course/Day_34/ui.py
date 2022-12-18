from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class UI:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain

        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label=Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)

        self.canvas=Canvas(width=300,height=250)
        self.question_text=self.canvas.create_text(150,125,width=280,text="question",font=("Ariel",20,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        self.cross_img=PhotoImage(file="images/false.png")
        self.wrong=Button(image=self.cross_img,highlightthickness=0,command=self.false_pressed)
        self.wrong.grid(column=1,row=2)

        self.check_img=PhotoImage(file="images/true.png")
        self.right=Button(image=self.check_img,highlightthickness=0,command=self.true_pressed)
        self.right.grid(column=0,row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text,text="GAME OVER")
            self.wrong.config(state="disabled")
            self.right.config(state="disabled")

    def true_pressed(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)