


conectado(Pos1,Pos2) :- conecta(Pos1,Pos2).
conectado(Pos1,Pos2) :- conecta(Pos2,Pos1).

miembro(X,[X|_]).
miembro(X,[_|Y]) :- miembro(X,Y) .

sol :- camino([inicio],Sol),write(Sol) .

camino([fin|RestoDelCamino],[fin|RestoDelCamino]).
camino([PosActual|RestoDelCamino],Sol) :- conectado(PosActual,PosSiguiente),\+ miembro(PosSiguiente,RestoDelCamino),
					   camino([PosSiguiente,PosActual|RestoDelCamino],Sol).
