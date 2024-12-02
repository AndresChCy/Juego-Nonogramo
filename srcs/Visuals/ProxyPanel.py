from srcs.Visuals.Panel import Panel


class ProxyPanel(Panel):
    def __init__(self,panelList: list):
        if panelList:
            self.target = panelList[0]
        else:
            self.target = None
        self.panelList = panelList

    def cambiarTarget(self, num):
        self.target = self.panelList[num]

    def addToList(self, panel: Panel):
        self.panelList.append(panel)
        if len(self.panelList) == 1:
            self.target = self.panelList[0]

    def ponerTarget(self,panel: Panel):
        self.target = panel

    def handle_mouse_motion(self,pos):
        self.target.handle_mouse_motion(pos)

    def handle_click(self, pos, button, soundManager):
        self.target.handle_click( pos, button, soundManager)

    def handle_key(self, event):
        self.target.handle_key( event)

    def draw(self):
        self.target.draw()