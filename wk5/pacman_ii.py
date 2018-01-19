maze=[]
DIR=[(-1,0),(0,-1),(1,0),(0,1)]
with open("maze.txt",'r') as f:
  for line in f.readlines():maze.append([c for c in line.strip()])

ghostLocations,pacDots=[],[]
for row in range(0,len(maze)):
  for col in range(0,len(maze[row])):
    if maze[row][col]=='.':
      pacDots.append((row,col))
    elif maze[row][col]=='G':
      ghostLocations.append((row,col))
    elif maze[row][col]=='P':
      pac=pacPrev=(row,col)
maxPoints=len(pacDots)
firstMoves=[]

def moveGhosts():
  dead=False
  newLocations,overlap=[],[]
  global ghostLocations
  for ghost in ghostLocations:
    todo=[[ghost]]
    while len(todo)>0:
      currPath = todo[0]
      if currPath[-1]!=pacPrev:
        todo.pop(0)
        for path in DIR:
          row=currPath[-1][0]+path[0]
          col=currPath[-1][1]+path[1]
          if maze[row][col]!='#' and ((row,col) not in currPath):
            todo+=[currPath+[(row,col)]]
      else:
        maze[ghost[0]][ghost[1]] = '.' if ghost in pacDots else 'G' if ghost in overlap else ' '
        if maze[currPath[1][0]][currPath[1][1]]=='P' or maze[currPath[1][0]][currPath[1][1]]=='X':
          maze[currPath[1][0]][currPath[1][1]]='X'
          dead=True
        elif maze[currPath[1][0]][currPath[1][1]]=='G':overlap.append(currPath[1])
        else:maze[currPath[1][0]][currPath[1][1]]='G'
        newLocations.append(currPath[1])
        break;
  ghostLocations=[x for x in newLocations]
  return dead
        
def printBoard(message):
  if message=='':'''do nothing'''
  else:print(message)
  print("Points:",str(maxPoints-len(pacDots)))
  for row in maze:print(''.join(row))
  
toPrint=True
for cmd in input("Commands: ").split():
  moved=True
  if cmd=='U':i=0
  elif cmd=='L':i=1
  elif cmd=='D':i=2
  elif cmd=='R':i=3
  elif cmd=='O':printBoard('');continue
  pac=tuple(map(lambda x, y: x + y, pacPrev, DIR[i]))
  if maze[pac[0]][pac[1]]=='#':moved=False
  else:
    maze[pacPrev[0]][pacPrev[1]]=' '
    if maze[pac[0]][pac[1]]=='G':maze[pac[0]][pac[1]]='X';printBoard('You died!');toPrint=False;break
    elif maze[pac[0]][pac[1]]=='.':pacDots.remove(pac);maze[pac[0]][pac[1]]='P'
    else:maze[pac[0]][pac[1]]='P'
    if len(pacDots)==0:printBoard('You won!');toPrint=False;break
  dead=moveGhosts()
  if dead:printBoard('You died!');toPrint=False;break
  if len(pacDots)==0:printBoard('You won!');toPrint=False;break
  if moved:pacPrev=pac
    
if toPrint:printBoard('')