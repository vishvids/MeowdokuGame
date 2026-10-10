import random
random.seed(30)

class GameBoard:
    def __init__(self, size = None  ):
        if size == None:
            self.size = 4
        else:
            self.size = size                            # define size
            
        self.board = []
        for i in range(self.size):
            self.board.append(['_'] * self.size)        # make the board with just undescores
        
        #self.solution = [2, 0, 3, 1]                    # define solution  * remover to make random
        self.solution = random.choice([[2, 0, 3, 1],[1, 3, 0, 2]])    # define solution randomly
        
        self.colours = ['B', 'R', 'G', 'Y']             # define colours
        random.shuffle(self.colours)                    # shuffle colours to make it random
        
        self.initialise_board()                         # call initialising to complete the board
    
    def __str__(self):
        return "\n".join("".join(x for x in row) for row in self.board)
        # super cool easy way to genarate the str of board

    def place_initial_colours(self):
        for row_number in range(len(self.solution)):            # iterate through solutions
            self.board[row_number][self.solution[row_number]] = self.colours[row_number]    #change
            
    def expand_region(self, row, col, colour):                   
        for row_num in range(len(self.board)):                  # iterate through every row
            for col_num in range(len(self.board)):              # iterate through every possition
                if abs(row_num - row)<=1 and abs(col_num - col) <= 1 and self.board[row_num][col_num]=='_':  # check neighbourhood
                    self.board[row_num][col_num] = colour       # change
        
    def initialise_board(self):
        self.place_initial_colours()                            # call the methode
        for i in range(self.size):
            self.expand_region(i, self.solution[i], self.colours[i])    # call expand region through the answer list
        #print (self.board)
    
    def check_guess(self, row, col):
        if self.board[row][col] == "C" or self.board[row][col] == "X":  # return none if already selecter answer
            return None
        
        elif self.solution[row] == col:                                 # return true if correctly guessed and change colour to C
            self.board[row][col] = "C"
            return True
        else:
            self.board[row][col] = "X"                                  # return false if wrong answer and change colour to X
            return False
            


class MeowdokuGame:
    def __init__(self, size = 4):                       # initial game definitions
        self.guesses = 0
        self.num_cats_found = 0
        self.size = size
        self.board = GameBoard (size)
        
    def all_cats_found(self):
        return self.size == self.num_cats_found         # checking whether all done or not
    
    def get_valid_position(self, prompt):               # take valid input locations
        while True:
            inp = input(prompt)
            try:
                inpu = int(inp)
            except ValueError:
                continue
            else:
                if  inpu < 0 or inpu > self.size-1:     # checking whether location is in board
                    continue
                else:
                    return inpu
        
    def play(self):
        
        while self.all_cats_found() == False:                   # iterate if all not guessed correctry yet
            print(self.board)
            row = self.get_valid_position("Enter Row: ")
            col = self.get_valid_position("Enter Column: ")
            self.guesses += 1
            check = self.board.check_guess(row, col)
            if check == None:
                print("Position already guessed!")
            elif check == True:
                print("Correct!")
                self.num_cats_found += 1
            else:
                print( "No cat there!")
                
        print("Congratulations!")                               # after all iterations and correct guesses, end game 
        print(f"Number of guesses: {self.guesses}")

