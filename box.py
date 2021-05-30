from __future__ import annotations

import json


class Box:

    def __init__(self, height: float, width: float, depth: float) -> None:
        self.height = height
        self.width = width
        self.depth = depth

    def get_volume(self):
        return self.height * self.width * self.width

    def __str__(self):
        return json.dumps(self.__dict__).__str__()

    def __gt__(self, other: Box):
        return self.get_volume() > other.get_volume()

    def __lt__(self, other: Box):
        return self.get_volume() < other.get_volume()

    def __le__(self, other: Box):
        return self.get_volume() <= other.get_volume()

    def __ge__(self, other: Box):
        return self.get_volume() >= other.get_volume()

    def __eq__(self, other: Box):
        return self.get_volume() == other.get_volume()
