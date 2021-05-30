from state import State
from queue import PriorityQueue
import sys


def get_solving_path(root_state: State) -> list:
    path = []
    visited_queue = []
    priority_queue = PriorityQueue()
    count = 0
    priority_queue.put((0, count, root_state))
    while not path and priority_queue.qsize():
        status = "\rNodes visited: %i" % len(visited_queue)
        sys.stdout.write(status)
        closest_child = priority_queue.get()[2]
        closest_child.create_children()
        visited_queue.append(closest_child.value)
        for child in closest_child.children:
            if child.value in visited_queue:
                continue
            count += 1
            if not child.get_distance():
                path = child.path
                break
            priority_queue.put((child.get_distance(), count, child))
        sys.stdout.flush()
    return path
