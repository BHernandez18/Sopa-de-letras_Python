import tablero as tbl

if __name__ == "__main__":
    lista_palabras = ["hola", "mundo", "benjamin"]
    tablero = tbl.Tablero(lista_de_palabras=lista_palabras)
    print('filas = {}'.format(tablero.numero_de_filas))
    print('columnas = {}'.format(tablero.numero_de_columnas))
    print('palabras = {}'.format(tablero.lista_de_palabras))
    tablero.mostrarTablero()
