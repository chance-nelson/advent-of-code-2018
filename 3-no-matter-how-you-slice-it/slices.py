#!/usr/bin/env python


import sys
import re
import pprint


if __name__ == '__main__':
    slices = open(sys.argv[1]).read().split('\n')[:-1]

    fabric = []
    for i in range(1000):
        fabric.append([])
        for j in range(1000):
            fabric[i].append([])

    sids = []

    for i in slices:
        if i == '':
            continue

        i = re.split('([#\ ,:])', i)
        sid  = int(i[2])
        sx   = int(i[6])
        sy   = int(i[8])
        dims = i[-1].split('x')
        dims = [int(x) for x in dims]

        sids.append(sid)

        for y in range(sy, sy+dims[1]):
            for x in range(sx, sx+dims[0]):
                fabric[y][x].append(sid)

    hits = []

    for i in fabric:
        for j in i:
            if len(j) >= 2:
                for k in j:
                    if k not in hits:
                        hits.append(k)

    print(len(list(set(hits))))

    for sid in sids:
        if sid not in hits:
            print(sid)
