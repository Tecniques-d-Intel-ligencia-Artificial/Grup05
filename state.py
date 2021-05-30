from __future__ import annotations

import copy


class State:

    def __init__(self, movement_count: int, parent: State, stacks: dict) -> None:
        self.movement_count = movement_count
        self.stacks = stacks
        self.children_states = []
        self.last_moved_box = None
        self.parent = parent

    def __str__(self):
        string = f"Movement count: {self.movement_count}\n"
        for stack_name in self.stacks:
            stack = self.stacks[stack_name]
            string += f"{stack_name}: "
            for box in stack: string += str(box.get_volume()) + ", "
            string += "\n"
        return string

    def __eq__(self, other: State):
        is_equal = True
        for stack_name in self.stacks:
            is_equal = is_equal and self.stacks[stack_name] == other.stacks[stack_name]
        return is_equal


def print_stack(stack: list):
    string = ""
    for box in stack: string += str(box.get_volume()) + ", "
    print(string)


def is_win_state(state: State):
    empty_counter = 0
    sorted_counter = 0

    for stack_name in state.stacks:
        stack = state.stacks[stack_name]
        if not stack:
            empty_counter += 1
            continue
        if sorted(stack, reverse=True) == stack: sorted_counter += 1

    return empty_counter == 2 and sorted_counter == 1


def is_repeated_state(state: State):
    parent = state.parent
    while parent is not None:
        if state == parent: return True
        parent = parent.parent
    return False


def process_state(state: State):
    stacks = state.stacks
    for source_stack_name in stacks:
        source_stack = stacks[source_stack_name]
        if not source_stack: continue
        last_moved_box = state.last_moved_box
        if last_moved_box is not None and source_stack[-1] == last_moved_box: continue
        for destination_stack_name in stacks:
            if destination_stack_name == source_stack_name: continue
            destination_stack = stacks[destination_stack_name]
            if destination_stack and destination_stack[-1] < source_stack[-1]: continue
            stacks_copy = copy.deepcopy(stacks)
            box_to_move = stacks_copy[source_stack_name].pop()
            stacks_copy[destination_stack_name].append(box_to_move)
            new_state = State(state.movement_count + 1, state, stacks_copy)
            new_state.last_moved_box = box_to_move
            state.children_states.append(new_state)


def create_state_tree(root_state: State):
    states = [root_state]
    best_outcome = None
    while states:
        current_state = states.pop(0)
        if is_win_state(current_state) and (
                best_outcome is None or current_state.movement_count < best_outcome.movement_count):
            best_outcome = current_state
            print(best_outcome)
            continue
        if is_repeated_state(current_state): continue
        process_state(current_state)
        for state in current_state.children_states:
            states.insert(0, state)
    print(best_outcome)
