from enum import Enum


class Colores(Enum):
    # Colores Básicos
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    # Escala de Grises
    DARK_GREY = (50, 50, 50)
    GREY = (128, 128, 128)
    WHITE_SMOKE = (245, 245, 245)
    LIGHT_GREY = (211, 211, 211)

    #-------------- Colores Rojizos --------------
    WINE = (114, 47, 55)
    RED = (255, 0, 0)
    LIGHT_RED = (255, 185, 185)

    #-------------- Colores Naranjas --------------
    MARMALADE = (128, 64, 0)
    ORANGE = (255, 185, 0)
    LIGHT_ORANGE = (255, 218, 185)

    #-------------- Colores Amarillos --------------
    DARK_YELLOW = (137, 137, 27)
    YELLOW = (255, 255, 0)
    LIGHT_YELLOW = (255, 255, 185)

    #-------------- Colores Verdes --------------
    DARK_GREEN = (0, 100, 0)
    GREEN = (0, 255, 0)
    LIGHT_GREEN = (185, 255, 185)

    #-------------- Colores Azulados --------------
    DARK_BLUE = (0, 0, 139)
    BLUE = (0, 0, 255)
    LIGHT_BLUE = (218, 218, 255)

    #-------------- Colores Morados --------------
    DARK_PURPLE = (128, 0, 128)
    PURPLE = (195, 0, 255)
    LIGHT_PURPLE = (255, 218, 255)

    #-------------- Colores Rosados --------------
    DARK_PINK = (175, 0, 137)
    PINK = (255, 131, 203)
    LIGHT_PINK = (255, 182, 193)

    #-------------- Colores Marrones --------------
    DARK_BROWN = (104, 55, 25)
    BROWN = (165, 89, 42)
    LIGHT_BROWN = (255, 196, 160)

    #-------------- Colores Complementarios --------------
    KHAKI = (240, 230, 140)

    @classmethod
    def get_mapping(cls):
        return {member.name: member.value for member in cls}

    @classmethod
    def get_reverse_mapping(cls):
        return {member.value: number for number, member in enumerate(cls, start=1)}

    @classmethod
    def get_number_mapping(cls):
        return {number: member.value for number, member in enumerate(cls, start=1)}