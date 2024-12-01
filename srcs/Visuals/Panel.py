from abc import ABC , abstractmethod

class Panel(ABC):
    def __init__(self,screen):
        self.screen = screen
    @abstractmethod
    def handle_mouse_motion(self,event):
        pass
    @abstractmethod
    def handle_click(self, pos, button):
        pass
    @abstractmethod
    def handle_key(self,event):
        pass
    @abstractmethod
    def draw(self):
        pass
    def getScreen(self):
        return self.screen

    def updateScreen(self,screen):
        self.screen = screen
