class ThemeManager:

    def __init__(self):
        self.themes = {

            "Deep Ocean Blue": {
                "bg": "#001f3f",          # Main background
                "card_bg": "#003366",     # Card background
                "fg": "white",            # Text color
                "button_bg": "#3399ff",   # Button background
                "button_fg": "black"      # Button text
            },

            "Dark Grey": {
                "bg": "#121212",
                "card_bg": "#1e1e1e",
                "fg": "white",
                "button_bg": "#bb86fc",
                "button_fg": "black"
            },

            "Pure Black": {
                "bg": "#000000",
                "card_bg": "#111111",
                "fg": "white",
                "button_bg": "#ff9800",
                "button_fg": "black"
            }

        }

        self.current_theme = "Deep Ocean Blue"

    # ----------------------------------

    def get_theme(self):
        """
        Returns the currently selected theme dictionary.
        """
        return self.themes.get(self.current_theme)

    # ----------------------------------

    def set_theme(self, theme_name):
        """
        Change the theme if it exists.
        """
        if theme_name in self.themes:
            self.current_theme = theme_name

    # ----------------------------------

    def get_theme_names(self):
        """
        Returns list of available theme names.
        """
        return list(self.themes.keys())