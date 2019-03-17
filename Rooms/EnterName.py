from GameFrame import Level
from GameFrame import TextObject
from Objects import PlayButton
from Objects import NameText


class EnterName(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image('ladybug_background.png')

        self.add_room_object(TextObject(self, 150, 50, 'Type your name', 80))
        self.add_room_object(NameText(self, 250, 200))

        self.add_room_object(PlayButton(self, 300, 400))
