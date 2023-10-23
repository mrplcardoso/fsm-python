import sys
import pygame
from pygame.locals import *
from FSM.AbstractStateMachine import *
from Controllers.Screen import Screen


class ExitApplication(AbstractState):

    @property
    def machine(self) -> AbstractMachine:
        return self.__state_machine

    @machine.setter
    def machine(self, value: AbstractMachine):
        self.__state_machine = value

    def __init__(self):
        self.__state_machine = None

    def on_enter(self):
        pygame.quit()
        sys.exit()
        pass

    def on_exit(self):
        pass

    def update(self):
        pass
