#!/usr/bin/python3


def canUnlockAll(boxes):
    keys_list = [0]
    for k in keys_list:
        for x in boxes[k]:
            if x < len(boxes):
                if x not in keys_list:
                    keys.append(x)
    if len(keys_list) != len(boxes):
        return False
    return True
