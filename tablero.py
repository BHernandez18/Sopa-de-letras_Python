from random import choices, random, randint
from string import ascii_uppercase
from copy import deepcopy


class Tablero():


    numero_de_filas: int = 0
    numero_de_columnas: int = 0
    tablero: list = []
    lista_de_palabras: list = []


    def __init__(self, numero_de_filas=10, numero_de_columnas=10, lista_de_palabras=[]):
        self.numero_de_filas = numero_de_filas
        self.numero_de_columnas = numero_de_columnas
        self.lista_de_palabras = lista_de_palabras
        self.inicializarTablero()
        self.ubicarPalabras(self.lista_de_palabras)


    def inicializarTablero(self):
        for _ in range(self.numero_de_columnas):
            fila = ' ' * self.numero_de_columnas
            fila = list(fila)
            self.tablero.append(fila)


    def ubicarPalabras(self, palabras_a_ingresar):
        orientaciones = ['arriba', 'abajo', 'izquierda', 'derecha']
        indice_palabra = 0
        while indice_palabra < len(palabras_a_ingresar):
            palabra = palabras_a_ingresar[indice_palabra]
            posicion_x = randint(0, self.numero_de_filas - 1)
            posicion_y = randint(0, self.numero_de_columnas - 1)
            orientacion = choices(orientaciones)[0]
            if self.verificarPosibilidad(palabra, posicion_x, posicion_y, orientacion):
                self.insertarPalabra(palabra, posicion_x, posicion_y, orientacion)
                indice_palabra += 1


    def verificarPosibilidad(self, palabra, posicion_x, posicion_y, orientacion):
        insertable = True
        posicion_x_final = posicion_x
        posicion_y_final = posicion_y
        if orientacion == 'arriba': posicion_x_final -= len(palabra)
        elif orientacion == 'abajo': posicion_x_final += len(palabra)
        elif orientacion == 'izquierda': posicion_y_final -= len(palabra)
        else: posicion_y_final += len(palabra)

        # 1ra verificacion: Mantenerse dentro de los limites del tablero
        if -1 <= posicion_x_final <= self.numero_de_filas and -1 <= posicion_y_final <= self.numero_de_columnas:

            # 2da verificacion: Insercion sin sobreescribir otras palabras ya insertadas
            insertable = True
            celdas_requeridas = self.obtenerContenidoCeldas(posicion_x, posicion_y, posicion_x_final, posicion_y_final, orientacion)
            for letra_postulante, letra_insertada in zip(palabra, celdas_requeridas):
                if letra_postulante == letra_insertada or letra_insertada == ' ': continue
                insertable = False

        else: insertable = False
        return insertable


    def obtenerContenidoCeldas(self, posicion_x, posicion_y, posicion_x_final, posicion_y_final, orientacion):
        salto = 1 if orientacion in ['abajo', 'derecha'] else -1
        palabra = ''
        if orientacion in ['arriba', 'abajo']:
            for indice_x in range(posicion_x, posicion_x_final, salto):
                palabra += self.tablero[indice_x][posicion_y]
        else:
            for indice_y in range(posicion_y, posicion_y_final, salto):
                palabra += self.tablero[posicion_x][indice_y]
        return palabra


    def insertarPalabra(self, palabra, posicion_x, posicion_y, orientacion):
        salto = 1 if orientacion in ['abajo', 'derecha'] else -1
        posicion_x_final = posicion_x
        posicion_y_final = posicion_y
        if orientacion == 'arriba': posicion_x_final -= len(palabra)
        elif orientacion == 'abajo': posicion_x_final += len(palabra)
        elif orientacion == 'izquierda': posicion_y_final -= len(palabra)
        else: posicion_y_final += len(palabra)

        if orientacion in ['arriba', 'abajo']:
            for indice_x in range(posicion_x, posicion_x_final, salto):
                self.tablero[indice_x][posicion_y] = palabra[0]
                palabra = palabra[1:]
        else:
            for indice_y in range(posicion_y, posicion_y_final, salto):
                self.tablero[posicion_x][indice_y] = palabra[0]
                palabra = palabra[1:]


    def mostrarTablero(self):
        for i in range(self.numero_de_filas):
            for j in range(self.numero_de_columnas):
                print('|{}'.format(self.tablero[i][j]), end = '')
            print('|')