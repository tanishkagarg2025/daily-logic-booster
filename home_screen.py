import tkinter as tk
from tkinter import ttk

class HomeScreen(tk.Frame):

    def __init__(self, parent, controller, question, theme, progress):
        super().__init__(parent, bg=theme.get("bg"))

        self.controller = controller
        self.theme = theme
        self.progress = progress
        self.question = question

        # Make full screen responsive
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ---- Center Card ----
        card = tk.Frame(self,
                        bg=theme.get("card_bg"),
                        bd=0,
                        highlightthickness=0)
        card.grid(row=0, column=0, padx=200, pady=80, sticky="nsew")

        card.grid_rowconfigure(3, weight=1)
        card.grid_columnconfigure(0, weight=1)

        # Title
        tk.Label(card,
                 text="Daily Logic Booster",
                 font=("Helvetica", 28, "bold"),
                 bg=theme.get("card_bg"),
                 fg=theme.get("fg")).grid(row=0, column=0, pady=20)

        # XP Progress Bar
        self.progress_bar = ttk.Progressbar(
            card,
            orient="horizontal",
            length=400,
            mode="determinate"
        )
        self.progress_bar.grid(row=1, column=0, pady=10)
        self.update_progress_bar()

        # Question
        tk.Label(card,
                 text=question["text"],
                 wraplength=900,
                 justify="center",
                 font=("Helvetica", 18),
                 bg=theme.get("card_bg"),
                 fg=theme.get("fg")).grid(row=2, column=0, pady=20)

        # Answer box
        self.answer_box = tk.Text(
            card,
            height=5,
            font=("Helvetica", 16),
            bg="white",
            fg="black"
        )
        self.answer_box.grid(row=3, column=0, sticky="nsew", padx=150, pady=20)

        # Buttons
        btn_frame = tk.Frame(card, bg=theme.get("card_bg"))
        btn_frame.grid(row=4, column=0, pady=20)

        tk.Button(btn_frame,
                  text="Submit",
                  bg=theme.get("button_bg"),
                  fg=theme.get("button_fg"),
                  command=self.check_answer).pack(side="left", padx=10)

        tk.Button(btn_frame,
                  text="Solution",
                  bg=theme.get("button_bg"),
                  fg=theme.get("button_fg"),
                  command=self.show_solution).pack(side="left", padx=10)

        tk.Button(btn_frame,
                  text="Dashboard",
                  bg=theme.get("button_bg"),
                  fg=theme.get("button_fg"),
                  command=lambda: controller.fade_to("Dashboard")).pack(side="left", padx=10)

        # Feedback
        self.feedback_label = tk.Label(card,
                                       text="",
                                       font=("Helvetica", 16),
                                       bg=theme.get("card_bg"))
        self.feedback_label.grid(row=5, column=0)

        self.solution_label = tk.Label(card,
                                       text="",
                                       wraplength=900,
                                       font=("Helvetica", 15),
                                       fg="#90EE90",
                                       bg=theme.get("card_bg"))
        self.solution_label.grid(row=6, column=0)

    # ------------------------

    def update_progress_bar(self):
        xp = self.progress["xp"]
        self.progress_bar["maximum"] = 100
        self.progress_bar["value"] = xp % 100

    def check_answer(self):
        user = self.answer_box.get("1.0", "end").strip().lower()
        correct = self.question["solution"].strip().lower()

        if user in correct:
            self.feedback_label.config(text="✅ Correct! +10 XP",
                                       fg="#90EE90")
            self.controller.progress_manager.add_xp(10)
            self.animate_xp()
        else:
            self.feedback_label.config(text="❌ Try again!",
                                       fg="red")

    def animate_xp(self):
        current = self.progress_bar["value"]
        target = (self.progress["xp"] % 100)

        if current < target:
            self.progress_bar["value"] = current + 1
            self.after(10, self.animate_xp)

    def show_solution(self):
        self.solution_label.config(text=self.question["solution"])