class Ventana:
    __titulo=""
    __ver_sup_izqX=""
    __ver_sup_izqY:""
    __ver_inf_derX:""
    __ver_inf_derY=""

    def __init__ (self,tit, vsiX=12, vsiY=14, vidX=20, vidY=18):
        self.__titulo = tit
        self.__ver_sup_izqX = vsiX
        self.__ver_sup_izqY = vsiY
        self.__ver_inf_derX = vidX
        self.__ver_inf_derY = vidY

    def mostrar (self):
        print("Titulo:{}. Vertice superior izquiero X e Y({},{}). Vertice inferior derecho X e Y ({},{})".format(self.__titulo,self.__ver_sup_izqX,self.__ver_sup_izqY,self.__ver_inf_derX,self.__ver_inf_derY))

    def getTitulo (self):
        return self.__titulo

    def alto (self):
        if(self.__ver_sup_izqY < self.__ver_inf_derY):
            alto= self.__ver_inf_derY - self.__ver_sup_izqY
            return alto
        else:
            print("Error en los vertices Y. No se puede calcular el Alto")

    def ancho (self):
        if(self.__ver_sup_izqX < self.__ver_inf_derX):
            ancho = self.__ver_inf_derX - self.__ver_sup_izqX
            return ancho
        else:
            print("Error en los vertices X. No se puede calcular Ancho")

    def moverDerecha (self, valor1=1):
        self.__ver_sup_izqX += valor1
        self.__ver_inf_derX += valor1

    def moverIzquierda (self, valor2=1):
        self.__ver_sup_izqX -= valor2
        self.__ver_inf_derX -= valor2

    def bajar (self, valor3=1):
        self.__ver_sup_izqY -= valor3
        self.__ver_inf_derY -= valor3

    def subir (self, valor4=1):
        self.__ver_inf_derY += valor4
        self.__ver_sup_izqY += valor4
