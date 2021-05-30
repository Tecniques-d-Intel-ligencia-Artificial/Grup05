from __future__ import annotations

import copy


class State:

    def __init__(self, value, parent=None, goal=None):
        self.children = []
        self.parent = parent
        self.value = value

        if parent is not None:
            self.path = parent.path[:]
            self.path.append(value)
            self.goal = parent.goal
        else:
            self.path = [value]
            self.goal = goal

    def get_distance(self):
        pass

    def create_children(self):
        pass


class HanoiState(State):

    def __init__(self, value, parent=None, goal=None):
        super(HanoiState, self).__init__(value, parent, goal)

    def get_distance(self):
        if self.value["Stack C"] == self.goal["Stack C"]:
            return 0
        distance = len(self.goal["Stack C"])
        for index, box in enumerate(self.value["Stack C"]):
            if self.goal["Stack C"][index] == box:
                distance -= 1
        return distance

    def create_children(self):
        if self.children:
            return
        for source_key in self.value:
            source_stack = self.value[source_key]
            if not source_stack:
                continue
            for destination_key in self.value:
                if source_key == destination_key:
                    continue
                destination_stack = self.value[destination_key]
                if destination_stack and destination_stack[-1] < source_stack[-1]:
                    continue
                value = copy.deepcopy(self.value)
                value[destination_key].append(value[source_key].pop())
                child = HanoiState(value=value, parent=self)
                self.children.append(child)
