#!/usr/bin/python3
import time


def canUnlockAll(boxes):
    # canUnlockAll() - checks if all lockboxes can be unlocked
    # Args:
    #   boxes - a list of lists with boxes and the keys inside them
    # Returns: boolean
    length = max(boxes)

    if len(length) > 1:
        length = max(length)
    else:
        length = length[0]

    list_ = [iter for iter in range(int(length+1))]
    list_.pop(0)  # Box 0 is already open

    av_keys = []
    av_keys.append(0)
    pend_keys = []

    for i in range(len(boxes)):
        # print("Checking for box {} key...".format(i))
        # time.sleep(2)
        if (i in av_keys):
            # print("Key found! Opening box {}...".format(i))
            # time.sleep(2)

            for j in range(len(boxes[i])):
                av_keys.append(boxes[i][j])

            for i in range(len(pend_keys)):
                if pend_keys[i] in av_keys:
                    # Go back to open box
                    for j in range(len(boxes[pend_keys[i]])):
                        av_keys.append(boxes[pend_keys[i]][j])
                    pend_keys.pop(i)
        else:
            # Add to pending keys
            # print("Key for box {} not found. Added to pending".format(i))
            pend_keys.append(i)

        # print("Available keys: {}".format(av_keys))
        # print("Pending keys: {}\n".format(pend_keys))

    for i in range(len(list_)):
        if list_[i] not in av_keys:
            return False
    return True
