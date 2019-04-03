 print()
 print('-----------------------')
 print('Welcome to Tic Tac Toe!')
 print('-----------------------')
 print()
 player1 = ''
 player2 = ''
 print('Player 1: Do you want to be X or O?')
 # Input the value and set values of player1 and player2
 print('Player 1 will go first.')

 inputVal = ''
 print('Are you ready to play? Enter Yes or No.')
 # Input whether they are ready to player1

board = {1 : ' ', 2 : ' ', 3 : ' ', 4 : ' ', 5 : ' ', 6 : ' ', 7 : ' ', 8 : ' ', 9 : ' '}

 while(inputVal == 'Yes'):
   # Player 1
   printBoard()
   player1Input = 0;
   print('Choose your next position: (1-9)')
   # Input the next position to enter

   flag = True;
   while(flag):
     if (player1Input > 0 and player1Input < 10):
       if board.get(player1Input) != '':
         print('The position already exists')
       else:
         board.set(player1Input, player1)
         flag = False
     else:
       print('The inputed value does not exist between 1 - 9')
  
   evaluateBoard()

   # Player 2
   printBoard()
   player2Input = 0;
   print('Choose your next position: (1-9)')
   # Input the next position to enter

   flag = True;
   while(flag):
     if (player2Input > 0 and player2Input < 10):
       if board.get(player2Input) != '':
         print('The position already exists')
       else:
         board.set(player2Input, player2)
         flag = False
     else:
       print('The inputed value does not exist between 1 - 9')
  
   evaluateBoard()


def printBoard():
    print('-------------------')
    print('| ', board.get(7), ' | ',  board.get(8), ' | ', board.get(9), ' |    ', ' 7 | 8 | 9 ')
    print('-------------------      ----------')
    print('| ', board.get(4), ' | ',  board.get(5), ' | ', board.get(6), ' |    ', ' 4 | 5 | 6 ')
    print('-------------------      ----------')
    print('| ', board.get(1), ' | ',  board.get(2), ' | ', board.get(3), ' |    ', ' 1 | 2 | 3 ')
    print('-------------------')


def evaluateBoard():
  # Need to figure out the evaluating part
