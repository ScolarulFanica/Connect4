

class Piece:
    def __init__(self,row:int,column:int,player:str,id_piece:int):
        self.__column = column
        self.__player = player
        self.__id_piece = id_piece
        self.__row = row

    @property
    def column(self):
        return self.__column
    
    @property
    def player(self):
        return self.__player
    
    @property
    def id_piece(self):
        return self.__id_piece
    
    @property
    def row(self):
        return self.__row
    
    @column.setter
    def column(self,column):
        self.__column = column

    @player.setter
    def player(self,player):
        self.__player = player

    @id_piece.setter
    def id_piece(self,id_piece):
        self.__id_piece = id_piece

    @row.setter
    def row(self,row):
        self.__row = row
        