import tkinter as tk

class DashboardScreen(tk.Frame):

    def __init__(self, parent, controller, theme, progress):
        super().__init__(parent, bg=theme.get("bg"))

        tk.Label(self,
                 text="Dashboard",
                 font=("Helvetica", 24, "bold"),
                 bg=theme.get("bg"),
                 fg=theme.get("fg")).pack(pady=20)

        tk.Label(self,
                 text=f"Level: {progress['level']}",
                 bg=theme.get("bg"),
                 fg=theme.get("fg")).pack()

        tk.Label(self,
                 text=f"XP: {progress['xp']}",
                 bg=theme.get("bg"),
                 fg=theme.get("fg")).pack()

        tk.Label(self,
                 text=f"Streak: {progress['streak']}",
                 bg=theme.get("bg"),
                 fg=theme.get("fg")).pack()

        tk.Button(self,
                  text="Back to Home",
                  bg=theme.get("button_bg"),
                  fg=theme.get("button_fg"),
                  command=lambda: controller.show_frame("Home")).pack(pady=20)