import abc
from abc import ABC


class AbstractState(ABC):

    @property
    @abc.abstractmethod
    def machine(self):
        pass

    @machine.setter
    @abc.abstractmethod
    def machine(self, value):
        pass

    @abc.abstractmethod
    def on_enter(self):
        return

    @abc.abstractmethod
    def on_exit(self):
        return

    @abc.abstractmethod
    def update(self):
        return


class AbstractMachine(ABC):

    @property
    @abc.abstractmethod
    def states(self) -> set:
        pass

    @property
    @abc.abstractmethod
    def running_state(self) -> AbstractState:
        pass

    @running_state.setter
    def running_state(self, value: AbstractState):
        self.running_state = value

    @property
    @abc.abstractmethod
    def in_transition(self) -> bool:
        pass

    def add_state(self, state: AbstractState):
        if not(state in self.states):
            self.states.add(state)
            state.machine = self
        return

    def change_state(self, state: AbstractState):
        if not(state in self.states):
            self.add_state(state)

        if not self.running_state:
            self.running_state.on_exit()

        self.running_state = state

        self.running_state.on_enter()
        return
