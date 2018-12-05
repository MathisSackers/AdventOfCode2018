import time


def removecollisions(d):
    r = '{}'.format(d)
    for x in range(ord('A'), ord('Z') + 1):
        r = r.replace(chr(x)+chr(x+32), '')
        r = r.replace(chr(x+32)+chr(x), '')
    return r, len(r) == len(d)


def removeunit(d, o):
    return d.replace(chr(o), '').replace(chr(o+32), '')

# part 1
start = time.time()
with open('./input.txt', 'r') as f:
    data = f.read().rstrip()
    data1, done = removecollisions(data)
    while not done:
        data1, done = removecollisions(data1)
    print('Part 1:', len(data1))
    end = time.time()
    print(end - start)
    # part 2
    start = time.time()
    shortest = len(data)
    for x in range(ord('A'), ord('Z') + 1):
        data2 = removeunit(data, x)
        data2, done = removecollisions(data2)
        while not done:
            data2, done = removecollisions(data2)
        shortest = min(len(data2), shortest)
    print('Part 2:', shortest)
    end = time.time()
    print(end - start)
