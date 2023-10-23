import random

import pygame

from States.Application.ExitApplication import *
from Game.RockObject import *


class UpdateApplication(AbstractState):

    @property
    def machine(self) -> AbstractMachine:
        return self.__state_machine

    @machine.setter
    def machine(self, value: AbstractMachine):
        self.__state_machine = value

    def __init__(self):
        self.__state_machine = None
        self.updating = False
        self.fps = pygame.time.Clock()

    def on_enter(self):
        self.updating = True
        return self.update()

    def on_exit(self):
        self.updating = False
        return

    def update(self):

        l = list()
        group = pygame.sprite.Group()
        for x in range(50):
            r = RockObject("rock", "Textures/rock.png")
            l.append(r)
           # r.position = (random.uniform(-300, 300), random.uniform(-200, 200))
            r.position = (0, 0)
            r.scale = (0.2, 0.2)
            group.add(r)

        while self.updating:
            dt = self.fps.tick(30) / 1000

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.machine.change_state(ExitApplication())

            group.update(dt)

            Screen.instance().surface.fill((0, 0, 0, 255))

            group.draw(Screen.instance().surface)
            pygame.display.update()
        return
