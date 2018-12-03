#!/usr/bin/env python


import sys


def checkRecurrances(box_id, recurrances):
    box_id = sorted(box_id)

    for i in box_id:
        if box_id.count(i) == recurrances:
            return True

    return False


def isClose(box_1, box_2, similarity):
    for index, i in enumerate(box_1):
        if i != box_2[index]:
            similarity -= 1

            if similarity < 0:
                return False

    return True


if __name__ == '__main__':
    fp = open(sys.argv[1])
    
    boxes = fp.read().split('\n')
    
    has_two   = 0
    has_three = 0

    for i in boxes:
        if i == '':
            continue

        if checkRecurrances(i, 2):
            has_two += 1

        if checkRecurrances(i, 3):
            has_three += 1

    print("2:", has_two)
    print("3:", has_three)
    print(has_two * has_three)

    for i in boxes:
        if i == '':
            continue

        for j in boxes:
            if j == '' or i == j:
                continue

            if isClose(i, j, 1):
                print("Similar Boxes:", i, j)
