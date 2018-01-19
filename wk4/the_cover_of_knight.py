length = int(input("Size: "))
maxMoves = int(input("Moves: "))
knightX, knightY = input("Knight: ").split(',')
DIRECTIONS = [(1,2),(2,1),(-1,-2),(-2,-1),(1,-2),(2,-1),(-1,2),(-2,1)]

def draw(grid, kx, ky, moves):
  if grid[kx][ky]=='.' or maxMoves+1-moves < int(grid[kx][ky]):
    grid[kx][ky]=str(maxMoves-moves)
    if moves > 0:
      for x,y in DIRECTIONS:
        if -1 < kx+x < length and -1 < ky+y < length:draw(grid,kx+x,ky+y,moves-1)

grid = [['.']*length for i in range(length)]
draw(grid, int(knightX), int(knightY), maxMoves)
for row in grid:
  print(' '.join(row))