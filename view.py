import tkinter as tk
from tkinter import messagebox

class OthelloView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Othello")
        
        # The currect state is menu
        self.state = "menu"
        
        # Initialize the menu screen
        self.create_menu_screen()
    
    def create_menu_screen(self):

        difficulty_label = tk.Label(self, text="Select Difficulty:")
        difficulty_label.pack(pady=10)
        
        # Levels radio buttons
        self.difficulty_var = tk.StringVar(value="Easy")
        difficulties = ["Easy", "Medium", "Hard"]
        
        for difficulty in difficulties:
            radio_button = tk.Radiobutton(self, text=difficulty, variable=self.difficulty_var, value=difficulty)
            radio_button.pack(anchor='w')
        
        # Start button
        start_button = tk.Button(self, text="Start Game", command=self.start_game)
        start_button.pack(pady=20)
    
    def start_game(self):
        self.controller.set_difficulty(self.difficulty_var.get())
        
        # The currect state is game
        self.state = "game"
        
        # Initialize the game board
        self.create_game_board()
    
    def create_game_board(self):
        # Clear previous widgets
        for widget in self.winfo_children():
            widget.destroy()
        
        # Create the game board frame
        self.board_frame = tk.Frame(self)
        self.board_frame.pack()
        
        self.square_size = 50
        
        # Initialize the board buttons with None values
        self.board_buttons = [[None for _ in range(8)] for _ in range(8)]
        
        # Create 8x8 buttons
        for row in range(8):
            for col in range(8):
                button = tk.Button(self.board_frame, width=4, height=2,
                            command=lambda r=row, c=col: self.controller.handle_square_click(r, c))
                button.grid(row=row, column=col, padx=2, pady=2)
                self.board_buttons[row][col] = button
        
        # Game board initial state (4 pieces in the middle)
        self.controller.reset_game()
        
        # Update the board ui
        self.update_board_display(self.controller.get_board())
    
    def update_board_display(self, board):
        # Update the board display based on the game state
        for row in range(8):
            for col in range(8):
                current_value = board[row][col]
                color = None
                
                if current_value == "B":
                    color = "black"
                elif current_value == "W":
                    color = "white"
                else:
                    color = "green"
                
                # Update the button background color
                self.board_buttons[row][col].config(bg=color)
    
    def display_winner(self, winner):
        # Display the winner 
        messagebox.showinfo("Game Over", f"The winner is: {winner}")
