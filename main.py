import tkinter as tk

from theme_manager import ThemeManager
from progress_manager import ProgressManager
from question_generator import generate_question

from home_screen import HomeScreen
from dashboard import Dashboard
from settings_screen import SettingsScreen


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # Window setup
        self.title("Daily Logic Booster")
        self.state("zoomed")  # Full screen (Windows)
        self.minsize(1000, 700)

        # Fade support
        self.attributes("-alpha", 1.0)

        # Managers
        self.theme_manager = ThemeManager()
        self.progress_manager = ProgressManager()

        self.theme = self.theme_manager.get_theme()
        self.progress = self.progress_manager.get_progress()

        # Generate question
        self.question = generate_question("Mixed Mode", "Hard")

        # Container
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.container = container
        self.frames = {}

        self.create_frames()

        self.show_frame("HomeScreen")

    # ---------------------------------

    def create_frames(self):

        for F, name in [
            (HomeScreen, "HomeScreen"),
            (Dashboard, "Dashboard"),
            (SettingsScreen, "Settings")
        ]:

            frame = F(
                parent=self.container,
                controller=self,
                question=self.question,
                theme=self.theme,
                progress=self.progress
            )

            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    # ---------------------------------

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    # ---------------------------------

    def fade_to(self, page_name):

        self.attributes("-alpha", 0.0)

        def fade_in():
            alpha = self.attributes("-alpha")
            if alpha < 1:
                self.attributes("-alpha", alpha + 0.05)
                self.after(15, fade_in)

        self.show_frame(page_name)
        fade_in()

    # ---------------------------------

    def refresh_app(self):
        """
        Rebuild screens after theme change.
        """
        self.theme = self.theme_manager.get_theme()
        self.progress = self.progress_manager.get_progress()

        for frame in self.frames.values():
            frame.destroy()

        self.frames.clear()
        self.create_frames()
        self.show_frame("HomeScreen")


# -----------------------------------------

if __name__ == "__main__":
    app = App()
    app.mainloop()