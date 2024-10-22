from domain.entities import Piece

class RepoPieces:
    def __init__(self):
        self.pieces = []

    def add(self, piece:Piece):
        #append piece to the list of pieces
        #piece = self.create_piece(piece.row, piece.column, piece.player, piece.id_piece)
        self.pieces.append(piece)
        print ("1 piece added to the board")

    def create_piece(self, row:int, column:int, player:str, id_piece:int)->list:
        piece = [row, column, player, id_piece]
        return piece
    
    def get_all_pieces(self):
        for piece in self.pieces:
            print(piece)
        return [piece for piece in self.pieces]
    
    

    
