from GameFrame import Level
from GameFrame import TextObject
from Objects import PlayButton
from Objects import NameText


class EnterName(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image('ladybug_background.png')
        self.add_room_object(TextObject(self, 150, 50, 'Type your name', 80))

        self.add_room_object(NameText(self, 200, 200))

        self.play_button = PlayButton(self, -300, 400)
        self.add_room_object(self.play_button)

    def valid_name(self):
        self.play_button.x = 300

    def invalid_name(self):
        print('Move Play Button')
        self.play_button.x = 1000
