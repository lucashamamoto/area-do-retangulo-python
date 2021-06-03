class Retangulo:
#classe Retangulo define os atributos X, Y e Área, além do contrutor e método obter_area().
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__area = x * y

    def obter_area(self):
        return self.__area