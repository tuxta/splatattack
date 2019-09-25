from GameFrame import Level, EntryTextObject
from GameFrame import TextObject
from Objects import PlayButton


class EnterName(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image('ladybug_background.png')
        self.add_room_object(TextObject(self, 150, 50, 'Type your name', 80))

        self.name_text = EntryTextObject(self, 200, 200, 10)
        self.add_room_object(self.name_text)

        self.play_button = PlayButton(self, -300, 400)
        self.add_room_object(self.play_button)

        self.set_timer(10, self.check_valid_name)

    def check_valid_name(self):
        if len(self.name_text.text) > 1:
            self.play_button.x = 300
        else:
            self.play_button.x = 1000
        self.set_timer(10, self.check_valid_name)
