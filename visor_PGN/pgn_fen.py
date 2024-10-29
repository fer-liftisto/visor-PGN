###Fer
# pgn
import chess
import re
from partidas import PGN

#########################


def traduce_replace(f):
    # '♟♜♞♝♛♚' #
    f = f.replace('R', 'K')
    f = f.replace('T', 'R')
    f = f.replace('C', 'N')
    f = f.replace('A', 'B')
    f = f.replace('D', 'Q')
    
    f = f.replace('OOO', 'O-O-O')
    f = f.replace('OO', 'O-O')

    return f
def elimina_llaves(PGN):
    pass

############################
def moviAlista(idioma,PGN) -> list:
    if idioma == 'uk':
    # mete los movimientos en una lista
        busca = r'[RNBQK]?[a-h]?[1-8]?x?[a-h][1-8]=?[RNBQ]?|O-O-O|O-O'
        planilla = re.findall(busca, PGN)
        return planilla
    ############################


    elif idioma == 'sp':
    # mete los movimientos en una lista
        busca = r'[TCADR]?[a-h]?[1-8]?x?[a-h][1-8]=?[TCAQ]?|O-O-O|O-O|OOO|OO'
        planilla = re.findall(busca, PGN)
        print(planilla)
        planilla1=[]
        con= 1
        for movimiento in planilla:
                planilla1.append(str(con)+traduce_replace(movimiento))
                con+= 1
        print('planilla1',planilla1)
        return planilla1
    ############################
############################
# diccionario obtenido
# partida = {'inicio': 'rnbqkbnr/pppppppp/8/8/8/PPPPPPPP/RNBQKBNR'
###########################

###########################
# crea un diccionario
# clave el movimiento
# valor la  FEN de movimiento


def diccionario_de_movimientos(PGN):

    ##########################
    tablero = chess.Board()

    # Lista de movimientos como str
    jugadas = moviAlista('sp', PGN)

    jugada_fen = {'inicial': tablero.fen()}
    con= 1
    for jugada in jugadas:
    # Introduce las jugadas
    # en el modulo
        inicio= len(str(con)) # Para que las claves del dicionario dean unicas
        tablero.push_san(jugada[inicio:]) # Para pasarle solo el movimiento
        con +=1
# Hay que hacer una copia
# Para hacer una lista de tableros
# aux = posi.copy()
# tablero.append(aux)

# Rellena el diccionario
# Con la jugada y el fen
        jugada_fen[jugada] = tablero.fen()

    planilla = ['inicial']
    planilla.extend(jugadas)
    return jugada_fen, planilla


def tabla_de_tableros(jugada_fen, planilla) -> dict:
    jugada_fotograma = {}
    
    for jugada in planilla: # un movimiento
        fotograma = []
        
        # ['rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1']
        FEN = jugada_fen[jugada].split(' ')
        
        # ['r1b1kbnr', 'ppppqppp', '2n5', '4P3', '8', '5N2', 'PPP1PPPP', 'RNBQKB1R']
        FEN = FEN[0].split('/') # una lista de filas
        
        for fila_fen in FEN:
            
            fila_tablero = []
            for casilla in fila_fen:
                
                if casilla.isnumeric():
                    con = int(casilla)
                    while con > 0:
                        fila_tablero.append(' ')
                        con -= 1
                elif casilla.isalpha():
                    fila_tablero.append(casilla)
                
            # [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            #  ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            #  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            #  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            #  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            #  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            #  ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            #  ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
            fotograma.append(fila_tablero)
           
        # inicial : [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        #            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        #            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        #            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        #            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        #            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        #            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        #            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        jugada_fotograma[jugada]= fotograma

    return jugada_fotograma

###################################################################
if __name__ == '__main__':
    elimina_llaves(PGN)
    jugada_fen, planilla = diccionario_de_movimientos(PGN)
    print(jugada_fen)
    jugada_fotograma = tabla_de_tableros(jugada_fen, planilla)
    
    for  jugada in planilla:
        print(jugada)
        for fotograma in jugada_fotograma[jugada]: 
            print(fotograma)
######################################################################
