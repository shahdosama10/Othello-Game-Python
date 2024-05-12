from player import Player



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

    def get_board(self):
        return self.board
    def print_board(self):
        print('  1 2 3 4 5 6 7 8')
        print(' +-+-+-+-+-+-+-+-+')
        for i in range(self.row):
            print(str(i + 1) + '|', end='')
            for j in range(self.col):
                print(self.board[i][j], end='|')
            print('\n +-+-+-+-+-+-+-+-+')

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
    def get_valid_moves(self, player):
        valid_moves = []
        for i in range(8):
            for j in range(8):
                if self.is_valid_move(i + 1, j + 1, player):
                    valid_moves.append([i + 1, j + 1])
        return valid_moves
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
    def make_move(self, row, col, player, flipped=[]):
        if self.is_valid_move(row, col, player) == False:
            return False
        self.board[row - 1][col - 1] = player
        for i, j in flipped:
            self.board[i][j] = player
        return True

    # make computer move
    def make_computer_move(self, ComputerPlayercolor):
        move = self.get_valid_moves(ComputerPlayercolor)[0]
        flipped = self.GetIndexsOfFlipped(move[0], move[1], ComputerPlayercolor)
        self.make_move(move[0], move[1], ComputerPlayercolor, flipped)
    def minimax(self):
        pass

    def get_utility(self):
        pass