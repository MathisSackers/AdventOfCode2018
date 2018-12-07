import time
import numpy as np


# part 1
with open('./input.txt', 'r') as f:
    start = time.time()
    lines = f.readlines()
    points = [[int(line[:line.index(',')]), int(line[line.index(' ') + 1:])] for line in lines]
    grid = np.zeros(shape=(500, 500))  # pretty arbitrary
    infinites = []
    for x in range(500):
        for y in range(500):
            pid = -1
            pdist = 500*500
            for point in points:
                dist = abs(point[0] - x) + abs(point[1] - y)
                if dist < pdist:
                    pid = points.index(point)
                    pdist = dist
                elif dist == pdist:  # equal distance
                    pid = -1
            grid[y][x] = pid
            if min(x, y) == 0 or max(x, y) == 499:  # naive
                if pid not in infinites:
                    infinites.append(pid)
    unique, counts = np.unique(grid, return_counts=True)
    unique, counts = [int(x) for x in list(unique)], [int(x) for x in list(counts)]
    # discount invalids
    for infinite in infinites:
        counts[unique.index(infinite)] = -1
    counts[unique.index(-1)] = -1
    print('Part 1:', max(counts))
    end = time.time()
    print(end - start)
    # part 2
    start = time.time()
    regionSize = 0
    for x in range(500):
        for y in range(500):
            dist = 0
            for point in points:
                dist += abs(point[0] - x) + abs(point[1] - y)
            if dist < 10000:
                regionSize += 1
    print('Part 2:', regionSize)
    end = time.time()
    print(end - start)
