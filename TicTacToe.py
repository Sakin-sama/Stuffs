import random

class TicTacToe():
    def __init__(self):
        self.board = []
    def create_board(self):
        for x in range(3):
            row = []
            for m in range(3):
                row.append('-')
            self.board.append(row)
    def get_random_first_player(self):
        return random.randint(0,1)
    def fix_spot(self, row, column, player_marker):
        self.board[row][column] = player_marker
    def is_player_win(self, player_marker):
        win_indicator = None
        n = len(self.board)
        
        for o in range(n):
            win_indicator = True
            for p in range(n):
                if self.board[o][p] != player_marker:
                    win_indicator = False
                    break
            if win_indicator == True:
                return win_indicator
        
        for i in range(n):
            win_indicator = True
            for j in range(n):
                if self.board[j][i] != player_marker:
                    win_indicator = False
                    break
            if win_indicator == True:
                return win_indicator
        
        win_indicator = True
        for x in range(n):
            if self.board[x][n-1-x] != player_marker:
                win_indicator = False
                break
        if win_indicator:
            return win_indicator
        return False
    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True
    def swap_player_turn(self, player_marker):
        return 'X' if player_marker == 'O' else 'O'
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end = " ")
            print()
    def start(self):
        self.create_board()
        player_marker = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"player {player_marker} turn")
            self.show_board()
            row, column = list(map(int, input("ENter row and column to fix spot").split()))
            self.fix_spot(row-1,column-1,player_marker)
            if self.is_player_win(player_marker):
                print(f"Player {player_marker} wins")
                break
            if self.is_board_filled():
                print("Match Draw")
                break
            player_marker = self.swap_player_turn(player_marker)
        print()
        self.show_board()
        
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
