#!/usr/bin/env python


import sys


def calibrate(signals, final=0):
    for i in signals:
        if i == '':
            continue

        final += int(i)

    return final


def findFirstFrequency(signals):
    iterations = []
    final = 0

    while True:
        for i in signals:
            if i == '':
                continue

            final += i

            if final in iterations:
                return final

            iterations.append(final)



if __name__ == '__main__':
    signals = [int(i) for i in open(sys.argv[1]).read().split('\n') if i != '']
    print("FINAL:", calibrate(signals))
    print("First Frequency:", findFirstFrequency(signals))
