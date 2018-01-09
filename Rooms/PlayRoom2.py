from GameFrame import Level
from Objects import Insect
from GameFrame import Globals


class PlayRoom2(Level):
    def __init__(self, screen):
        Level.__init__(self, screen)

        self.set_background_image('bricks.png')
        self.splat_sound = self.load_sound('Splat.wav')

        self.splat_image = self.load_image('splat.png')
        self.ant_image = self.load_image('ant_32x32.png')
        self.roach_image = self.load_image('cockroach_32x32.png')
        self.scorpion_image = self.load_image('scorpion_32x32.png')
        self.spider_image = self.load_image('spider_32x32.png')

        self.set_timer(60, self.add_ant)
        self.set_timer(120, self.add_roach)
        self.set_timer(180, self.add_scorpion)
        self.set_timer(240, self.add_spider)

        self.set_timer(1200, self.times_up)

    def add_ant(self):
        if Globals.num_ants < 2:
            Globals.num_ants += 1
            self.add_room_object(Insect(self, 0, 0, self.splat_sound, self.ant_image, self.splat_image, 3, 25))
            self.set_timer(120, self.add_ant)

    def add_roach(self):
        if Globals.num_roaches < 3:
            Globals.num_roaches += 1
            self.add_room_object(Insect(self, 0, 0, self.splat_sound, self.roach_image, self.splat_image, 4, 50))
            self.set_timer(240, self.add_roach)

    def add_scorpion(self):
        if Globals.num_scorpions < 2:
            Globals.num_roaches += 1
            self.add_room_object(Insect(self, 0, 0, self.splat_sound, self.scorpion_image, self.splat_image, 5, 75))
            self.set_timer(120, self.add_scorpion)

    def add_spider(self):
        if Globals.num_spiders < 1:
            Globals.num_spiders += 1
            self.add_room_object(Insect(self, 0, 0, self.splat_sound, self.spider_image, self.splat_image, 7, 100))
            self.set_timer(40, self.add_spider)

    def times_up(self):
        Globals.num_ants = 0
        Globals.num_roaches = 0
        Globals.num_scorpions = 0
        Globals.num_spiders = 0
        self.running = False
