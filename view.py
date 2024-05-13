import tkinter as tk
from tkinter import messagebox


class OthelloView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.board_size = 8
        self.controller = controller
        self.title("Othello")

        # The currect state is menu
        self.state = "menu"
        # Initialize the menu screen
        self.create_menu_screen()

    def create_menu_screen(self):

        self.title("Othello")
        self.configure(background="#2c3e50")
        text_color = "#ecf0f1"
        button_color = "#3498db"
        selected_button_color = "#2980b9"
        self.geometry("400x200")
        self.eval('tk::PlaceWindow . center')
        difficulty_label = tk.Label(self, text="Select Difficulty:", fg=text_color, bg="#2c3e50",
                                    font=("Helvetica", 14))
        difficulty_label.pack(pady=10)
        self.difficulty_var = tk.StringVar(value="Easy")
        difficulties = ["Easy", "Medium", "Hard"]
        for difficulty in difficulties:
            radio_button = tk.Radiobutton(self, text=difficulty, variable=self.difficulty_var, value=difficulty,
                                          fg=text_color, bg="#2c3e50", font=("Helvetica", 12),
                                          selectcolor=selected_button_color, activeforeground=text_color,
                                          activebackground=button_color, relief=tk.FLAT)
            radio_button.pack(anchor='w')
        start_button = tk.Button(self, text="Start Game", command=self.start_game, fg=text_color, bg=button_color,
                                 font=("Helvetica", 14), relief=tk.FLAT, activeforeground=text_color,
                                 activebackground=selected_button_color)
        start_button.pack(pady=20)

    def start_game(self):
        self.controller.set_difficulty(self.difficulty_var.get())
        # Message box to choose the player color
        player_color = messagebox.askquestion("Player Color", "Do you want to play as Black?")
        if player_color == "yes":
            self.controller.HumanPlayer.color = "B"
            self.controller.ComputerPlayer.color = "W"
        else:
            self.controller.HumanPlayer.color = "W"
            self.controller.ComputerPlayer.color = "B"

        self.state = "game"
        # input to choose the player color
        # Initialize the game board
        self.create_game_board()
        if self.controller.HumanPlayer.color == "W":
            #####################################
            self.after(100, self.controller.make_computer_move(self.controller.ComputerPlayer.color))
            self.board = self.controller.get_board()
            self.update_board_display(self.board)
            self.controller.ComputerPlayer.number_of_pieces -= 1

    def create_game_board(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.title("Othello")
        self.configure(background="#2c3e50")
        self.geometry("400x450")
        self.eval('tk::PlaceWindow . center')
        self.canvas = tk.Canvas(self, width=400, height=400, bg="#2c3e50")
        whiteplayer = "Human" if self.controller.HumanPlayer.color == "W" else "Computer"
        blackplayer = "Computer" if self.controller.HumanPlayer.color == "W" else "Human"
        self.white = tk.Label(self, text="White: 2 " + whiteplayer, fg="white", bg="#2c3e50", font=("Helvetica", 14))
        self.white.pack()
        self.black = tk.Label(self, text="Black: 2 " + blackplayer, fg="black", bg="#2c3e50", font=("Helvetica", 14))
        self.black.pack()
        self.canvas.pack()
        for i in range(8):
            self.canvas.create_line(i * 50, 0, i * 50, 400, fill="white")
            self.canvas.create_line(0, i * 50, 400, i * 50, fill="white")
        self.canvas.bind("<Button-1>", self.on_click)
        self.board = self.controller.get_board()
        self.update_board_display(self.board)

    def on_click(self, event):
        x, y = event.x, event.y
        i, j = x // 50, y // 50
        self.controller.make_move(i, j)

    def update_board_display(self, board):
        valid_moves = self.controller.model.get_valid_moves(self.controller.HumanPlayer.color)
        whiteplayer = "Human" if self.controller.HumanPlayer.color == "W" else "Computer"
        blackplayer = "Computer" if self.controller.HumanPlayer.color == "W" else "Human"
        [w, b] = self.controller.model.return_number_of_white_black()
        self.white.config(text="White: " + str(w) + " " + whiteplayer)
        self.black.config(text="Black: " + str(b) + " " + blackplayer)
        for i in range(self.board_size):
            for j in range(self.board_size):
                if board[i][j] == "B":
                    x, y = i * 50 + 25, j * 50 + 25
                    self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="black")
                elif board[i][j] == "W":
                    x, y = i * 50 + 25, j * 50 + 25
                    self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="white")
                else:
                    if [i + 1, j + 1] in valid_moves:
                        x, y = i * 50 + 25, j * 50 + 25
                        self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="", outline="gray", dash=(4, 4))
                    else:
                        x, y = i * 50 + 25, j * 50 + 25
                        self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="#2c3e50", outline="#2c3e50")

    def Win(self, Player):
        messagebox.showinfo("Game Over", f"{Player} wins!")
        self.quit()

    def Tie(self):
        messagebox.showinfo("Game Over", "It's a tie!")
        self.quit()

    def InvalidMove(self):
        messagebox.showinfo("Invalid Move", "Invalid Move!")

    def NoMove(self, Player):
        messagebox.showinfo("No Move", "player that has no move is the player has the color: " + Player)

    def GameOver(self, HumanPlayer, ComputerPlayer):
        board = self.controller.get_board()
        player1 = 0
        player2 = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == HumanPlayer.color:
                    player1 += 1
                elif board[i][j] == ComputerPlayer.color:
                    player2 += 1
        if player1 > player2:
            self.Win("Human")
        elif player1 < player2:
            self.Win("Computer")
        else:
            self.Tie()

