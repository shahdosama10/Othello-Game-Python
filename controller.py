from model import Model
from view import OthelloView
from player import Player

# The controller class handles the game logic
class OthelloController:
    def __init__(self):
        # Initialize the view
        self.model = Model()
        self.HumanPlayer = Player()
        self.ComputerPlayer = Player()
        self.view = OthelloView(self)
        self.difficulty = "Easy"  # Default difficulty level
        self.depth = 1
        # GUI loop
        self.view.mainloop()

    def set_difficulty(self, difficulty):
        # Set the difficulty level
        self.difficulty = difficulty
        if (self.difficulty == "Medium"):
            self.depth = 3
        elif (self.difficulty == "Hard"):
            self.depth = 5
            
    def get_difficulty(self):
        # Return the difficulty level
        return self.difficulty

    
    def get_board(self):
        # Return the current board state
        return self.model.get_board()

    def CheckGame(self):
        if self.HumanPlayer.number_of_pieces == 0 or self.ComputerPlayer.number_of_pieces == 0:
            return True
        return False

    def SkipTurn(self, player):
        if self.model.get_valid_moves(player) == []:
            return True
        return False
    def make_move(self, x, y):
          if self.model.make_move(x + 1, y + 1, self.HumanPlayer.color,self.model.GetIndexsOfFlipped(x + 1, y + 1, self.HumanPlayer.color)):
              self.view.update_board_display(self.model.get_board())
              self.HumanPlayer.number_of_pieces -= 1
              if (self.CheckGame() or (
                      self.SkipTurn(self.ComputerPlayer.color) and self.SkipTurn(self.HumanPlayer.color))):
                  self.view.GameOver(self.HumanPlayer, self.ComputerPlayer)
                  return
              if self.SkipTurn(self.ComputerPlayer.color)== False:
                  self.make_computer_move( self.depth, self.ComputerPlayer.color , self.HumanPlayer.color)
                  self.view.after(100)
                  self.view.update_board_display(self.model.get_board())
                  self.ComputerPlayer.number_of_pieces -= 1
                  if (self.CheckGame() or (
                      self.SkipTurn(self.ComputerPlayer.color) and self.SkipTurn(self.HumanPlayer.color))):
                         self.view.GameOver(self.HumanPlayer, self.ComputerPlayer)
                         return
                  while  self.SkipTurn(self.HumanPlayer.color) == True :
                        self.view.NoMove(self.HumanPlayer.color)
                        self.make_computer_move(self.depth, self.ComputerPlayer.color ,self.HumanPlayer.color)
                        self.view.after(100)
                        self.view.update_board_display(self.model.get_board())
                        self.ComputerPlayer.number_of_pieces -= 1
                        if (self.CheckGame() or (
                                self.SkipTurn(self.ComputerPlayer.color) and self.SkipTurn(self.HumanPlayer.color))):
                            self.view.GameOver(self.HumanPlayer, self.ComputerPlayer)
                            return
              else:
                  self.view.NoMove(self.ComputerPlayer.color)
          else:
              self.view.InvalidMove()





    def make_computer_move(self, depth,ComputerPlayercolor , HumanPlayerColor):
        self.model.make_computer_move(depth , ComputerPlayercolor, HumanPlayerColor)



    def SkipTurn(self, player):
        if self.model.get_valid_moves(player) == []:
            return True
        return False




    # def make_move(self, x, y):
        # if (self.CheckGame() or(self.SkipTurn(self.ComputerPlayer.color) and self.SkipTurn(self.HumanPlayer.color)) ):
        #     self.view.GameOver(self.HumanPlayer,self.ComputerPlayer)
        #     return
        # if (self.SkipTurn(self.HumanPlayer.color) )== False :
        #     if self.model.make_move(x + 1, y + 1, self.HumanPlayer.color,self.model.GetIndexsOfFlipped(x + 1, y + 1, self.HumanPlayer.color)):
        #         self.view.update_board_display(self.model.get_board())
        #         self.HumanPlayer.number_of_pieces -= 1
        #         if (self.CheckGame() or (
        #                 self.SkipTurn(self.ComputerPlayer.color) and self.SkipTurn(self.HumanPlayer.color))):
        #             self.view.GameOver(self.HumanPlayer, self.ComputerPlayer)
        #             return
        #         if self.SkipTurn(self.ComputerPlayer.color)== False:
        #             self.make_computer_move(self.ComputerPlayer.color)
        #             self.view.update_board_display(self.model.get_board())
        #             self.ComputerPlayer.number_of_pieces -= 1
        #             if (self.CheckGame() or (
        #                     self.SkipTurn(self.ComputerPlayer.color) and self.SkipTurn(self.HumanPlayer.color))):
        #                 self.view.GameOver(self.HumanPlayer, self.ComputerPlayer)
        #                 return
        #         else:
        #             self.view.NoMove(self.ComputerPlayer.color)
        #     else:
        #         self.view.InvalidMove()
        # else:
        #     self.view.NoMove(self.HumanPlayer.color)
        #     self.make_computer_move(self.ComputerPlayer.color)
        #     self.view.update_board_display(self.model.get_board())
        #     self.ComputerPlayer.number_of_pieces -= 1
        #     if (self.CheckGame() or (
        #                 self.SkipTurn(self.ComputerPlayer.color) and self.SkipTurn(self.HumanPlayer.color))):
        #         self.view.GameOver(self.HumanPlayer, self.ComputerPlayer)
        #         return
