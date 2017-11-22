
from random import randint  

class Boat:
  row = 0
  col = 0

  def checkRow(self, guessRow):
    return (self.row == int(guessRow))

  def checkCol(self, guessCol):
    return (self.col ==int(guessCol))

  def print(self):
    print("(", self.row, ", ", self.col, ')')


board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
      print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)
def random_col(board):
  return randint(0, len(board) - 1)


enemyBoat = Boat();
enemyBoat.row = random_row(board)
enemyBoat.col = random_col(board)

enemyBoat.print()



for turn in range(0,5):
  guess_row = input("Guess row: ")
  guess_col = input("Guess col: ")

  if (enemyBoat.checkRow(guess_row) and enemyBoat.checkCol(guess_col)) :
    print("Congratulations! You sunk my battleship!!!")
    break
  else:
    if (int(guess_row) < 0 or int(guess_row) > 4) or (int(guess_col) < 0 or int(guess_col) > 4):
      print("Oops, that's not even in the ocean.")
      if turn == 4:
        print("******Game Over******")  
    elif board[int(guess_row)][int(guess_col)] == "X":
      print("Looks like you've already guessed that one...")
      if turn == 4:
        print("******Game Over******")
    else:
      board[int(guess_row)][int(guess_col)] = "X"
      print("You missed my battleship!")
      if turn == 4:
        print("******Game Over******")
  if turn < 4:
    print("Turn", turn + 1)
    print_board(board)
  elif turn == 4:
    print("Battleship was at " + "Row:" + str(ship_row) + " " + "Column:" + str(ship_col))
