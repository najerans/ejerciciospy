
class Square:
    def __init__(self):
        self.__height = 2 #doble _ _ dato protegido 
        self.__width = 2
    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_sdie
squere = Square()
square.__height = 3




'''CAPTADORES: *Descriptores de acceso* --> metodos dedicados a leer datos o a cambiarlos 
los captadores se encargan de hacer que los datros internos sean legibles para el exterior
los ESTABLECEDORES  son metodos que pueden cambiar los datos directamente 
Un establecedor puede actuar como proteccion para que no se pueda establecer un valor incorrecto'''


class Square:
    def __init__(self):
        self.__height = 2
        self.__width = 2
    def __init__(self, new_side):
        self.__height = new_side 
        self.__widht = new_side
    def get_height(self):
        return self.__height
    def set_height(self, h):
        if h >= 0:
            self.__height = h
        else:
            raise Exception("El valor necesita ser 0 o mayor")

    square = Square()
    square.__height = 3


    ''' DECORADORES @property (metaprogramacion) son funciones que toman la funcion como una entrada
    la idea es codificar la  funcionalidad reutilizable como funciones de decorador y despues usarla 
    para decorar esas funciones 

    --@property--
    Crea un campo de respaldo: al decorar una función con el decorador @property, se crea un campo privado de respaldo. Puede invalidar este comportamiento si quiere, pero es estupendo tener un comportamiento predeterminado.
    Identifica un establecedor: un método de establecedor puede cambiar el campo de respaldo.
    Identifica un captador: esta función debe devolver el campo de respaldo.    
    Identifica una función de eliminación: esta función puede eliminar el campo. '''


    class Square:
        def __init__(self, w, h):
            self.__height = h
            self.__width = w

        def set_side(self, new_side):
            self.__height = new_side
            self.__width = new_side

        @property
            def height(self):
                return self.__height

        @height.setter
            def height(self, new_value):
                if new_value >= 0:
                    self.__height = new_value
                else:
                raise Exception("value must be larger than 0")

