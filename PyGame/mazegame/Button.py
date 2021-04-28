import pygame

class Button:
    def __init__(self, rect):
        self.buttonrect = pygame.Rect(rect)
        self.buttonimage = pygame.Surface(self.buttonrect.size).convert()
        self.buttoncolorneutral = (0,150,0)
        self.buttoncolorhovered = (0,200,0)
        self.buttonfont = pygame.font.SysFont('Arial', 40)
        self.buttontext = self.buttonfont.render("Go!",True,(255, 255, 255))
        self.buttontextlocation = self.buttontext.get_rect(center=self.buttonrect.center)

    def mouse_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return self.mouse_clicked_button(event)
        else:
            return False

    def mouse_clicked_button(self, event):
        if self.buttonrect.collidepoint(event.pos):
            return True
            print("True")
        else:
            return False

    def render(self, display):
        self.buttonimage.fill(self.buttoncolorneutral)
        display.blit(self.buttonimage, self.buttonrect)
        display.blit(self.buttontext, self.buttontextlocation)
