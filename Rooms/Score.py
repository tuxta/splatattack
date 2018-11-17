from GameFrame import Level
from GameFrame import Globals
from GameFrame import TextObject


class Score(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image('ladybug_background.png')

        self.add_room_object(TextObject(self, 200, 200, 'Score'))
        self.add_room_object(TextObject(self, 250, 400, str(Globals.SCORE)))

        self.set_timer(150, self.endgame)

    def endgame(self):
        self.running = False
