#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened.
    Args:
        boxes: list of lists
    Returns:
        True if all boxes can be opened, else return False
    """
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    v = [False] * n
    v[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not v[key]:
                v[key] = True
                stack.append(key)

    return all(v)
