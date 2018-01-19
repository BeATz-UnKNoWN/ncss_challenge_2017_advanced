from collections import deque
class Board:
    def __init__(self, file):
        self.board = list(map(lambda x:list(x.rstrip('\n')), file.readlines()))
        self.cols = max(map(len, self.board))
        for li in self.board:
            if len(li) != self.cols:
                li += list('.' * (self.cols-len(li)))
        self.rows = len(self.board)
        self.used = [[False for i in range(self.cols)] for w in range(self.rows)]
        
    def in_grid(self, x, y):
        if x < 0 or y < 0:
            return False
        elif x >= self.cols or y >= self.rows:
            return False
        return True
      
    def get(self, x, y):
        if self.in_grid(x,y):
            return self.board[y][x]
        else:
            return '.'

    def __str__(self):
        return '\n'.join(((''.join(map(str, row))) for row in self.board))

    def get_points(self, x, y):
        out = [(x, y - 1),(x - 1, y),(x, y + 1),(x + 1, y),(x+1, y+1),(x-1, y+1),(x+1, y-1),(x-1, y-1)]
        return [i for i in out if self.in_grid(*i) and self.get(*i) == '%' and not self.has_used(*i)]
    def bfs(self, x, y):
        seen = set()
        queue = deque()
        queue.append((x,y))
        seen.add((x,y))
        total = 0
        while queue:
            current = queue.popleft()
            self.set_used(*current)
            total += 1
            for point in self.get_points(*current):
                if point not in seen:
                    queue.append(point)
                    seen.add(point)
        return total

    def solve(self):
        patches = 0
        for y, row in enumerate(self.board):
            for x, item in enumerate(row):
                if self.get(x,y) == '%' and not self.has_used(x,y):
                    size = self.bfs(x,y)
                    patches += 1
        return patches

    def has_used(self, x, y):
        return self.used[y][x]
      
    def set_used(self, x, y):
        self.used[y][x] = True

with open('patches.txt') as f:
    b = Board(f)
patches = b.solve()
print(str(patches) + (' patches' if patches != 1 else ' patch'))