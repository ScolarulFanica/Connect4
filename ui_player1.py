from game_engine.gamebrain import GameBrain
from domain.entities import Piece

class UIPlayer1():
    def __init__(self):
        self.__game_brain = GameBrain()

    def run(self):
        while True:
            self.width = int(input("Choose the width of the board(must be at least 4): "))
            if self.width < 4:
                raise ValueError("The width must be at least 4!")
            self.height = int(input("Choose the height of the board(must be at least 4): "))
            if self.height < 4:
                raise ValueError("The height must be at least 4!")
            else:
                break
        
        while True:
            player = input("Choose between X and 0.")
            player = player.strip()
            if player in ["X", "0"]:
                break
        while True:
            self.__draw_board()
            if player == 'X':
                column = int(input("Choose a column between 1 and " + str(self.width) + ": "))
                if column in range(self.width):
                    new_piece = self.__game_brain.create_piece(self.__game_brain.get_row(column), column, player,0)
                    self.__game_brain.add_piece_to_board(new_piece)

                else:
                    raise ValueError("The column must be between 1 and " + str(self.width) + "!")
            else:
                column = int(input("Choose a column between 1 and " + str(self.width) + ": "))
                if column in range(self.width):
                    self.__game_brain.place_piece(self.__game_brain.get_row(column), column, player)
                else:
                    raise ValueError("The column must be between 1 and " + str(self.width) + "!")


    def __draw_board(self):
        pieces = self.__game_brain.get_pieces()
        self.see_pieces()
        board =[['~']*self.height]*self.width
        for piece in pieces:
            board[piece[0]][piece[1]] = piece[2]
        for row in board:
            print(row)


    def see_pieces(self):
        print(self.__game_brain.get_pieces())

    

        

        
        
        
