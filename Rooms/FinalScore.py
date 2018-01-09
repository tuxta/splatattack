from GameFrame import Level
from GameFrame import Globals
from GameFrame import TextObject
from Objects import PlayButton


class FinalScore(Level):
    def __init__(self, screen):
        Level.__init__(self, screen)

        self.set_background_image('ladybug_background.png')

        self.add_room_object(TextObject(self, 200, 200, 'Final Score'))
        self.add_room_object(TextObject(self, 250, 250, str(Globals.SCORE)))
        self.add_room_object(PlayButton(self, 200, 350))

        Globals.SCORE = 0
