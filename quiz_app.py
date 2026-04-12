import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

# ---------------- LOAD QUESTIONS ----------------
def load_questions(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    blocks = [b.strip() for b in content.split("\n---") if b.strip()]
    questions = []
    
    for block in blocks:
        lines = [line.strip() for line in block.split("\n") if line.strip()]
        
        q_data = {"question": "", "options": {}, "answer": "", "explanation": ""}
        
        for line in lines:
            if line.startswith("Question:"):
                q_data["question"] = line.replace("Question:", "").strip()
            elif line.startswith("A:"):
                q_data["options"]["A"] = line.replace("A:", "").strip()
            elif line.startswith("B:"):
                q_data["options"]["B"] = line.replace("B:", "").strip()
            elif line.startswith("C:"):
                q_data["options"]["C"] = line.replace("C:", "").strip()
            elif line.startswith("D:"):
                q_data["options"]["D"] = line.replace("D:", "").strip()
            elif line.startswith("Answer:"):
                q_data["answer"] = line.replace("Answer:", "").strip()
            elif line.startswith("Explanation:"):
                q_data["explanation"] = line.replace("Explanation:", "").strip()
        
        if q_data["question"] and len(q_data["options"]) == 4:
            questions.append(q_data)
    
    return questions


# ---------------- MAIN APP ----------------
class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.root.title("Quantitative Aptitude Practice Application")
        self.root.state('zoomed')
        
        # Background
        self.bg_image = Image.open("bg.jpg")
        self.bg_image = self.bg_image.resize(
            (self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        )
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.all_questions = questions
        self.show_start_screen()
    
    # ---------------- START SCREEN ----------------
    def show_start_screen(self):
        for widget in self.root.winfo_children():
            if widget != self.bg_label:
                widget.destroy()
        
        container = tk.Frame(self.root,bg="#000000" )
        container.place(relx=0.5, rely=0.3, anchor="center")
        
        tk.Label(container, text="Quantitative Aptitude Practice Application",
                 font=("Arial", 36, "bold"),
                 fg="white", bg="#000000").pack(pady=20)
        
        tk.Label(container, text="Select Difficulty",
                 font=("Arial", 18),
                 fg="white", bg="#000000").pack(pady=10)
        
        btn_frame = tk.Frame(container, bg="#000000")
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="Easy", width=10,
                  command=lambda: self.start_quiz("easy")).grid(row=0, column=0, padx=15)
        
        tk.Button(btn_frame, text="Medium", width=10,
                  command=lambda: self.start_quiz("medium")).grid(row=0, column=1, padx=15)
        
        tk.Button(btn_frame, text="Hard", width=10,
                  command=lambda: self.start_quiz("hard")).grid(row=0, column=2, padx=15)
    
    # ---------------- START QUIZ ----------------
    def start_quiz(self, level):
        for widget in self.root.winfo_children():
            if widget != self.bg_label:
                widget.destroy()
        
        if level == "easy":
            self.questions = random.sample(self.all_questions, min(5, len(self.all_questions)))
            self.time_left = 60
        elif level == "medium":
            self.questions = random.sample(self.all_questions, min(10, len(self.all_questions)))
            self.time_left = 60
        else:
            self.questions = random.sample(self.all_questions, min(20, len(self.all_questions)))
            self.time_left = 80
        
        self.q_index = 0
        self.answers = {}
        self.score = 0
        
        self.main_frame = tk.Frame(self.root, bg="#ffffff")
        self.main_frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)
        
        self.selected_option = tk.StringVar()
        
        self.question_label = tk.Label(self.main_frame, font=("Arial", 20, "bold"),
                                       bg="#ffffff", wraplength=1000)
        self.question_label.pack(pady=20)
        
        self.timer_label = tk.Label(self.main_frame, font=("Arial", 14),
                                    fg="red", bg="#ffffff")
        self.timer_label.pack()
        
        self.progress = ttk.Progressbar(self.main_frame, length=400)
        self.progress.pack(pady=10)
        
        self.progress_label = tk.Label(self.main_frame, bg="#ffffff")
        self.progress_label.pack()
        
        center_frame = tk.Frame(self.main_frame, bg="#ffffff")
        center_frame.pack(expand=True)
        
        self.options_frame = tk.Frame(center_frame, bg="#ffffff")
        self.options_frame.pack()
        
        self.radio_buttons = {}
        for opt in ["A","B","C","D"]:
            rb = tk.Radiobutton(
                self.options_frame,
                text="",
                variable=self.selected_option,
                value=opt,
                font=("Arial", 16, "bold"),
                bg="#ffffff",
                anchor="w",
                padx=20,
                pady=10
            )
            rb.pack(pady=5)
            self.radio_buttons[opt] = rb
        
        btn_frame = tk.Frame(self.main_frame, bg="#ffffff")
        btn_frame.pack(fill="x", pady=20)
        
        self.prev_button = tk.Button(btn_frame, text="Previous", command=self.prev_question)
        self.prev_button.pack(side="left", padx=40)
        
        self.next_button = tk.Button(btn_frame, text="Next", command=self.next_question)
        self.next_button.pack(side="right", padx=40)
        
        self.submit_button = tk.Button(btn_frame, text="Submit",
                                       bg="#4CAF50", fg="white",
                                       command=self.submit_quiz)
        
        self.load_question()
        self.update_timer()
    
    def load_question(self):
        q = self.questions[self.q_index]
        self.question_label.config(text=f"Q{self.q_index+1}: {q['question']}")
        
        for opt in ["A","B","C","D"]:
            self.radio_buttons[opt].config(text=f"{opt}: {q['options'][opt]}")
        
        self.selected_option.set(self.answers.get(self.q_index, ""))
        
        self.progress["value"] = ((self.q_index+1)/len(self.questions))*100
        self.progress_label.config(text=f"{self.q_index+1}/{len(self.questions)}")
        
        if self.q_index == len(self.questions)-1:
            self.next_button.pack_forget()
            self.submit_button.pack(side="right", padx=40)
        else:
            self.submit_button.pack_forget()
            self.next_button.pack(side="right", padx=40)
    
    def save_answer(self):
        if self.selected_option.get():
            self.answers[self.q_index] = self.selected_option.get()
    
    def next_question(self):
        self.save_answer()
        if self.q_index < len(self.questions)-1:
            self.q_index += 1
            self.load_question()
    
    def prev_question(self):
        self.save_answer()
        if self.q_index > 0:
            self.q_index -= 1
            self.load_question()
    
    def update_timer(self):
        self.timer_label.config(text=f"⏱️ {self.time_left}s")
        
        if self.time_left > 0:
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.submit_quiz()
    
    def submit_quiz(self):
        self.save_answer()
        self.score = sum(1 for i,q in enumerate(self.questions)
                         if self.answers.get(i)==q["answer"])
        self.show_result()
    
    # ---------------- FIXED RESULT ----------------
    def show_result(self):
        for widget in self.root.winfo_children():
            if widget != self.bg_label:
                widget.destroy()
        
        self.main_frame = tk.Frame(self.root, bg="#ffffff")
        self.main_frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)
        
        tk.Label(self.main_frame,
                 text=f"Score: {self.score}/{len(self.questions)}",
                 font=("Arial", 24, "bold"),
                 bg="#ffffff").pack(pady=10)
        
        # 🔥 REVIEW AREA (FIXED)
        review_container = tk.Frame(self.main_frame, bg="#ffffff")
        review_container.pack(fill="both", expand=True)
        
        canvas = tk.Canvas(review_container, bg="#ffffff")
        scrollbar = tk.Scrollbar(review_container, command=canvas.yview)
        review_frame = tk.Frame(canvas, bg="#ffffff")
        
        review_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=review_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        for i,q in enumerate(self.questions):
            ua = self.answers.get(i,"Not Answered")
            correct = q["answer"]
            
            frame = tk.Frame(review_frame, bg="#ffffff", bd=1, relief="solid")
            frame.pack(fill="x", pady=5, padx=20)
            
            tk.Label(frame,text=f"Q{i+1}: {q['question']}",wraplength=900,
                     bg="#ffffff",font=("Arial",12,"bold")).pack(anchor="w")
            
            tk.Label(frame,text=f"Your Answer: {ua}",bg="#ffffff").pack(anchor="w")
            tk.Label(frame,text=f"Correct Answer: {correct}",bg="#ffffff").pack(anchor="w")
            
            if ua==correct:
                tk.Label(frame,text="✅ Correct",fg="green",bg="#ffffff").pack(anchor="w")
            else:
                tk.Label(frame,text="❌ Wrong",fg="red",bg="#ffffff").pack(anchor="w")
            
            tk.Label(frame,text=f"Explanation: {q['explanation']}",
                     wraplength=900,bg="#ffffff").pack(anchor="w")
        
        # 🔥 BOTTOM BUTTON
        tk.Button(self.main_frame,
                  text="🔁 Restart Quiz",
                  font=("Arial", 16, "bold"),
                  bg="#2ecc71",
                  fg="white",
                  command=self.show_start_screen).pack(pady=10)


# ---------------- RUN ----------------
if __name__ == "__main__":
    root = tk.Tk()
    questions = load_questions("questions.txt")
    app = QuizApp(root, questions)
    root.mainloop()