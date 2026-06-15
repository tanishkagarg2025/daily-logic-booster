import tkinter as tk


class Dashboard(tk.Frame):

    def __init__(self, parent, controller, question, theme, progress):
        super().__init__(parent, bg=theme.get("bg"))

        self.controller = controller
        self.theme = theme
        self.progress = progress

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Center card
        card = tk.Frame(self,
                        bg=theme.get("card_bg", theme.get("bg")))
        card.grid(row=0, column=0, padx=200, pady=100, sticky="nsew")

        tk.Label(card,
                 text="📊 Dashboard",
                 font=("Helvetica", 28, "bold"),
                 bg=theme.get("card_bg"),
                 fg=theme.get("fg")).pack(pady=30)

        tk.Label(card,
                 text=f"Level: {progress['level']}",
                 font=("Helvetica", 18),
                 bg=theme.get("card_bg"),
                 fg=theme.get("fg")).pack(pady=10)

        tk.Label(card,
                 text=f"XP: {progress['xp']}",
                 font=("Helvetica", 18),
                 bg=theme.get("card_bg"),
                 fg=theme.get("fg")).pack(pady=10)

        tk.Label(card,
                 text=f"Streak: {progress['streak']} days 🔥",
                 font=("Helvetica", 18),
                 bg=theme.get("card_bg"),
                 fg=theme.get("fg")).pack(pady=10)

        tk.Button(card,
                  text="Back to Home",
                  bg=theme.get("button_bg"),
                  fg=theme.get("button_fg"),
                  command=lambda: controller.fade_to("HomeScreen")
                  ).pack(pady=30)