import pygame
import sys

from pygame.constants import FULLSCREEN

from Grid import Grid
from Colores import Colores
from Menu import MenuPrincipal
from MenuNiveles import MenuNiveles
from Musica.SoundManager import SoundManager
from ProxyPanel import ProxyPanel
from srcs.Comandos.CommandAbrirMenu import CommandMenu
from srcs.Comandos.CommandCambiarPanel import CommandCambiarPanel
from srcs.Logica.Niveles import Niveles
from srcs.Visuals.Grilla.GrillaDecorator import DecoratorClues, DecoratorMiniatureRender
from srcs.Visuals.Grilla.GrillaVisual import GrillaVisual
from srcs.Visuals.ImageManager import ImageManager
from srcs.Visuals.MenuCrearNivel import CrearNivel
from srcs.Visuals.MenuDificultad import MenuDificultad
from srcs.Visuals.PanelMenu import Menu
from srcs.Visuals.SeleccionTipoNivel import SeleccionTipoNivel
from srcs.Visuals.Tutorial import mostrar_tutorial


class Window:
    def __init__(self, matrix):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 650))
        self.image_manager = ImageManager()
        self.image_manager.load_image("background", "Img/backgroun.jpg", scale=(1000, 700))
        # Cargar la imagen de fondo usando el ImageManager
        self.background_image = self.image_manager.get_image("background")
        self.screen.blit(self.background_image, (0, 0))
        #self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        pygame.display.set_caption('Nonograma')
        self.panel = ProxyPanel([])
        self.iniciarMusica()
        self.iniciarMenus()
        #cuadricula = Grid(self.screen, matrix,self.panel)
        #niveles = Niveles()
        #niveles.GuardarNivelesCreados()
        #niveles.GuardarNivelesPredeterminados()
        #niveles.CargarNivelesCreados()
        #niveles.CargarNivelesPredeterminados()
        #menu = MenuPrincipal(self.screen,self.panel)
        #menuTipos = SeleccionTipoNivel(self.screen, self.panel)
        #self.panel.addToList(menu)
        #self.panel.addToList(cuadricula)

    def execute(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    niveles = Niveles()
                    niveles.GuardarNivelesCreados()
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.panel.handle_click(event.pos, event.button)
                elif event.type == pygame.MOUSEMOTION:
                    self.panel.handle_mouse_motion(event.pos)
                elif event.type == pygame.KEYDOWN:
                    self.panel.handle_key(event)

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.panel.handle_clickUp(event)
            self.screen.fill(Colores.WHITE.value)
            self.panel.draw()
            pygame.display.flip()
        pygame.quit()
        sys.exit()

    def iniciarMenus(self):
        niveles = Niveles()
        niveles.CargarNivelesCreados()
        niveles.CargarNivelesPredeterminados()

        volver = CommandCambiarPanel(None,self.panel)
        #Crear menus para juegos
        nombres= ["Facil","Normal","Dificil" ]
        titulo = "Seleccionar Dificultad"
        commands = []
        commands.append(CommandCambiarPanel(MenuNiveles(self.screen,niveles.getFaciles()[0],self.panel),self.panel))
        commands.append(CommandCambiarPanel(MenuNiveles(self.screen,niveles.getNormal()[0],self.panel),self.panel))
        commands.append(CommandCambiarPanel(MenuNiveles(self.screen,niveles.getDificil()[0], self.panel), self.panel))
        menuSeleccionarDificultadBase = Menu(self.screen,self.panel,commands,nombres,titulo,volver)

        commands = []
        commands.append(CommandCambiarPanel(MenuNiveles(self.screen, niveles.getFaciles()[1], self.panel), self.panel))
        commands.append(CommandCambiarPanel(MenuNiveles(self.screen, niveles.getNormal()[1], self.panel), self.panel))
        commands.append(CommandCambiarPanel(MenuNiveles(self.screen, niveles.getDificil()[1], self.panel), self.panel))
        menuSeleccionarDificultadBaseColor = Menu(self.screen,self.panel,commands,nombres,titulo,volver)

        commands= []
        commands.append(CommandCambiarPanel(MenuNiveles(self.screen, niveles.getFacilesCreados()[0], self.panel), self.panel))
        commands.append(CommandCambiarPanel(MenuNiveles(self.screen, niveles.getNormalCreados()[0], self.panel), self.panel))
        commands.append(CommandCambiarPanel(MenuNiveles(self.screen, niveles.getDificilCreados()[0], self.panel), self.panel))
        menuSeleccionarDificultadCrea = Menu(self.screen, self.panel, commands, nombres,titulo,volver)

        commands = []
        commands.append(CommandCambiarPanel(MenuNiveles(self.screen, niveles.getFacilesCreados()[1], self.panel), self.panel))
        commands.append(CommandCambiarPanel(MenuNiveles(self.screen, niveles.getNormalCreados()[1], self.panel), self.panel))
        commands.append(CommandCambiarPanel(MenuNiveles(self.screen, niveles.getDificilCreados()[1], self.panel), self.panel))
        menuSeleccionarDificultadCreaColor = Menu(self.screen, self.panel, commands, nombres,titulo,volver)

        nombres= ["Sin Color","Con Color"]
        titulo = "Seleccionar Nivel"
        commands= []
        commands.append(CommandCambiarPanel(menuSeleccionarDificultadCrea, self.panel))
        commands.append(CommandCambiarPanel(menuSeleccionarDificultadCreaColor, self.panel))
        menuEscogerCreados = Menu(self.screen, self.panel, commands, nombres,titulo,volver)

        commands = []
        commands.append(CommandCambiarPanel(menuSeleccionarDificultadBase, self.panel))
        commands.append(CommandCambiarPanel(menuSeleccionarDificultadBaseColor, self.panel))
        menuEscogerBase = Menu(self.screen, self.panel, commands, nombres,titulo,volver)

        nombres = ["Niveles","Niveles creados","Nivel al azar"]
        commands = []
        commands.append(CommandCambiarPanel(menuEscogerBase,self.panel))
        commands.append(CommandCambiarPanel(menuEscogerCreados,self.panel))
        def nivelAlAzar():
            self.screen = pygame.display.set_mode((0,0),FULLSCREEN)
            g = GrillaVisual(self.screen,niveles.getTableroAleatorio(),self.panel)
            gc = DecoratorClues(g)
            gcm = DecoratorMiniatureRender(gc)
            self.panel.ponerTarget(gcm)
        commands.append(nivelAlAzar)
        menuJuego = Menu(self.screen,self.panel,commands,nombres,titulo,volver)
        nombres = ["Jugar","Crear Nivel","Como jugar","Opciones","Salir"]
        titulo = "Nonograma The_Game"
        commands = []
        commands.append(CommandCambiarPanel(menuJuego,self.panel))

        def crearNivel():
            self.panel.ponerTarget(CrearNivel(self.screen, "Escoger dimensiones", 400, 300, self.panel,
                                    volver))
        commands.append(crearNivel)
        commands.append(mostrar_tutorial)
        commands.append(CommandMenu(self.screen))
        def salir():
            pygame.quit()
            niveles = Niveles()
            niveles.GuardarNivelesCreados()
            niveles.GuardarNivelesPredeterminados()
            sys.exit()
        commands.append(salir)
        menuInicial = Menu(self.screen,self.panel,commands,nombres,titulo)
        volver.setPanel(menuInicial)
        self.panel.addToList(menuInicial)
        self.panel.ponerTarget(menuInicial)

    def iniciarMusica(self):
        self.soundManager = SoundManager()
        self.soundManager.load_sound_as_music("MainMenuTheme", "Musica/MainMenuTheme.mp3")
        self.soundManager.load_sound("guiclick", "Musica/guiclick.ogg")
        self.soundManager.load_sound("victory", "Musica/victory.mp3")
        self.soundManager.load_sound("pintar", "Musica/coins-1.wav")
        self.soundManager.load_sound("error", "Musica/error.wav")
        #soundManager.play_sound_as( "MainMenuTheme", -1)
        self.soundManager.play_music()
        self.soundManager.set_volume_music(50)
        self.soundManager.set_volume_sounds(50)



if __name__ == "__main__":
    matrix = [
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
      [1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    Window(matrix).execute()