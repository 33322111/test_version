from LoadImage import load_image
import pygame as pg
import random


class Ball():
    def __init__(self, tp):
        width, height = 800, 600
        if tp == 0:
            tp = random.randint(1, 3)

        if tp == 1:
            self.picture = load_image("red_ball.png", -1)
        elif tp == 2:
            self.picture = load_image("green_ball.png", -1)
        elif tp == 3:
            self.picture = load_image("blue_ball.png", -1)

        self.rect = pg.Rect(
            random.randint(0, width - self.picture.get_rect().width),
            random.randint(0, height - self.picture.get_rect().height),
            self.picture.get_rect().width,
            self.picture.get_rect().height)

        self.angle = random.randint(0, 360)
        self.speed = 4
