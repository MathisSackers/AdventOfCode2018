import time


def addMetadata(data):
    metaSum = 0
    children = data[0]
    metas = data[1]
    data = data[2:]
    length = 2 + metas
    for child in range(children):
        cMeta, cLength = addMetadata(data)
        metaSum += cMeta
        data = data[cLength:]
        length += cLength
    for meta in range(metas):
        metaSum += data[meta]
    return metaSum, length


def nodeValue(data):
    odata = data[:]
    value = 0
    numChildren = data[0]
    metas = data[1]
    data = data[2:]
    length = 2 + metas
    children = []
    for child in range(numChildren):
        cVal, cLength = nodeValue(data)
        children.append(cVal)
        data = data[cLength:]
        length += cLength
    for meta in range(metas):
        if len(children) == 0:
            value += data[meta]
        elif data[meta] - 1 < len(children):
            value += children[data[meta] - 1]
    return value, length

# part 1
with open('./input.txt', 'r') as f:
    start = time.time()
    data = [int(x) for x in f.read().rstrip().split(' ')]
    metaSum, _ = addMetadata(data)
    print('Part 1:', metaSum)
    end = time.time()
    print(end - start)
    # part 2
    start = time.time()
    val, _ = nodeValue(data)
    print('Part 2:', val)
    end = time.time()
    print(end - start)
