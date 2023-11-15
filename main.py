import os
from args import get_args

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self, file=None):
        for row in self.board:
            row_str = " | ".join(row)
            print(row_str, file=file)
            print("-" * 9, file=file)

    # TODO: Implement the check_winner() and is_board_full() methods below
    # check_winner() should return True if there is a winner, and False otherwise
    def check_winner(self):

        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True  # Row win
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True  # Column win
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True  # Diagonal win
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True  # Diagonal win
        return False

    # is_board_full() should return True if the board is full, and False otherwise
    def is_board_full(self):
        
        #*************add your code here*************
        for row in range(3):
            for col in range(3):
                if self.board[row][col]==' ': return False
        return True  # Board is full









        #*************end your code here*************
    
    import os
from args import get_args
 
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
 
    def print_board(self, file=None):
        for row in self.board:
            row_str = " | ".join(row)
            print(row_str, file=file)
            print("-" * 9, file=file)
 
    def check_winner(self):
        for player in ['X', 'O']:
            for i in range(3):
                status = True
                for j in range(3):
                    if self.board[i][j]!=player: status = False
                if status: return True
                status=True
                for j in range(3):
                    if self.board[j][i]!=player: status = False
                if status: return True
                status=True
                for i in range(3):
                    if self.board[i][i]!=player: status=False
                if status: return True
                status=True
                for i in range(3):
                    if self.board[i][2-i]!=player: status=False
                if status: return True
                status=True
        return False
 
    def is_board_full(self):
        full=True
        for i in range(3):
            for j in range(3):
                if (self.board[i][j]==' '): full=False
        return full
    
    def play_game(self, input_file, output_file):
        win = None
        with open(input_file, "r") as f:
            for line in f.readlines():
                try:
                    a, b = line.split(' ')
                    a = int(a)-1; b = int(b)-1
                    if (a>2 or a<0 or b>2 or b<0): continue
                except:
                    break
                self.board[a][b] = self.current_player
                if self.check_winner():
                    win = self.check_winner()
                    break
                if self.is_board_full(): break
                self.current_player = 'X' if self.current_player=='O' else 'O'
 
        with open(output_file, "w+") as r:
            self.print_board(r)
            if win: print(f'Player {self.current_player} wins!', file=r)
            else: print("It's a draw!", file=r)
 
if __name__ == "__main__":
    args = get_args()
    input_folder = args.input_dir  # 輸入資料夾的名稱
    output_folder = args.output_dir  # 輸出資料夾的名稱
 
    for filename in os.listdir(input_folder):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        game = TicTacToe()
        game.play_game(input_file, output_file)
        if not os.path.exists("check_functions"):
            os.makedirs("check_functions")
        with open("check_functions/" + filename, 'w') as f:
            print(game.check_winner(), file=f)
            print(game.is_board_full(), file=f)