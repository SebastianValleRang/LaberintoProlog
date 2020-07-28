conecta(3, 4).
conecta(4, 5).
conecta(9, 10).
conecta(10, 11).
conecta(11, 12).
conecta(12, 13).
conecta(17, 18).
conecta(18, 19).
conecta(19, 20).
conecta(20, 21).
conecta(21, 22).
conecta(22, 23).
conecta(inicio, 2).
conecta(1, 6).
conecta(2, 7).
conecta(3, 8).
conecta(6, 9).
conecta(7, 11).
conecta(8, 13).
conecta(9, 14).
conecta(14, 15).
conecta(15, 17).
conecta(16, 20).
conecta(19, 24).
conecta(23, fin).
conectado(Pos1,Pos2) :- conecta(Pos1,Pos2).
conectado(Pos1,Pos2) :- conecta(Pos2,Pos1).
miembro(X,[X|_]).
miembro(X,[_|Y]) :- miembro(X,Y).
sol :- camino([inicio],Sol),write(Sol).
camino([fin|RestoDelCamino],[fin|RestoDelCamino]).
camino([PosActual|RestoDelCamino],Sol) :- conectado(PosActual,PosSiguiente),\+miembro(PosSiguiente,RestoDelCamino),camino([PosSiguiente,PosActual|RestoDelCamino],Sol).
