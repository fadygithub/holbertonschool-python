#!/usr/bin/python3


def canUnlockAll(boxes):
    keys = [0]
    for key in keys:
        for x in boxes[key]:
            if x < len(boxes):
                if x not in keys:
                    keys.append(x)
    if len(keys) != len(boxes):
        return False
    return True
'''
        if boxes[key] != -999:
            keys += boxes[key]
            boxes[key] = -999

    for x in boxes:
        if x != -999:
            return False
    return True
'''
