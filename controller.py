from model import Model
from view import OthelloView

# The controller class handles the game logic
class OthelloController:
    def __init__(self):
        # Initialize the view
        self.view = OthelloView(self)
        self.difficulty = "Easy"  # Default difficulty level
        
        # GUI loop
        self.view.mainloop()
    
    def set_difficulty(self, difficulty):
        # Set the difficulty level
        self.difficulty = difficulty
    
    def reset_game(self):
        # Initialize the game board with starting positions
        self.board = [["" for _ in range(8)] for _ in range(8)]
        self.board[3][3] = "W"
        self.board[3][4] = "B"
        self.board[4][3] = "B"
        self.board[4][4] = "W"
    
    def handle_square_click(self, row, col):
        print(f"Square clicked at row {row}, column {col}")
        # Handle the square click and update the board state
    
    def get_board(self):
        # Return the current board state
        return self.board

# Start the application
controller = OthelloController()

