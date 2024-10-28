from enum import Enum


class Colores(Enum):
    # Colores Básicos
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    # --------------- Propuesta de Futuros Colores ---------------
    # Escala de Grises
    GREY = (128, 128, 128)
    WHITE_SMOKE = (245, 245, 245)
    LIGHT_GREY = (211, 211, 211)
    DARK_GREY = (50, 50, 50)
    # Colores Primarios
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    # Colores Secundarios
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    PINK = (255, 192, 203)
    BROWN = (165, 42, 42)
    # Colores Claros
    LIGHT_RED = (255, 192, 203)
    LIGHT_BLUE = (173, 216, 230)
    LIGHT_GREEN = (144, 238, 144)
    LIGHT_YELLOW = (255, 255, 224)
    LIGHT_CYAN = (224, 255, 255)
    LIGHT_MAGENTA = (255, 224, 255)
    LIGHT_ORANGE = (255, 218, 185)
    LIGHT_PURPLE = (229, 128, 255)
    LIGHT_PINK = (255, 182, 193)
    LIGHT_BROWN = (210, 105, 30)
    # Colores Oscuros
    DARK_RED = (139, 0, 0)
    DARK_BLUE = (0, 0, 139)
    DARK_GREEN = (0, 100, 0)
    DARK_YELLOW = (139, 139, 0)
    DARK_CYAN = (0, 139, 139)
    DARK_MAGENTA = (139, 0, 139)
    DARK_ORANGE = (255, 140, 0)
    DARK_PURPLE = (75, 0, 130)
    DARK_PINK = (199, 21, 133)
    DARK_BROWN = (139, 69, 19)
