import pygame

from srcs.Comandos.Command import Command
from srcs.Visuals.Panel import Panel
from srcs.Visuals.ProxyPanel import ProxyPanel


class CommandCambiarPanel(Command):
    def __init__(self,panel: Panel,proxy : ProxyPanel):
        self.panel = panel
        self.proxy = proxy

    def setPanel(self,panel:Panel):
        self.panel = panel

    def execute(self) -> None:
        self.proxy.ponerTarget(self.panel)

class CommandReturnInicio(Command):
    def __init__(self,proxy : ProxyPanel,screen):
        self.proxy = proxy
        self.screen = screen
    def execute(self) -> None:
        self.screen = self.screen = pygame.display.set_mode((1000, 650))
        self.proxy.cambiarTarget(0)