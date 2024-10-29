
from tkinter import *
from functools import partial
from pgn_fen import *


def traduce(idioma, pieza):

    if idioma == 'sn':
        a_sinbolo = {'R': '♜',
                     'N': '♞',
                     'B': '♝',
                     'Q': '♛',
                     'K': '♚',
                     'P': '♟',

                     'r': '♜',
                     'n': '♞',
                     'b': '♝',
                     'q': '♛',
                     'k': '♚',
                     'p': '♟',
                     ' ': ' '}

        return a_sinbolo[pieza]

# Posicion inicial
jugada_fen, planilla = diccionario_de_movimientos(PGN)

jugada_fotograma = tabla_de_tableros(jugada_fen, planilla)

table = Tk()
table.geometry('1100x900+50+50')
table.title('VISOR DE PARTIDAS <pgn>')
#### Constantes ####
COLUMNAS = 'abcdefgh'
FILAS = '12345678'
# PIEZAS ='TCADRACT'
PIEZAS = '♜♞♝♛♚♝♞♜'
# PEON='P'
PEON = '♟'
LADO = 80
LETRA = 'Helvetica'
#
COLOR_BLANCO = 'red'
COLOR_NEGRO = 'green'
COLOR_PIEZA_BLANCA = 'white'
COLOR_PIEZA_NEGRA = 'black'

cuadro=dict()

### Variables###
quita = BooleanVar(value=True)
pieza = StringVar()
color = StringVar()
grande = IntVar(value=int(LADO*0.5))

turno = IntVar()
turno.set(0)
############################
def introduce_adelante(jugada_fotograma,planilla):
    if turno.get() < len(planilla)-1:
        turno.set(turno.get() + 1)
    
    jugada = planilla[turno.get()]
    print(jugada)
    
    for j in jugada_fotograma[jugada]:
        print('jugada',j)
    
    for f, fila in enumerate(FILAS):
        for c, colum in enumerate(COLUMNAS):
            casilla = (colum+fila)

            cuadro[casilla].configure(text= traduce('sn',jugada_fotograma[jugada][f][c]),
                          font=('Helvetica', grande.get()),
                          fg = 'blue' if jugada_fotograma[jugada][f][c].isupper() else 'black')
    inicio = len(str(turno.get()))
    movimiento.config(
        text=f'{turno.get()//2}... {jugada[inicio:]}' if turno.get() % 2 == 0 else f'{turno.get()//2+1}. {jugada[inicio:]}')
    
    


def introduce_atras(jugada_fotograma, planilla):
    if turno.get() > 0:
        turno.set(turno.get() - 1)
    
    jugada = planilla[turno.get()]
    print(jugada)
    
    for j in jugada_fotograma[jugada]:
        print(j)

    for f, fila in enumerate(FILAS):
        for c, colum in enumerate(COLUMNAS):
            casilla = (colum+fila)

            cuadro[casilla].configure(text=traduce('sn', jugada_fotograma[jugada][f][c]),
                                      font=('Helvetica', grande.get()),
                                      fg='blue' if jugada_fotograma[jugada][f][c].isupper() else 'black')
    if turno.get() == 0:
        movimiento.config(text=f'{jugada}')
    else:
        movimiento.config(text=f'{turno.get()//2}... {jugada}' if turno.get() % 2 == 0 else f'{turno.get()//2+1}. {jugada}')

    
    
#####################################################################################################
# Coronar
def promueve(a, corona):
    pieza.set(a[corona].cget('text'))
############################

# Mueve


def mueve(cuadro, casilla):


    if quita.get():
        quita.set(False)
        pieza.set(cuadro[casilla].cget('text'))
        color.set(cuadro[casilla].cget('fg'))
        cuadro[casilla].configure(text=' ')

    else:
        quita.set(True)
        cuadro[casilla].configure(text=pieza.get(), font=(
    LETRA, grande.get()), fg=color.get())
############################

## corona########
    if casilla[1] == '1':
        a = dict()
        piezas = 'TCAD'
        for c, corona in enumerate(piezas):
    ##
            a[corona] = Button(table, text=corona, font=(LETRA, grande.get()),
                   fg=color.get(), command=partial(promueve, a, corona))
##
            a[corona].place(x=c*200, y=LADO*8, width=200, height=200)

##
            cuadro[casilla].configure(text=pieza.get(), font=(
    LETRA, grande.get()), fg=color.get())
##

############################

## TABLERO###################
for f, fila in enumerate(FILAS):
    for c, colum in enumerate(COLUMNAS):
        casilla = (colum+fila)


        if (c+f) % 2 == 0:
            cuadro[casilla] = Button(table, text= ' ', bg= COLOR_BLANCO,
                         command=partial(mueve, cuadro, casilla))
            ###
            cuadro[casilla].place(x= (c+1)*LADO, y= (f+1)*LADO, width= LADO, height= LADO)
            ###
        else:
            cuadro[casilla] = Button(table, text= ' ', bg= COLOR_NEGRO,
                         command= partial(mueve, cuadro, casilla))

            cuadro[casilla].place(x= (c+1)*LADO, y= (f+1)*LADO, width= LADO, height= LADO)

####    POSICION INICIAL ######################################################################
jugada = planilla[turno.get()]
print(jugada)
for j in jugada_fotograma[jugada]:
        print(j)

for f, fila in enumerate(FILAS):
    for c, colum in enumerate(COLUMNAS):
        casilla = (colum+fila)

        cuadro[casilla].configure(text= traduce('sn', jugada_fotograma[jugada][f][c]),
                                      font= ('Helvetica', grande.get()),
                                      fg = 'blue' if jugada_fotograma[jugada][f][c].isupper() else 'black')

#####################################################################################################
movimiento = Label(table, text= planilla[turno.get()], 
                   font= ('Helvetica', grande.get()))
movimiento.place(x= LADO, y= 9*LADO, width= LADO*4)

avance = Button(table, text='>>', bg= 'lightblue',
                command=partial(introduce_adelante, jugada_fotograma, planilla))
avance.place(x= 3*LADO, y= 10*LADO, width= LADO)

retroceso = Button(table, text= '<<', bg= 'lightblue',
                command=partial(introduce_atras, jugada_fotograma, planilla))
retroceso.place(x= 6*LADO, y= 10*LADO, width= LADO)

lb_pgnb = Listbox(table, width= 7, height= len(planilla)//2,
                   font='arial 20', bg='yellow')
lb_pgnb.place(x= 10*LADO, y=1*LADO)

lb_pgnn = Listbox(table, width= 7, height= len(planilla)//2,
                   font='arial 20', bg='yellow')
lb_pgnn.place(x= 11*LADO+29, y= 1*LADO)

lb_pgnb.delete(0, END)  # para que quede bacio
movi_completo= ''
con = 0
for index, movi in enumerate(planilla):
    
    if index == 0:
        pass
    
    elif index != 0:   
        if index % 2 != 0:
            con += 1
            inicio= len(str(index))
            movi_completo = str(con) + '.' + movi[inicio:]
           
            lb_pgnb.insert(con, movi_completo)
            

        else:
            
            lb_pgnn.insert(con, movi[inicio:])
            
        

############################
############################
table.mainloop()
