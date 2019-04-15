class Setting():
    """A class for setting of game"""

    def __init__(self):
        # initalize the game setting
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)  # Green
        self.ship_speed = 2
        self.alien_speed = 0.5
        self.bullet_speed = 0.6
        self.max_lives = 3
