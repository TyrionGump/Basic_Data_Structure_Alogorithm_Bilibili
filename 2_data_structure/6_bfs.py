from collections import deque


maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

dirs = [lambda x,y: (x+1, y), lambda x,y: (x-1, y), lambda x,y: (x, y+1), lambda x,y: (x, y-1)]


def print_r(path):
    cur_node = path[-1]
    real_path = []

    while cur_node[2] != -1:
        real_path.append(cur_node[0:2])
        cur_node = path[cur_node[2]]
    real_path.append(cur_node[0:2]) #  起点
    real_path.reverse()
    print(real_path)

def maze_path(x1, y1, x2, y2):
    queue = deque()
    # 记录节点坐标和该节点的父节点
    queue.append((x1, y1, -1))
    path = []
    while queue:
        cur_node = queue.popleft()
        maze[cur_node[0]][cur_node[1]] == 2
        path.append(cur_node)
        if cur_node[0] == x2 and cur_node[1] == y2:
            print_r(path)
            return
        for dir in dirs:
            next_node = dir(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                queue.append((next_node[0], next_node[1], len(path) - 1))
                
        

maze_path(1, 1, 8, 8)
