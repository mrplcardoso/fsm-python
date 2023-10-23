from States.Application.UpdateApplication import *


class StartApplication(AbstractState):

    @property
    def machine(self) -> AbstractMachine:
        return self.__state_machine

    @machine.setter
    def machine(self, value: AbstractMachine):
        self.__state_machine = value

    def __init__(self, name, screen_size: tuple):
        self.__state_machine = None
        self.screen_size = screen_size
        self.running = False
        self.name = name
        return

    def on_enter(self):
        pygame.init()
        Screen.instance().surface = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption(self.name)

        self.machine.change_state(UpdateApplication())
        return

    def on_exit(self):
        pass

    def update(self):
        pass
