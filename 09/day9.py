import time
from collections import deque


def addMarble(circle, current, value):
    current = (current + 2) % len(circle)
    circle.insert(current, value)
    return circle, current


def getPoints(circle, current, value):
    current = (current - 7) % len(circle)
    points = value + circle[current]
    del circle[current]
    return circle, current, points

# part 1
with open('./input.txt', 'r') as f:
    start = time.time()
    players = f.read().rstrip().split(' ')
    marbles = int(players[6])
    players = int(players[0])
    points = {}
    highscore = 0
    circle = [0]
    current = 0
    for val in range(1, marbles):
        if val % 23 == 0:
            circle, current, p = getPoints(circle, current, val)
            if val % players in points:
                points[val % players] += p
            else:
                points[val % players] = p
            highscore = max(highscore, points[val % players])
        else:
            circle, current = addMarble(circle, current, val)
    print('Part 1:', highscore)
    end = time.time()
    print(end - start)
    # part 2. The idea to use deque came from reddit
    start = time.time()
    marbles *= 100
    points = {}
    highscore = 0
    circle = deque([0])
    for val in range(1, marbles):
        if val % 23 == 0:
            circle.rotate(7)
            p = circle.pop() + val
            circle.rotate(-1)
            if val % players in points:
                points[val % players] += p
            else:
                points[val % players] = p
            highscore = max(highscore, points[val % players])
        else:
            circle.rotate(-1)
            circle.append(val)
    print('Part 2:', highscore)
    end = time.time()
    print(end - start)
