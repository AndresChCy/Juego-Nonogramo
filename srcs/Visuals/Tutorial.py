import pygame

from srcs.Visuals.Colores import Colores
from Button import Button

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tutorial de Nonogramas")

def mostrar_tutorial():
    running = True
    current_step = 0

    # Configuración de los paneles del tutorial
    panels = [
        {"buttons": [("", Colores.RED.value, "Img/tutorial1.png")], "background": Colores.LIGHT_BLUE.value},
        {"buttons": [("", Colores.GREEN.value, "Img/tutorial2.png")], "background": Colores.LIGHT_GREEN.value},
        {"buttons": [("", Colores.YELLOW.value, "Img/tutorial3.png")], "background": Colores.LIGHT_YELLOW.value}
    ]

    def siguiente():
        nonlocal current_step
        if current_step < len(panels) - 1:
            current_step += 1
            return

    def anterior():
        nonlocal current_step
        if current_step > 0:
            current_step -= 1
            return


    while running:
        # Fondo del panel actual
        current_panel = panels[current_step]
        if "image" in current_panel:
            try:
                background_image = pygame.image.load(current_panel["image"])
                screen.blit(pygame.transform.scale(background_image, screen.get_size()), (0, 0))
            except pygame.error:
                screen.fill(current_panel["background"])
        else:
            screen.fill(current_panel["background"])

        # Dibujar botones de navegación
        boton_siguiente = Button(screen, 120, 60, 650, 500, Colores.GREEN.value, siguiente, text="Siguiente")
        boton_anterior = Button(screen, 120, 60, 40, 510, Colores.RED.value, anterior, text="Anterior")
        boton_siguiente.draw()
        boton_anterior.draw()

        # Dibujar botones del panel actual
        for i, (text, color, image_path) in enumerate(panels[current_step]["buttons"]):
            x = 400 - (100 // 2)
            y = 250 + i * 60
            Button(screen, 740, 450, 30, 10, color, lambda: print(f"{text} presionado"), text=text, image_path=image_path).draw()

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_siguiente.is_clicked(event.pos):
                    if  current_step == len(panels) -1 :
                        return
                    boton_siguiente.click()
                elif boton_anterior.is_clicked(event.pos):
                    if not current_step > 0:
                        return
                    boton_anterior.click()

        pygame.display.flip()


