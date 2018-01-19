from collections import deque
class BaseEntity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def get_point(self):
        return self.x, self.y
 
    def set_point(self, point):
        self.x, self.y = point
 
class Ghost(BaseEntity):
 
    pass
 
class Pacman(BaseEntity):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.is_dead = False
    pass
 
class EntHolder(list):
    def get_points(self):
        out = set()
        for ent in self:
            out.add((ent.x, ent.y))
        return out
 
class Board:
    def __init__(self, board):
        self.board = board
        # pushes pacman and ghost locations
        self.pac = self.get_pacman()
        self.ghosts = self.get_ghosts()
 
        self.dots = set()
        for y, row in enumerate(self.board):
            for x, item in enumerate(row):
                if item == ".":
                    self.dots.add((x,y))
                if item == "." or item == "P" or item == "G":
                    self.set(x, y, ' ')
 
 
 
        self.rows = len(self.board)
        self.cols = len(self.board[0])
        self.queue = deque()
        self.seen = set()
        self.previous = {}
 
 
        self.pac_points = 0
 
 
 
 
        self.pac_previous = self.pac.get_point()
 
        self.start()
 
    def start(self):
        commands = input("Commands: ").split()
        for com in commands:
            if com != "O":
                if not self.move(com):
                    break
            else:
                print(self)
        else:
            print(self)
 
 
 
    def move(self, dir):
        """moves the pacman, then ticks ghost movement
        returns true if game still goes on, else false"""
        self.move_pac(dir)
        if self.check_won_or_lost():
            return False
        self.move_ghost()
        if self.check_won_or_lost():
            return False
        return True
 
    def check_won_or_lost(self):
        if self.pac.get_point() in self.ghosts.get_points():
            print("You died!")
            self.pac.is_dead = True
            print(self)
            return True
        elif len(self.dots) == 0:
            print("You won!")
            print(self)
            return True
        else:
            return False
 
 
    def move_pac(self, dir):
        prev = self.pac.get_point()
        self.pac_previous = prev
        if dir == 'U':
            # up
            if self.valid((prev[0], prev[1]-1)):
                self.pac.y -= 1
        elif dir == 'D':
            # down
            if self.valid((prev[0], prev[1] + 1)):
                self.pac.y += 1
 
        elif dir == 'R':
            # right
            if self.valid((prev[0] + 1, prev[1])):
                self.pac.x += 1
 
        elif dir == 'L':
            # down
            if self.valid((prev[0] - 1, prev[1])):
                self.pac.x -= 1
 
        else:
            raise Exception("Cmmand cannot be found")
 
        if self.eat():
            self.pac_points += 1
 
    def eat(self):
        # attempts to eat any dots pacman is standing on
        p = self.pac.get_point()
        if p in self.dots and p not in self.ghosts.get_points():
            self.dots.remove(p)
            return True
        else:
            return False
 
 
    def move_ghost(self):
        """Moves the ghost one step to pacman"""
 
        for ghost in self.ghosts:
            ghost.set_point(self.do_bfs(ghost.x, ghost.y, *self.pac_previous))
            if ghost.get_point == (4,0):
                print('pause')
 
 
 
    def in_grid(self, x, y):
        if x < 0 or y < 0:
            return False
        elif x >= self.cols or y >= self.rows:
            return False
        return True
 
    def get_pacman(self):
        for y, row in enumerate(self.board):
            for x, item in enumerate(row):
                if item == "P":
                    return Pacman(x,y)
        raise Exception("Cant find packmens")
 
    def get_ghosts(self):
        out = EntHolder()
        for y, row in enumerate(self.board):
            for x, item in enumerate(row):
                if item == "G":
                    out.append(Ghost(x,y))
        return out
 
    def valid(self, point):
        return self.in_grid(*point) and self.get(*point) != "#"
 
    def get_points(self, x, y):
        """ gets valid points from location"""
        out = []
        # up, left, down, right order
        out.append((x,y-1))
        out.append((x-1, y))
        out.append((x, y+1))
        out.append((x+1, y))
 
        return [i for i in out if self.valid(i)]
 
 
    def get(self, x, y):
        return self.board[y][x]
 
    def set(self, x, y, item):
        self.board[y][x] = item
 
    def __str__(self):
        out = ["Points: {}".format(self.pac_points)]
        ghosts = self.ghosts.get_points()
        for y, row in enumerate(self.board):
            r = []
            for x, item in enumerate(row):
                pac = self.pac.get_point()
                if pac == (x,y) and self.pac.is_dead:
                    r.append("X")
                elif self.pac.get_point() == (x,y):
                    r.append("P")
                elif (x,y) in ghosts:
                    r.append("G")
 
                elif (x,y) in self.dots:
                    r.append('.')
 
                else:
                    r.append(item)
            out.append("".join(r))
        return "\n".join(out)
 
 
    def do_bfs(self, startx, starty, endx, endy):
        '''
        Does a bfs, and returns the first step of said bfs
        '''
        self.queue.clear()
        self.seen.clear()
        self.previous.clear()
 
        self.queue.append((startx,starty))
 
 
 
        end = (endx, endy)
        start = (startx, starty)
 
        while self.queue:
 
            curr = self.queue.popleft()
            for i in self.get_points(*curr):
 
 
                if i not in self.seen:
                    self.previous[i] = curr
                    self.seen.add(i)
                    self.queue.append(i)
                    if end == i:
                        self.queue.clear()
 
        # sliding window
        # 2nd last, last
       # try:
        curr = end
        prev = self.previous[curr]
        #except:
        #    print(startx, starty, endx, endy)
       #     print(self)
        #    raise
 
        while prev != start:
            curr = prev
            prev = self.previous[curr]
 
        return curr
 
 
 
 
 
 
with open("maze.txt") as f:
    y = [list(r.strip("\n")) for r in f.readlines()]
    board = Board(y)