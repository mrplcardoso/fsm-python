import pygame

from States.Application.StartApplication import StartApplication
from FSM.AbstractStateMachine import *


class ApplicationController(AbstractMachine):

    def states(self) -> set:
        return self.states

    def in_transition(self) -> bool:
        return self._in_transition

    def running_state(self) -> AbstractState:
        return self._running_state

    def __init__(self):
        # machine initialization
        self.states = set()
        self._running_state = None
        self._in_transition = False
        return

    def start_application(self):
        self.change_state(StartApplication("Hello Game", (800, 600)))
        return
