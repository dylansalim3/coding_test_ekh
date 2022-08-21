import sys
import collections


#
def bfs(maze, start, maxX, maxY):
    wall, clear, goal = "#", ".", "S"
    width, height = maxY, maxX
    queue = collections.deque()
    queue.append(start)
    seen = set([start])
    counter = 0
    while queue:
        path = queue.popleft()
        x, y = path
        if maze[y][x] == goal:
            if y - start[0] > 1:
                counter = maxY + maxX - start[1] + 1
            elif x - start[1] > 1:
                counter = maxX + maxY - start[0] + 1
            else:
                counter = -1

        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):  # directions
            if (0 <= x2 < width and  # X-axis in range
                    0 <= y2 < height and  # y-axis
                    maze[y2][x2] != wall and  # not a wall
                    (x2, y2) not in seen):  # not visited
                queue.append((x2, y2))
                seen.add((x2, y2))
            elif (0 <= x2 < width and  # X-axis in range
                  0 <= y2 < height and  # y-axis
                  maze[y2][x2] == wall and  # is a wall
                  (x2, y2) not in seen):  # not visited
                # draw a line to block the road
                wallQueue = collections.deque()

                for x3 in range(0, x2):
                    if maze[y2][x3] == wall:
                        counter += 1

                for y3 in range(0, y2):
                    if maze[y3][x2] == wall:
                        counter += 1

    return counter


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    mat = []
    maxX = 0
    maxY = 0
    start = (0, 0)
    for i, v in enumerate(lines):
        if i == 0:
            v = v.replace(" ", "")
            maxX, maxY = int(v[0]), int(v[1])
        if i != 0:
            innerList = list(v)
            innerLine = []
            for j, g in enumerate(innerList):
                innerLine.append(g)
                if g == "H":
                    start = (i-1, j)
            mat.append(innerLine)
    ans = 0 if mat[0][0] == 0 else bfs(mat, start, maxX,
                                       maxY)  # check if start(0,0) is walkable or not if not return False else Run BFS
    print(ans)  # if path exist it will print True else prints False


with open("sample_input1.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
main(lines)
