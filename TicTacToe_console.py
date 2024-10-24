

"""TicTacToe console game Module
Developer: Daniel Fatokun (DannyPy)
Date:      12th March 2024.
status:.   Productive"""

__version__ = "0.5.0"

__author__ = "DannyPy"
__date__ = "12th March 2024"


class TicTacToe:
    """class TicTacToe.
    
    class attributes:
    ----------------
         BOARD_WIDTH(int): the witdh of the TicTacToe board.  
         
    Class Methods here:
    ------------------
        - get_row_col_text:
            get the text in the specified grid (row, column, or diagonal ).
        - get_row_text:
            get and return row text which has 3 Xs or 3 0s otherwise [].
        - get_column_text:
            get and return column text which has 3 Xs or 3 0s otherwise [].
        - get_both_diagonals:
            get and return any of the diagonal text which has 3 Xs or 3 0s otherwise [].
        - restart:
            restart the game. 
        - prepare_reatart:
            ask question before restarting. 
        - check_win:
            check for any row, column, or diagonal with 3 Xs or 0s and declare winner. 
        - get_new_player:
            switch players. 
    """
    
    BOARD_WIDTH = 10
    assert BOARD_WIDTH >=8, "Board width less than 8."
    assert BOARD_WIDTH <= 16, "Board width greater than 16."
    def __init__(self):
        """class constructor
        Attributes:
          - grid(list): 3x3 grid.
          - grid_value(dict): all grid with default value{gird: " "*7} 
          - current_player(bool): to track the next player.
          - chosen_board(list): list of all boards that has been chosen
          - fist_bord(bool): if true, print empty board"""
        self.grids = [(x, y) for x in range(3) for y in range(3)]
        self.grid_value = {}.fromkeys(self.grids, " "*TicTacToe.BOARD_WIDTH)
        self.current_player = True
        
        self.chosen_board = []
        self.first_board = True
        
        
    def get_row_col_text(self, row=False, column=False, is_diagonal=False):
        """get the text in the specified grid(row, column, or diagonal ).
        param:
          - row(bool)->False: if set to True, returns list of text in all rows. 
          - column(bool)->False: if set to True, returns list of text in all columns. 
          - is_diagonal(bool)->False: is set to True, returns the list of text in all diagonals."""
        
        if is_diagonal:
            # main diagonal and anti-diagonal
            both_diagonals = [
                [self.grid_value[grid] for grid in self.grid_value if grid[0] == grid[1]],   # mian diagonal 
                [self.grid_value[grid] for grid in self.grid_value if grid[0] + grid[1] == 2]   # anti-diagonal 
            ]
            
            #print("both_diagonals: ", both_diagonals)
            return both_diagonals
            
        if any([row, column]): 
            _all = [
                 [self.grid_value[grid]  for grid in self.grid_value if grid[0 if row else 1] == 0],   # First row or column 
                 [self.grid_value[grid]  for grid in self.grid_value if grid[0 if row else 1] == 1],   # second row or column 
                 [self.grid_value[grid]  for grid in self.grid_value if grid[0 if row else 1] == 2]    # third row or column 
            ]
            return _all
        
    def get_row_text(self):
        """return a row which has len of 3 Xs or 0s out of all columns.
        or: return [] if no row has len of 3 Xs or 0s."""
        
        all_row_text = self.get_row_col_text(row=True)
        
        row_text = [value.strip() for each_row_text in all_row_text for value in each_row_text if each_row_text.count(value) == 3]    
        return row_text 
    
    def get_column_text(self):
        """return a column which has len of 3 Xs or 0s out of all columns.
        or: return [] if no column has len of 3 Xs or 0s."""
        
        all_col_text = self.get_row_col_text(column=True)
        
        col_text = [value.strip() for each_col_text in all_col_text for value in each_col_text if each_col_text.count(value) == 3]    
        #print(f"{col_text = }")
        return col_text 
        
    def get_both_diagonals(self):
        """return a diagonal (antidiagonal(top-right to bottom-left) or main-diagonal(top-left to bottom-right)
        which has len of 3 Xs or 0s out of the two diagonals.
        or: return [] if no diagonal has len of 3 Xs or 0s."""
        
        all_diagonal_text = self.get_row_col_text(is_diagonal=True)
        
        diagonal_text =[value.strip() for each_diagonal_text in all_diagonal_text for value in each_diagonal_text if each_diagonal_text.count(value) == 3]
        #print(f"{diagonal_text = }")
        return diagonal_text
    
    def restart(self):
        """restart the game. Sets the grid_value value to empty string"""
        self.grid_value = {}.fromkeys(self.grids, " "*TicTacToe.BOARD_WIDTH)
        self.chosen_board.clear()
        self.draw_board()
        
    def prepare_reatart(self):
        play_again = input("Play again(y/n): ")
        if play_again == "y":
            self.restart()
        else: exit()
        
    def check_no_win(self):
        all_board = [self.grid_value[grid].strip() for grid in self.grid_value]
        return None if "" in all_board else "\nNo winner."
                
    def check_win(self):
        all_text = [self.get_row_text(), self.get_column_text(), self.get_both_diagonals()]
        # print(all_text)
        for text in all_text:
            if text.count("X") == 3:
                print("\nX player wins!\n")
                self.prepare_reatart()
            elif text.count("0") == 3:
                print("\n0 player wins!\n")
                self.prepare_reatart()
        if self.check_no_win():
            print(self.check_no_win())
            self.prepare_reatart()
        # else: print("\nYou can still make it focus well") # declare a variable to hold more interactive text and choose randomly 
                
    def get_new_player(self):
        """switch players. 
        returns: X if current player is 0 else 0."""
        
        if self.current_player:
            self.current_player = False
            return "X"
        else:
            self.current_player = True
            return "0"
                    
    def draw_board(self, player=""):
        """draws tictactoe board"""
        print()
        
        draw_line = lambda grid, end1, end2: print(self.grid_value[grid], end=f"{end2 if n in (3, 6, 9) else end1}")
        for n, grid in enumerate(self.grid_value, start=1):
           draw_line(grid, "|", "")
           if n in (3, 6, 9):
               print("\n", " - " * (TicTacToe.BOARD_WIDTH ), "\n")  if n != 9 else None
        print() # leave a line 
       
    def get_grid(self, board_num):
        """find the grid of the number inputed."""
        n = 0
        for x in range(3):
            for y in range(3):
                n += 1
                if n == board_num:
                    return (x, y)
            
    def insert_player(self, board_num, player=None):
        right_padding, left_padding = " " * ((TicTacToe.BOARD_WIDTH // 2 -1)), " " * (TicTacToe.BOARD_WIDTH // 2)
        _board = [x for x in range(10)] # {}.fromkeys([x for x in range(10)], "0")
        if board_num in _board: # _board.get(board_num):
            # print(self.get_grid(board_num))
            self.grid_value[self.get_grid(board_num)] = f"{right_padding}{player}{left_padding}"
        else:
            return False if board_num == 0 else (None if board_num == 111 else False)
    
    def repeat_player(self):
        self.get_new_player()
        
    def get_board_num(self, player):
        try: 
            player_board = int(input("\n" + player + " player's turn\nEnter shell(1-9) \'111\' to quit \'222\' to restart\n>> "))
            if player_board in self.chosen_board:
                return "None" # to make decisions different in play_game()
        except ValueError as e: 
            return False
        return player_board
   
    def info(self, msg):
        print(msg)
        self.repeat_player()
    
    def check_exit_restart(self, player):
        if player == 111:
            exit()
        elif player == 222:
           self.restart()
           print("\n","------ Restarted -----\n".center(50))
           
    def play_functions(self, player_board, player):
        """calls some special functions to run validations"""
        self.chosen_board.append(player_board) 
        self.insert_player(player_board, player)
        self.draw_board(player)     
        self.check_win()
        self.check_exit_restart(player_board)
         
    def play_game(self):
        while True:
            self.draw_board() if self.first_board else None
            self.first_board = False
            player = self.get_new_player()
            player_board = self.get_board_num(player)
            
            #print(type(player_board))
            if not player_board:
                self.info("\ninvalid Input try again!\n") if player_board != 222 else None 
                continue 
            elif isinstance(player_board, str):
                self.info(f"\nChosen, please select again!\n") 
                    
            elif self.insert_player(player_board) == False:
                self.info("\nBoard out of range choose (1-9)\n") if player_board != 222 else None
                #continue 
            
            self.play_functions(player_board, player)

a = TicTacToe()
a.play_game()

__import__("time").sleep(55555)
