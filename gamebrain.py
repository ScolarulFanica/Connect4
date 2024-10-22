from domain.entities import Piece
from repository.repo import RepoPieces

class GameBrain():
    def __init__(self):
        self.__repo_pieces = RepoPieces()
        width = 6
        height = 6
        self.__width = width
        self.__height = height
        self.__base_id = 0

    def place_piece(self,row, column, player):
        new_id = self.__base_id
        row = self.get_row(column)
        piece = Piece(row,column,player,new_id)
        self.__base_id+=1

    def add_piece_to_board(self,piece):
        self.__repo_pieces.add(piece)

    def get_pieces(self):
        return self.repo.pieces.get_all_pieces()
    
    # get_row places the piece on the lowest row possible but checks if there is any pieces on that column and if yes places the piece on top of the already existing one
    def get_row(self,column):
        for piece in self.get_pieces():
            if piece.column == column:
                position += 1
            print(self.__height - position) 

    def create_piece(self, row, column, player, id_piece):
        return self.__repo_pieces.create_piece(row, column, player, id_piece)
            
