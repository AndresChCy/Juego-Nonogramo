from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass

    def __call__(self):
        self.execute()

class Ejecutador(Command):
    def __init__(self):
        self.commands = []

    def addCommand(self,command : Command):
        self.commands.append(command)

    def execute(self) -> None:
        for command in self.commands:
            command.execute()