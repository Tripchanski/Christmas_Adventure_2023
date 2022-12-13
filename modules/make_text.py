import pygame
from modules.level_map import screen

class Text():
        def __init__(self, text, color, size):
            self.text = text
            self.color = color        
            self.font = pygame.font.SysFont('sans serif', size)

        def draw_text(self, counter):  
            img = self.font.render(self.text[counter], True, self.color)
            if counter % 2 == 0:
                screen.blit(img, (10,70))
            else:
                screen.blit(img, (10, 320))

text = Text(
    ["",
    "???: Здраствуйте, я эльф Олег.",
     "???: Здраствуй Олег, я Дед Мороз, для чего пришел?",
     "Олег: Помочь найти подарки.",
     "Дед Мороз: Хорошо, следуй за другими эльфами.",
     "Ahmed: Slam Oleg.",
     "Олег:Салам брам как твои дела."
    ], (0,0,0), 24)

