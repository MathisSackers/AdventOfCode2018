import time


# part 1
with open('./input.txt', 'r') as f:
    start = time.time()
    lines = f.readlines()
    prerequisites = {}
    for line in lines:
        if line[5] not in prerequisites:
            prerequisites[line[5]] = []
        if line[36] not in prerequisites:
            prerequisites[line[36]] = [line[5]]
        else:
            prerequisites[line[36]].append(line[5])
    answer = ''
    for i in range(len(prerequisites)):
        # collect possibles
        possibles = []
        for step, pres in prerequisites.items():
            if len(pres) == 0:
                possibles.append(step)
        choice = sorted(possibles)[0]
        answer += choice
        # remove prerequisite
        prerequisites.pop(choice, None)
        for step, pres in prerequisites.items():
            if choice in pres:
                pres.remove(choice)
    print('Part 1:', answer)
    end = time.time()
    print(end - start)
    # part 2
    start = time.time()
    # TODO
    print('Part 2:')
    end = time.time()
    print(end - start)
