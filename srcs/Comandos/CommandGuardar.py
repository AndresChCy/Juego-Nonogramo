from srcs.Comandos.Command import Command
from srcs.Logica.Dibujo import Dibujo
from srcs.Logica.Tablero import Tablero


class CommandGuardar(Command):
    def __init__(self,dibujo: Dibujo):
        self.dibujo = dibujo

    def execute(self) -> None:
        tab = Tablero(self.dibujo)
        tab.guardarProgreso(self.dibujo.getProgreso(), "../../Niveles/nivel1")