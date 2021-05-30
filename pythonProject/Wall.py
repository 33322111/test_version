from LoadImage import load_image
import pygame as pg
import random


class Wall():
    def __init__(self):
        width, height = 800, 600
        self.angle = random.randint(0, 1)
        if self.angle == 0:
            self.picture = load_image("ladder_v.png")
        else:
            self.picture = load_image("ladder_h.png")

        self.rect = pg.Rect(
            random.randint(0, width - self.picture.get_rect().width),
            random.randint(0, height - self.picture.get_rect().height),
            self.picture.get_rect().width,
            self.picture.get_rect().height)
