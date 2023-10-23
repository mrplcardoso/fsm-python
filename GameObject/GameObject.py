import abc
from abc import ABC
import random

import pygame.sprite


class GameObject(pygame.sprite.Sprite):

    @property
    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def start(self):
        return

    @abc.abstractmethod
    def update(self, dt):
        return
