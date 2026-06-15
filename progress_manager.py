class ProgressManager:

    def __init__(self):
        self.progress = {
            "level": 1,
            "xp": 0,
            "streak": 0
        }

    # ---------------------------------

    def get_progress(self):
        """
        Returns current progress dictionary
        """
        return self.progress

    # ---------------------------------

    def add_xp(self, amount):
        """
        Adds XP and handles level up
        """
        self.progress["xp"] += amount

        # Level up every 100 XP
        while self.progress["xp"] >= 100:
            self.progress["xp"] -= 100
            self.progress["level"] += 1

    # ---------------------------------

    def increase_streak(self):
        """
        Increase streak count
        """
        self.progress["streak"] += 1