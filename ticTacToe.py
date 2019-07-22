# Functions
#################################################################

# Prints the current tic tac toe board
def printBoard():
  print()
  print(' ' + board[0] + ' ' + '|' + ' ' + board[1] + ' ' + '|' + ' ' + board[2] + ' ')
  print('-----------')
  print(' ' + board[3] + ' ' + '|' + ' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ')
  print('-----------')
  print(' ' + board[6] + ' ' + '|' + ' ' + board[7] + ' ' + '|' + ' ' + board[8] + ' ')
  print()
  
# Takes the input of both users 
def inputPosition(player):
  position = int(input(player + ': Choose your next position: (1 - 9): '))
  if(player == 'Player 1' and board[position - 1] == ' '):
    board[position - 1] = p1
    return False
  elif(player == 'Player 2' and board[position - 1] == ' '):
    board[position - 1] = p2
    return False
  else:
    return True
  
# Checks if a user has won the particular round
def checkWinner():
  if (board[0] == board[1] and board[0] == board[2]):
    winner = board[0]
  elif (board[3] == board[4] and board[3] == board[5]):
    winner = board[3]
  elif (board[6] == board[7] and board[6] == board[8]):
    winner = board[6]
  elif (board[0] == board[3] and board[0] == board[6]):
    winner = board[0]
  elif (board[1] == board[4] and board[1] == board[7]):
    winner = board[1]
  elif (board[2] == board[5] and board[2] == board[8]):
    winner = board[2]
  elif (board[0] == board[4] and board[0] == board[8]):
    winner = board[0]
  elif (board[2] == board[4] and board[2] == board[6]):
    winner = board[2]
  else:
    winner = ' '
    
  if (p1 == winner):
    print('The winner is Player 1')
    print()
    return True
  elif (p2 == winner):
    print('The winner is Player 2')
    print()
    return True
  else:
    return False
    
# Main
#################################################################

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
p1 = ' '
p2 = ' '
p1_input = ' '
p2_input = ' '

print('Welcome to Tic Tac Toe!')
print()

p1 = input('Player 1: Do you want to be X or O? ')

if (p1 == 'X'):
  p2 = 'O'
else:
  p2 = 'X'

print()
validation = input('Are you ready to play? Enter Yes or No. ')
print()
print('=======================================')
print()

while (validation == 'Yes'):
  validInput = True 
  while (validInput):
    validInput = inputPosition('Player 1')
  
  printBoard()
  check = checkWinner()
  
  if(check == True):
    break
    
  validInput = True
  while (validInput):
    validInput = inputPosition('Player 2')
  printBoard()
  check = checkWinner()
  
  if(check == True):
    break
    
print()
print('=======================================')
print()
  
