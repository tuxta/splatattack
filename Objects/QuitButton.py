from GameFrame import RoomObject
from GameFrame import Globals


class QuitButton(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        button_image = self.load_image('Quit_Button.png')
        self.set_image(button_image, 150, 150)

        self.handle_mouse_events = True

    def clicked(self, button_number):
        self.room.running = False
        Globals.exiting = True
