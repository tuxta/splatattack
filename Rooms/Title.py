from GameFrame import Level
from Objects import PlayButton
from Objects import QuitButton


class Title(Level):
    def __init__(self, screen):
        Level.__init__(self, screen)

        self.set_background_image('title.png')

        self.add_room_object(PlayButton(self, 425, 100))
        self.add_room_object(QuitButton(self, 625, 100))
