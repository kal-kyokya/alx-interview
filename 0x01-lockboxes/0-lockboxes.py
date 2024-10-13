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
    if (type(boxes) != list): return False

    boxes_no = len(boxes)

    if (boxes_no == 1): return True

    return 'In process...'
