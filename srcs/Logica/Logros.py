class Logros:
    def __init__(self):
        # Inicializar los atributos como parte de la instancia
        self.Superar_nivel_facil = False
        self.Superar_nivel_normal = False
        self.Superar_nivel_dificil = False
        self.Crear_nivel = False
        # Guardar los atributos en una lista para manipularlos más fácilmente
        self.valores_logros = [self.Superar_nivel_facil, self.Superar_nivel_normal,
                               self.Superar_nivel_dificil, self.Crear_nivel]

        # Leer archivo y actualizar logros
        contador = 0
        with open('../../Logros', 'r') as file:
            for item in file:
                data = item.split(' ')
                if data[1].strip() == "True":
                    self.valores_logros[contador] = True
                print(data)
                contador += 1
            print(self.valores_logros)

    def superar_nivel_facil(self):
        if self.valores_logros[0]  == False:
            self.valores_logros[0]  = True
            with open('../../Logros', 'r') as file:
                lineas = file.readlines()  # Lee todas las líneas en una lista

            # Modifica la primera línea (línea 0) en la lista
            lineas[0] = "Superar_nivel_facil: True\n"

            # Escribe todas las líneas de nuevo al archivo
            with open('../../Logros', 'w') as file:
                file.writelines(lineas)

    def superar_nivel_normal(self):
        if self.valores_logros[1] == False:
            self.valores_logros[1]  = True
            with open('../../Logros', 'r') as file:
                lineas = file.readlines()  # Lee todas las líneas en una lista

            # Modifica la primera línea (línea 0) en la lista
            lineas[1] = "Superar_nivel_facil: True\n"

            # Escribe todas las líneas de nuevo al archivo
            with open('../../Logros', 'w') as file:
                file.writelines(lineas)

    def superar_nivel_dificil(self):
        if self.valores_logros[2] == False:
            self.valores_logros[2]= True
            with open('../../Logros', 'r') as file:
                lineas = file.readlines()  # Lee todas las líneas en una lista

            # Modifica la primera línea (línea 0) en la lista
            lineas[2] = "Superar_nivel_facil: True\n"

            # Escribe todas las líneas de nuevo al archivo
            with open('../../Logros', 'w') as file:
                file.writelines(lineas)
    def crear_nivel(self):
        if self.valores_logros[3] == False:
            self.valores_logros[3] = True
            with open('../../Logros', 'r') as file:
                lineas = file.readlines()  # Lee todas las líneas en una lista

            # Modifica la primera línea (línea 0) en la lista
            lineas[3] = "Superar_nivel_facil: True\n"

            # Escribe todas las líneas de nuevo al archivo
            with open('../../Logros', 'w') as file:
                file.writelines(lineas)


if __name__ == '__main__':
    logros = Logros()
    print("\n")
    logros.superar_nivel_facil()
    logros.crear_nivel()

