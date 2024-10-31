from srcs.Visuals.Panel import Panel


class DecoratorGrilla(Panel):

    def __init__(self, component: Panel) -> None:
        self._component = component

    @property
    def component(self) -> Panel:
        return self._component

    def draw(self):
        self._component.draw()

    def handle_mouse_motion(self, event):
        self._component.handle_mouse_motion(event)

    def handle_click(self, pos, button):
        self._component.handle_click( pos, button)

    def handle_key(self, event):
        self._component.handle_key(event)

class DecoratorClues(DecoratorGrilla):
    def draw(self):
        self._component.draw()
