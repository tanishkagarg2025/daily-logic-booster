import tkinter as tk


class SettingsScreen(tk.Frame):

    def __init__(self, parent, controller, question, theme, progress):
        super().__init__(parent, bg=theme.get("bg"))

        self.controller = controller
        self.theme = theme

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Center Card
        card = tk.Frame(
            self,
            bg=theme.get("card_bg", theme.get("bg"))
        )
        card.grid(row=0, column=0, padx=200, pady=100, sticky="nsew")

        # Title
        tk.Label(
            card,
            text="⚙ Settings",
            font=("Helvetica", 28, "bold"),
            bg=theme.get("card_bg"),
            fg=theme.get("fg")
        ).pack(pady=30)

        # ---------------- THEME ----------------
        tk.Label(
            card,
            text="Select Theme:",
            bg=theme.get("card_bg"),
            fg=theme.get("fg"),
            font=("Helvetica", 14)
        ).pack()

        self.selected_theme = tk.StringVar(
            value=controller.theme_manager.current_theme
        )

        tk.OptionMenu(
            card,
            self.selected_theme,
            *controller.theme_manager.get_theme_names()
        ).pack(pady=10)

        # ---------------- DIFFICULTY ----------------
        tk.Label(
            card,
            text="Select Difficulty:",
            bg=theme.get("card_bg"),
            fg=theme.get("fg"),
            font=("Helvetica", 14)
        ).pack()

        self.selected_difficulty = tk.StringVar(value="Hard")

        tk.OptionMenu(
            card,
            self.selected_difficulty,
            "Easy",
            "Hard"
        ).pack(pady=10)

        # ---------------- CATEGORY ----------------
        tk.Label(
            card,
            text="Select Category:",
            bg=theme.get("card_bg"),
            fg=theme.get("fg"),
            font=("Helvetica", 14)
        ).pack()

        self.selected_category = tk.StringVar(value="Mixed Mode")

        tk.OptionMenu(
            card,
            self.selected_category,
            "DSA",
            "Probability",
            "Recursion",
            "OOPS",
            "Logical Puzzles",
            "Mixed Mode"
        ).pack(pady=10)

        # ---------------- BUTTONS ----------------
        tk.Button(
            card,
            text="Apply Settings",
            bg=theme.get("button_bg"),
            fg=theme.get("button_fg"),
            command=self.apply_settings
        ).pack(pady=20)

        tk.Button(
            card,
            text="Back to Home",
            bg=theme.get("button_bg"),
            fg=theme.get("button_fg"),
            command=lambda: controller.fade_to("HomeScreen")
        ).pack(pady=10)

    # ------------------------------------------------

    def apply_settings(self):

        # Update theme
        new_theme = self.selected_theme.get()
        self.controller.theme_manager.set_theme(new_theme)

        # Save difficulty & category inside controller
        self.controller.selected_difficulty = self.selected_difficulty.get()
        self.controller.selected_category = self.selected_category.get()

        # Regenerate question
        from question_generator import generate_question

        self.controller.question = generate_question(
            self.controller.selected_category,
            self.controller.selected_difficulty
        )

        # Refresh UI
        self.controller.refresh_app()