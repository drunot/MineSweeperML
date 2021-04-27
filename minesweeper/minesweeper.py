import random

class Minesweeper():
    """Minesweeper game 
    """

    def __init__(self, height=10, width=10, mines=10):
        """Initialize board with mines

        Args:
            height(int): Height of board (default=10)
            width(int): Width of board (default=10)
            mines(int): Number of mines (default=10)
        """
        self.height = height
        self.width = width
        self.mines = set()
        self.unrevealed = height * width - mines

        # Create board
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(-1)
            self.board.append(row)

        # Initialize mines
        while len(self.mines) != mines:
            x = random.randrange(width)
            y = random.randrange(height)
            self.mines.add((y, x))

    def open_square(self, y, x):
        """'Presses' on a select square

        Args:
            x(int): x-position of square
            y(int): y-position of square
        
        Returns:
            bool: False if a mine was clicked, else True
        """
        mines = 0
        if (y, x) in self.mines:
            return False
        for i in range(y-1, y+2):
            for j in range(x-1, x+2):
                if (i, j) in self.mines:
                    mines += 1
        self.board[y][x] = mines
        self.unrevealed -= 1
        return True
    
    def is_game_won(self):
        return self.unrevealed == 0

    def print_board(self):
        """Prints the board to terminal
        """
        print()
        for row in self.board:
            for square in row:
                print(square, end=' ')
            print()

    def print_board_with_mines(self):
        """Prints the board to terminal with mines marked
        """
        print()
        for (y, row) in enumerate(self.board):
            for (x, square) in enumerate(row):
                if (y, x) in self.mines:
                    print('#', end=' ')
                else: 
                    print(square, end=' ')
            print()
