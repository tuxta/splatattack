from GameFrame import Level
from GameFrame import Globals
from GameFrame import TextObject
from GameFrame import DataBaseController


class HighScores(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image('ladybug_background.png')

        database = DataBaseController('game_data.sqlite')

        database.add_score(Globals.player_name, Globals.SCORE)
        names_scores = database.get_top_5()

        self.add_room_object(TextObject(self, 50, 10, 'Top 5 Scores', 80))
        y_pos = 150
        for person in names_scores:
            self.add_room_object(TextObject(self, 20, y_pos, person[0]))
            self.add_room_object(TextObject(self, 390, y_pos, str(person[1])))
            y_pos += 70

        self.set_timer(150, self.endgame)

    def endgame(self):
        Globals.SCORE = 0
        self.running = False
