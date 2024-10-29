
from pgn_fen import *
PGN= '''
[Evento "Partida relámpago puntuada"]
[Sitio " https://lichess.org/hYMu3JbV "]
[Fecha "2024.09.20"]
[LIFTISTO blanco]
[Negro "Sso889"]
[Resultado "0-1"]
[Fecha UTC "2024.09.20"]
[Hora UTC "00:22:48"]
[Elo blanco "1628"]
[Elo negro "1641"]
[Diferencia de calificación de WhiteRating "-5"]
[Diferencia de calificación negra "+6"]
[Variante "Estándar"]
[Control de tiempo "300+0"]
[ECO "A41"]
[Introducción "Defensa de la rata: la rata inglesa, Gambito de Lisboa"]
[Terminación "Normal"]
[Anotador " lichess.org "]

1. d4 {[ % eval 0.17] [%clk 0:05:00]} 1... d6 {[%eval 0.5] [%clk 0:05:00]} 2. c4 {[%eval 0.25] [%clk 0:04:59]} 2... e5 {[%eval 0.33] [%clk 0:04:59]} 3. dxe5 {[%eval - 0.05] [%clk 0:04:56]} 3... Cc6 {[%eval 0.42] [%clk 0:04:59]} {A41 Defensa de la Rata: Rata Inglesa, Gambito de Lisboa} 4. exd6 {[%eval 0.34] [%clk 0:04:54]} 4... Axd6 {[%eval 0.41] [%clk 0:04:59]} 5. Cc3 {[%eval 0.34] [%clk 0:04:52]} 5... Cf6 {[%eval 0.43] [%clk 0:04:58]} 6. Cf3 {[%eval 0.39] [%clk 0:04:50]} 6... Ag4 {[%eval 0.44] [%clk 0:04:57]} 7. e4?! {(0.44 → - 0.53) Inexactitud. Cd4 era la mejor opción.} {[%eval - 0.53] [%clk 0:04:47]} (7. Cd4 OO 8. Cxc6 bxc6 9. g3 De7 10. Ag2 Ae5 11. OO Axc3) 7... De7 {[%eval - 0.53] [%clk 0:04:56]} 8. Ae2 {[%eval - 0.58] [%clk 0:04:44]} 8... OOO {[%eval - 0.7] [%clk 0:04:55]} 9. Cd5?? {(-0.70 → - 2.49) Error garrafal. Cd2 era lo mejor.} {[%eval - 2.49] [%clk 0:04:18]} (9. Cd2) 9... Dxe4 {[%eval - 2.52] [%clk 0:04:45]} 10. Cxf6?? {(-2.52 → - 5.31) Error garrafal. Lo mejor era OO.} {[%eval - 5.31] [%clk 0:04:06]} (10. OO Cxd5 11. cxd5 Ce5 12. Cd4 Ac5 13. Dc2 Dxc2 14. Axg4 + Cxg4 15. Cxc2 Txd5) 10... gxf6 {[%eval - 4.83] [%clk 0:04:42]} 11. Ae3?! {(-4, 83 → - 6, 33) Inexactitud. Rf1 era la mejor.} {[%eval - 6, 33] [%clk 0:03:38]} (11. Rf1 Ac5 12. Cd2 Axe2 + 13. Dxe2 Dc2 14. g3 Ab4 15. Rg2 Axd2 16. Te1 Td7) 11... Cb4?? {(-6, 33 → - 2, 24) Error. Ab4 + era la mejor.} {[%eval - 2.24] [%clk 0:04:19]} (11... Ab4 + 12. Ad2 Th8 13. OO Axd2 14. h3 Ah5 15. Cxd2 Dxe2 16. g4 Txd2 17. Dxe2) 12. Db3?? {(-2.24 → - 5.99) Error garrafal. Lo mejor era OO.} {[%eval - 5.99] [%clk 0:03:11]} (12. OO Thg8 13. Rh1 Ac5 14. Db3 Cc2 15. Tac1 Cxe3 16. fxe3 Axe3 17. Tc3 Ac5) 12... Cc2 + {[%eval - 6.04] [%clk 0:04:07]} 13. Rf1 {[%eval - 6.03] [%clk 0:03:10]} 13... Cxa1 {[%eval - 6.04] [%clk 0:04:00]} 14. h3?! {(-6.04 → - 10.59) Inexactitud. Dd3 era la mejor opción.} {[%eval - 10.59] [%clk 0:03:08]} (14. Dd3 Af5 15. Dxe4 Axe4 16. c5 Ae7 17. Ce1 Cc2 18. Cxc2 Axc2 19. c6 Rb8) 14... Cxb3 {[%eval - 9.77] [%clk 0:03:54]} {Las blancas se rinden.} 0-1
'''

#PGN =
'''
[Evento "Partida relámpago puntuada"]
[Sitio " https://lichess.org/BNrT8FR2 "]
[Fecha "2024.09.16"]
[LIFTISTO blanco]
["jjdox" negro]
[Resultado "0-1"]
[Fecha UTC "2024.09.16"]
[Hora UTC "00:46:47"]
[Elo blanco "1582"]
[Elo negro "1621"]
[Diferencia de calificación de WhiteRating "-5"]
[Diferencia de calificación negra "+5"]
[Variante "Estándar"]
[Control de tiempo "300+0"]
[ECO "D45"]
[Introducción a la "Defensa Semieslava: Variante Normal"]
[Terminación "Normal"]
[Anotador " lichess.org "]

1. d4 { [%clk 0:05:00] } 1... e6 { [%clk 0:05:00] } 2. c4 { [%clk 0:04:58] } 2... d5 { [%clk 0:04:59] } 3. Cc3 { [%clk 0:04:56] } 3... Cf6 { [%clk 0:04:58] } 4. e3 { [%clk 0:04:55] } 4... c6 { [%clk 0:04:53] } 5. Cf3 { [%clk 0:04:53] } 5... Cbd7 { [%clk 0:04:52] } { D45 Defensa Semieslava: Variante Normal } 6. Ae2 { [%clk 0:04:52] } 6... Ad6  { [%clk 0:04:47] } 7. b3 { [%clk 0:04:50] } 7... e5 { [%clk 0:04:46] } 8. dxe5 { [%clk 0:04:46] } 8... Cxe5 { [%clk 0:04:45] } 9. OO { [%clk 0:04:42] } 9... Cxf3+ { [%clk 0:04:42] } 10. Axf3 { [%clk 0:04:40] } 10... Dc7 { [%clk 0:04:41] } 11. h3 { [%clk 0:04:33] } 11... OO { [%clk 0:04:38] } 12. cxd5 { [%clk 0:04:27] } 12... cxd5 { [%clk 0:04:34] } 13. Cxd5 { [%clk 0:04:25] } 13... Cxd5  { [%clk 0:04:32] } 14. Axd5 { [%clk 0:04:19] } 14... Td8 { [%clk 0:04:27] } 15. Df3 { [%clk 0:04:08] } 15... Ae6 { [%clk 0:03:49] } 16. Axe6 { [%clk 0:04:01] } 16... fxe6 { [%clk 0:03:48] } 17. Ab2 { [%clk 0:03:59] } 17... Tf8 { [%clk 0:03:43] } 18. Dg4 { [%clk 0:03:52] } 18... De7 { [%clk 0:03:34] } 19. Tad1 { [%clk 0:03:37] } 19... Tf7 { [%clk 0:03:22] } 20. Dd4 { [%clk 0:03:27] } 20... Ac5 { [%clk 0:03:16] } 21. De5 { [%clk 0:03:20] } 21... Taf8 { [%clk 0:03:09] } 22. Ad4 { [%clk 0:03:15] } 22... Ad6 { [%clk 0:03:06] } 23. Dg5 { [%clk 0:03:06] } 23... Dxg5 { [%clk 0:02:59] } { Las blancas se rinden. } 0-1

'''

'''para quitatr parentesis'''

def quitar(PGN,caracter1,caracter2):
    paren=''
    aux = False
    for i in PGN:
        if i == caracter1:
            aux=True
        if aux:    
            paren += i
        if i == caracter2:
            aux=False
            PGN=PGN.replace(paren,'')
            paren=''
    return PGN
    


    ############################
if __name__ == '__main__':
    print(dir(str))
    PGN = quitar(PGN, '(', ')')
    PGN = quitar(PGN, '{', '}')


    print(PGN)
