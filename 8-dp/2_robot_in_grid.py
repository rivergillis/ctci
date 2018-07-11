# Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in 2 directions: right and down, but certain cells are
# off limits such that the robot cannot step onto them. Design an algorithm to find
# a path from the top left to the bottom right.
# 331, 360, 388

# For the robot to reach the last cell, it must find a path to the second-to-last cells. For it to find a path to the second-to-last cells, it must find a path to the third-to-last cells.
# Simplify this problem a bit by first figuring out if there's a path. Then, modify your algorithm to track the path

def robot(rows, columns, bad):
    dead_ends = set(bad)
    print(dead_ends)
    def robot_helper(path):
        current = path[-1]
        if current[0] == rows-1 and current[1] == columns-1:
            return path
        if current in dead_ends:
            return None
        if current[0] >= rows:
            dead_ends.add(current)
            return None
        if current[1] >= columns:
            dead_ends.add(current)
            return None
        right = robot_helper(path + [(current[0] + 1, current[1])])
        if right is not None:
            return right
        down = robot_helper(path + [(current[0], current[1] + 1)])
        if down is not None:
            return down
        dead_ends.add(current)
        return None
    return robot_helper([(0,0)])

if __name__ == '__main__':
    bad = [(0, 1), (2, 0), (2, 2), (4, 2), (3, 3)]
    print(robot(5, 5, bad))