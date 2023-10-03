def canUnlockAll(boxes):
    opened = [False] * len(boxes)
    opened[0] = True
    counter = [0]

    while counter:
        current_box = counter.pop(0)

        for key in boxes[current_box]:
            if key >= 0 and key < len(boxes) and not opened[key]:
                opened[key] = True
                counter.append(key)

    return all(opened)
