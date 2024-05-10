import tkinter as tk


class OthelloView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("Othello")
        self.geometry("400x200")
        self.controller = controller
        
    
    def create_difficulty_selection(self):
       pass


    def create_board(self):
        pass
    
    def start_game(self):
        pass
    
    def update_board_display(self, board):
        pass
    
    def display_winner(self, winner):
        pass