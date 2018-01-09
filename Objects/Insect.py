from GameFrame import RoomObject
from GameFrame import Globals
import random


class Insect(RoomObject):
    def __init__(self, room, x, y, splat_sound, insect_image, splat_image, speed, points):
        RoomObject.__init__(self, room, x, y)

        self.splat_sound = splat_sound
        self.insect_image = insect_image
        self.splat_image = splat_image
        self.set_image(self.insect_image, 32, 32)
        self.speed = speed
        self.points = points
        self.reset()

        self.alive = True

        self.handle_mouse_events = True

    def step(self):
        if self.y > Globals.SCREEN_HEIGHT:
            self.reset()

    def reset(self):
        self.set_direction(90, self.speed)
        self.y = -(random.randint(self.height, 200 + self.height))
        self.x = random.randint(0, Globals.SCREEN_WIDTH - self.width)
        self.set_image(self.insect_image, 32, 32)

    def clicked(self, button_number):
        if self.alive:
            self.set_image(self.splat_image, 32, 32)
            self.set_direction(90, 0)
            Globals.SCORE += 25
            self.set_timer(45, self.squashed)
            self.splat_sound.play()
        self.alive = False

    def squashed(self):
        self.reset()
        self.alive = True
