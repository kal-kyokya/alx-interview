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
    if (type(boxes) != list): return (False)

    # Store the number of available boxes
    boxes_no = len(boxes)

    # Handle single box case
    if (boxes_no == 1): return (True)

    # Ready a variable to hold the keys found in each box
    keys = set()

    # Handle Case of two boxes
    if (boxes_no == 2):
        if len(boxes[0]) == 0: return (False)
        else:
            return (True if (1 in boxes[0]) else False)

    # Case: More than two boxes

    return ('In progress...')
