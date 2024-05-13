class Model:
    def __init__(self):
        # define the current player with black piece player
        self.board = [["-" for _ in range(8)] for _ in range(8)]
        self.board[3][3] = "W"
        self.board[3][4] = "B"
        self.board[4][3] = "B"
        self.board[4][4] = "W"
        self.row = 8
        self.col = 8
        self.number_of_human_pieces = 30
        self.number_of_computer_pieces = 30

#================================================================================================================================


    def get_board(self):
        return self.board
    
#================================================================================================================================

    def print_board(self):
        print('  1 2 3 4 5 6 7 8')
        print(' +-+-+-+-+-+-+-+-+')
        for i in range(self.row):
            print(str(i + 1) + '|', end='')
            for j in range(self.col):
                print(self.board[i][j], end='|')
            print('\n +-+-+-+-+-+-+-+-+')

#================================================================================================================================

    def is_valid_move(self, row, col, player):
        if row < 1 or row > 8 or col < 1 or col > 8:
            return False
        if self.board[row - 1][col - 1] != '-':
            return False
        Opponent = 'B' if player == 'W' else 'W'
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        for d in directions:
            x, y = row - 1, col - 1
            x += d[0]
            y += d[1]
            if x >= 0 and x < 8 and y >= 0 and y < 8 and self.board[x][y] == Opponent:
                x += d[0]
                y += d[1]
                while x >= 0 and x < 8 and y >= 0 and y < 8:
                    if self.board[x][y] == player:
                        return True
                    if self.board[x][y] == '-':
                        break
                    x += d[0]
                    y += d[1]
        return False
    
#================================================================================================================================

    def get_valid_moves(self, player):
        valid_moves = []
        for i in range(8):
            for j in range(8):
                if self.is_valid_move(i + 1, j + 1, player):
                    valid_moves.append([i + 1, j + 1])
        return valid_moves
    
#================================================================================================================================

    def GetIndexsOfFlipped(self, row, col, player):
        if (self.is_valid_move(row, col, player) == False):
            return []
        Opponent = 'B' if player == 'W' else 'W'
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        flipped = []
        for d in directions:
            x, y = row - 1, col - 1
            x += d[0]
            y += d[1]
            temp = []
            while x >= 0 and x < 8 and y >= 0 and y < 8 and self.board[x][y] == Opponent:
                temp.append([x, y])
                x += d[0]
                y += d[1]
            if x >= 0 and x < 8 and y >= 0 and y < 8 and self.board[x][y] == player:
                flipped += temp
        return flipped

#================================================================================================================================

    
    def make_move(self, row, col, player, flipped=[]):
        if self.is_valid_move(row, col, player) == False:
            return False
        self.board[row - 1][col - 1] = player
        for i, j in flipped:
            self.board[i][j] = player
        return True

#================================================================================================================================


    # make computer move
    def make_computer_move(self, depth,ComputerPlayercolor , HumanPlayerColor):
        
        # get the best move for the computer using minimax algorithm

        move , _ = self.minimax(depth , -999,999 ,True ,ComputerPlayercolor , HumanPlayerColor)

        # Get the indices of flipped pieces after getting the move

        flipped = self.GetIndexsOfFlipped(move[0], move[1], ComputerPlayercolor)
        
        # Make the move on the board with outflanking

        self.make_move(move[0], move[1], ComputerPlayercolor, flipped)


#================================================================================================================================

    # return the board to the previous state 
    # using in minimax algorithm to undo the move that was made
    def undo_move(self, row, col, flipped):
        self.board[row - 1][col - 1] = '-'  # 
        for i, j in flipped:
            opponent = 'B' if self.board[i][j] == 'W' else 'W'
            self.board[i][j] = opponent


#================================================================================================================================

    # check if the Game is finished or not
    def check_game_over(self):

        if self.number_of_computer_pieces == 0:
            return True
        elif self.number_of_human_pieces == 0:
            return True
        
        # if no valid move for both players

        elif self.get_valid_moves('W') == [] and self.get_valid_moves('B') == []:
            return True
        return False
    

#================================================================================================================================


    def minimax(self, depth, alpha, beta, maximizingPlayer, ComputerPlayerColor, HumanPlayerColor):
        
        # Base case: If depth is 0 or game is over return the utility value of the current state
        if depth == 0 or self.check_game_over():
            if maximizingPlayer:
                return None, self.get_utility(False,HumanPlayerColor)
            else:
                return None, self.get_utility(True,ComputerPlayerColor)

        # Maximizer's turn
        if maximizingPlayer:
            best_move = None
            max_value = -999

            # get all valid moves

            valid_moves = self.get_valid_moves(ComputerPlayerColor)

            # If no valid moves available, return the utility value

            if valid_moves == []:
                _, value = self.minimax(depth - 1, alpha, beta, False, ComputerPlayerColor, HumanPlayerColor)
                return None, value
    
            # loop on all valid moves of the current state and find the best one

            for move in valid_moves:

                # Get the indices of flipped pieces after getting the move
                flipped = self.GetIndexsOfFlipped(move[0], move[1], ComputerPlayerColor)

                # Make the move on the board with outflanking
                self.make_move(move[0], move[1], ComputerPlayerColor, flipped)
                
                # get one piece from the computer pieces
                self.number_of_computer_pieces -=1


                # Recursively evaluate the position after making the move
                # we don't want to need the move returned by this function
                # the importance thing is the current move 
                _, value = self.minimax(depth - 1, alpha, beta, False, ComputerPlayerColor, HumanPlayerColor)


                # Undo the move to revert the board to its previous state
                self.undo_move(move[0], move[1], flipped)
                
                # return the piece to the computer pieces
                self.number_of_computer_pieces +=1

                # Update the maximum value found
                if value > max_value:
                    max_value = value
                    best_move = move
                
                # Update the alpha value 

                alpha = max(alpha, max_value)
                
                # if the beta value is less than or equal to alpha, stop searching
                
                if beta <= alpha:
                    break
            
            # return the best move and the utility value.
            return best_move, max_value

        
        # Minimizer's turn
        
        else:
            best_move = None
            min_value = 999

            # get all valid moves

            valid_moves = self.get_valid_moves(HumanPlayerColor)
            
            # If no valid moves available, return the utility value
            
            if valid_moves == []:
                _, value = self.minimax(depth - 1, alpha, beta, True, ComputerPlayerColor, HumanPlayerColor)
                return None, value 

            # loop on all valid moves of the current state and find the best one

            for move in valid_moves:

                # Get the indices of flipped pieces after getting the move

                flipped = self.GetIndexsOfFlipped(move[0], move[1], HumanPlayerColor)

                # Make the move on the board with outflanking
 
                self.make_move(move[0], move[1], HumanPlayerColor, flipped)

                # get one piece from the human pieces
                self.number_of_human_pieces -=1

                # Recursively evaluate the position after making the move
                # we don't want to need the move returned by this function
                # the importance thing is the current move 
               
                _, value = self.minimax(depth - 1, alpha, beta, True, ComputerPlayerColor, HumanPlayerColor)

                # Undo the move to revert the board to its previous state

                self.undo_move(move[0], move[1], flipped)

                # retrun the piece to the human pieces
                self.number_of_human_pieces +=1
                
                # Update the mimimum value found
                if value < min_value:
                    min_value = value
                    best_move = move


                # Update the beta value 

                beta = min(beta, min_value)

                # if the beta value is less than or equal to alpha, stop searching

                if beta <= alpha:
                    break
            
            # return the best move and the utility value.

            return best_move, min_value


#================================================================================================================================


    def getScores(self , computerPlayerColor):
        computer_count = 0
        human_count = 0

        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] == computerPlayerColor:
                    computer_count += 1
                else:
                    human_count += 1

        
        return computer_count , human_count


#================================================================================================================================

    def get_utility(self,isComputer,color):
        if not isComputer:
            if color == 'B':
                color = 'W'
            else:
                color = 'B'  

        computer_count, human_count = self.getScores(color)

        # if is computer return difference between the number of computer pieces and human pieces
        if isComputer:
            return computer_count - human_count
        
        # else that mean is human return difference between the number of human pieces and computer pieces
        
        else :
            return human_count - computer_count




#================================================================================================================================
    def return_number_of_white_black(self):
        white = 0
        black = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 'W':
                    white += 1
                elif self.board[i][j] == 'B':
                    black += 1
        return white, black


#================================================================================================================================



   