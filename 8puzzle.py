import heapq
import copy

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def heuristic(state):
    total = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                correct_x = (val - 1) // 3
                correct_y = (val - 1) % 3
                total += abs(i - correct_x) + abs(j - correct_y)
    return total


class Node:
    def __init__(self, state, x, y, level, parent):
        self.state = state
        self.x = x
        self.y = y
        self.level = level
        self.parent = parent
        self.cost = level + heuristic(state)

    def __lt__(self, other):
        return self.cost < other.cost


def print_state(state):
    for row in state:
        for value in row:
            print(value, end=" ")
        print()
    print()


def solve(start, x, y):
    pq = []
    first = Node(start, x, y, 0, None)
    heapq.heappush(pq, first)

    visited = set()
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while pq:
        current = heapq.heappop(pq)

        state_key = tuple(tuple(r) for r in current.state)
        if state_key in visited:
            continue
        visited.add(state_key)

        if heuristic(current.state) == 0:
            path = []
            temp = current
            while temp is not None:
                path.append(temp.state)
                temp = temp.parent

            for step in reversed(path):
                print_state(step)
            return

        for dx, dy in directions:
            new_x = current.x + dx
            new_y = current.y + dy

            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = copy.deepcopy(current.state)
                new_state[current.x][current.y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[current.x][current.y]

                child = Node(new_state, new_x, new_y, current.level + 1, current)
                heapq.heappush(pq, child)


start = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

solve(start, 1, 0)