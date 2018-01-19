def board_is_happy(board):
  n = len(board)
  for row in range(n):
    for col in range(n):
      x,y = row,col
      #bulb line check
      if board[row][col] == 'L':
        while x < n-1 and (board[x][y] == '.' or board[x][y]=='L'):
          x+=1
          if board[x][y] == 'L': return False
        x,y = row,col
        while x > 0 and (board[x][y] == '.' or board[x][y]=='L'):
          x-=1
          if board[x][y] == 'L': return False
        x,y = row,col
        while y < n-1 and (board[x][y] == '.' or board[x][y]=='L'):
          y+=1
          if board[x][y] == 'L': return False
        x,y = row,col
        while y > 0 and (board[x][y] == '.' or board[x][y]=='L'):
          y-=1;
          if board[x][y] == 'L': return False
      #touching bulbs check
      elif board[row][col].isdigit():
        count = 0
        if row < n-1 and board[row+1][col] == 'L': count += 1
        if row > 0 and board[row-1][col] == 'L': count += 1
        if col < n-1 and board[row][col+1] == 'L':count += 1
        if col > 0 and board[row][col-1] == 'L':count += 1
        if count > int(board[row][col]): return False
  return True  # TODO


def board_is_solved(board):
  n = len(board)
  for row in range(n):
    for col in range(n):
      #touching bulbs check
      if board[row][col].isdigit():
        count = 0
        if row < n-1 and board[row+1][col] == 'L': count += 1
        if row > 0 and board[row-1][col] == 'L': count += 1
        if col < n-1 and board[row][col+1] == 'L': count += 1
        if col > 0 and board[row][col-1] == 'L': count += 1
        if count != int(board[row][col]): return False
      #all lit check
      elif board[row][col] == '.':
        isLit = False
        x,y = row,col
        while x < n-1 and (board[x][y] == '.' or board[x][y]=='L') and not isLit:
          x+=1
          if board[x][y] == 'L': isLit = True
        x,y = row,col
        while x > 0 and (board[x][y] == '.' or board[x][y]=='L') and not isLit:
          x-=1
          if board[x][y] == 'L': isLit = True
        x,y = row,col
        while y < n-1 and (board[x][y] == '.' or board[x][y]=='L') and not isLit:
          y+=1
          if board[x][y] == 'L': isLit = True
        x,y = row,col
        while y > 0 and (board[x][y] == '.' or board[x][y]=='L') and not isLit:
          y-=1;
          if board[x][y] == 'L': isLit = True
        if not isLit: return False
  return True  # TODO


def get_board_state(board):
  if board_is_happy(board):
    if board_is_solved(board):
      return 'solved'
    else:
      return 'happy'
  else:
    return 'unhappy'


if __name__ == '__main__':
  # Example board, happy state.
  print(get_board_state('''
...1.0.
X......
..X.X..
X...L.X
..X.3..
.L....X
L3L2...'''.strip().split('\n')))
  # Example board, solved state.
  print(get_board_state('''
..L1.0.
X...L..
L.X.X.L
X...L.X
..XL3L.
.L....X
L3L2L..'''.strip().split('\n')))
  # Example board, unhappy state.
  print(get_board_state('''
L..1L0.
X.L....
L.X.X.L
X...L.X
..XL3L.
.L....X
L3L2L..'''.strip().split('\n')))
  # Different board, happy state.
  print(get_board_state('''
L1.L.
..L3L
..X1.
.1...
.....'''.strip().split('\n')))
  print(get_board_state('''
.'''.strip().split('\n')))