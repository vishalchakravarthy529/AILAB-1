import heapq

class State:
    def __init__(self, monkey, box, on_box, has_banana, level, parent, action):
        self.monkey = monkey
        self.box = box
        self.on_box = on_box
        self.has_banana = has_banana
        self.level = level
        self.parent = parent
        self.action = action
        self.cost = level + self.heuristic()

    def heuristic(self):
        if self.has_banana:
            return 0
        h = 0
        if self.monkey != "room":
            h += 1
        if self.box != "banana":
            h += 1
        if not self.on_box:
            h += 1
        return h

    def __lt__(self, other):
        return self.cost < other.cost


def print_path(node):
    steps = []
    while node:
        if node.action:
            steps.append(node.action)
        node = node.parent

    for step in reversed(steps):
        print(step)
    print("Monkey got the banana")


def solve():
    start = State("outside", "corner", False, False, 0, None, None)
    pq = []
    heapq.heappush(pq, start)

    visited = set()

    while pq:
        current = heapq.heappop(pq)

        state_tuple = (current.monkey, current.box, current.on_box, current.has_banana)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if current.has_banana:
            print_path(current)
            return

        if current.monkey == "outside":
            new_state = State("room", current.box,
                              current.on_box, current.has_banana,
                              current.level + 1, current,
                              "Monkey enters the room")
            heapq.heappush(pq, new_state)

        elif current.monkey == "room" and current.box != "banana":
            new_state = State("banana", "banana",
                              current.on_box, current.has_banana,
                              current.level + 1, current,
                              "Monkey pushes the box under the banana")
            heapq.heappush(pq, new_state)

        elif current.monkey == "banana" and not current.on_box:
            new_state = State(current.monkey, current.box,
                              True, current.has_banana,
                              current.level + 1, current,
                              "Monkey climbs the box")
            heapq.heappush(pq, new_state)

        elif current.on_box and not current.has_banana:
            new_state = State(current.monkey, current.box,
                              current.on_box, True,
                              current.level + 1, current,
                              "Monkey takes the banana")
            heapq.heappush(pq, new_state)


solve()