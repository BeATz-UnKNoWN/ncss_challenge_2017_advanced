maze=[]
DIR=[(-1,0),(0,-1),(1,0),(0,1)]
with open("maze.txt",'r') as f:
  for line in f.readlines():maze.append([c for c in line.strip()])

ghostLocations=[]
for row in range(0,len(maze)):
  for col in range(0,len(maze[row])):
    if maze[row][col]=='G':
      ghostLocations.append((row,col))
    elif maze[row][col]=='P':
      target = (row,col)

firstMoves=[]
      
for ghost in ghostLocations:
  todo=[[ghost]]
  while len(todo)>0:
    currPath = todo[0]
    if currPath[-1]!=target:
      todo.pop(0)
      for path in DIR:
        row=currPath[-1][0]+path[0]
        col=currPath[-1][1]+path[1]
        if maze[row][col]!='#' and ((row,col) not in currPath):
          newPath=currPath[:]
          newPath.append((row,col))
          todo.append(newPath)
    else:
      firstMoves.append(todo[0][1])
      break;
      
for row,col in ghostLocations:maze[row][col]=' '
for row,col in firstMoves:maze[row][col]='G'
  
for row in maze:print(''.join(row))