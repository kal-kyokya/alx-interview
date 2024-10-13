#!/usr/bin/python3
"""
'0-lockboxes' holds a python script that solves a problem involving nested lists.
"""
def canUnlockAll(boxes):
    """Determine whether keys to all boxes were acquired during search.
    Args:
        Boxes: A list whose elements represent keys to boxes.
    Return:
        A boolean; True if all boxes were opened, False otherwise.
    """
    # Ensure that the input is a list of lists
    if (type(boxes) != list or len(boxes) == 0): return (False)

    # Store the number of available boxes
    boxes_no = len(boxes)

    # Handle single box case
    if (boxes_no == 1): return (True)

    # Ready a variable to hold the keys found in each box
    keys = set()

    # Handle Case of two boxes
    if (boxes_no == 2):
        if (len(boxes[0]) == 0): return (False)
        else:
            return (True if (1 in boxes[0]) else False)

    # Case: More than two boxes
    visited = set()
    visiting = 0
    to_visit = []
    for count in range(boxes_no):
        # Access a specific box
        # If any, Extract and Store the keys
        for key in boxes[visiting]:
            keys.add(key)

        if (len(keys) == boxes_no): return (True)
        if (len(keys) == (boxes_no - 1) and 0 not in keys): return (True)

        visited.add(visiting)
        not_visited = list(filter(lambda x: x not in visited, boxes[visiting]))
        to_visit.extend(not_visited)

        if (len(to_visit) == 0): return False

        visiting = to_visit.pop(0)

    return ('In progress...')
