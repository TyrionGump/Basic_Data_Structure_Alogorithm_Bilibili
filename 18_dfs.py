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

def maze_path(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    while (len(stack) > 0):
        cur_node = stack[-1]
        if cur_node[0] == x2 and cur_node[1] == y2:
            for p in stack:
                print(p)
            return True
        
        for dir in dirs:
            next_node = dir(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                stack.append(next_node)
                maze[next_node[0]][next_node[1]] == 2
                break 
        else:
            maze[cur_node[0]][cur_node[1]] = 2
            stack.pop()

    else:
        print('没有路')

maze_path(1, 1, 8, 8)