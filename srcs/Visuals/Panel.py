from abc import ABC , abstractmethod

class Panel(ABC):
    @abstractmethod
    def handle_mouse_motion(self,event):
        pass
    @abstractmethod
    def handle_click(self, pos, button, soundManager):
        pass
    @abstractmethod
    def handle_key(self,event):
        pass
    @abstractmethod
    def draw(self):
        pass
