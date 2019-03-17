from GameFrame import TextObject, Globals
import pygame


class NameText(TextObject):
    def __init__(self, room, x, y):
        TextObject.__init__(self, room, x, y, '')

        self.handle_key_events = True

        self.accepting_input = True

    def accept_input(self):
        self.accepting_input = True

    def key_pressed(self, key):
        if self.accepting_input:
            self.accepting_input = False
            self.set_timer(20, self.accept_input)

            if key[pygame.K_a]:
                self.text += 'A'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_b]:
                self.text += 'B'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_c]:
                self.text += 'C'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_d]:
                self.text += 'D'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_e]:
                self.text += 'E'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_f]:
                self.text += 'F'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_g]:
                self.text += 'G'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_h]:
                self.text += 'H'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_i]:
                self.text += 'I'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_j]:
                self.text += 'J'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_k]:
                self.text += 'K'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_l]:
                self.text += 'L'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_m]:
                self.text += 'M'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_n]:
                self.text += 'N'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_o]:
                self.text += 'O'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_p]:
                self.text += 'P'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_q]:
                self.text += 'Q'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_r]:
                self.text += 'R'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_s]:
                self.text += 'S'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_t]:
                self.text += 'T'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_u]:
                self.text += 'U'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_v]:
                self.text += 'V'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_w]:
                self.text += 'W'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_x]:
                self.text += 'X'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_y]:
                self.text += 'Y'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_z]:
                self.text += 'Z'
                self.update_text()
                Globals.player_name = self.text
            elif key[pygame.K_SPACE]:
                self.text += ' '
                self.update_text()
                Globals.player_name = self.text
