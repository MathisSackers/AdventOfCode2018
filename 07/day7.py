import time


def collectPossibles(prerequisites):
    possibles = []
    for step, pres in prerequisites.items():
        if len(pres) == 0:
            possibles.append(step)
    return possibles


def removePrerequisite(prerequisites, choice):
    prerequisites.pop(choice, None)
    for step, pres in prerequisites.items():
        if choice in pres:
            pres.remove(choice)
    return prerequisites

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
        choice = sorted(collectPossibles(prerequisites))[0]
        answer += choice
        prerequisites = removePrerequisite(prerequisites, choice)
    print('Part 1:', answer)
    end = time.time()
    print(end - start)
    # part 2
    start = time.time()
    # reset prerequisites
    prerequisites = {}
    for line in lines:
        if line[5] not in prerequisites:
            prerequisites[line[5]] = []
        if line[36] not in prerequisites:
            prerequisites[line[36]] = [line[5]]
        else:
            prerequisites[line[36]].append(line[5])
    # work
    idleWorkers = 5
    schedule = {}
    for timestep in range(90*26):  # ~maxtime
        # finish tasks
        if timestep in schedule:
            for finishedTask in schedule[timestep]:
                prerequisites = removePrerequisite(prerequisites, finishedTask)
                idleWorkers += 1
            schedule.pop(timestep, None)
        # begin new tasks
        while idleWorkers > 0 and 0 < len(collectPossibles(prerequisites)):
            idleWorkers -= 1
            workOn = sorted(collectPossibles(prerequisites))[0]
            prerequisites.pop(workOn, None)
            if timestep + ord(workOn) - 4 not in schedule:
                schedule[timestep + ord(workOn) - 4] = [workOn]
            else:
                schedule[timestep + ord(workOn) - 4].append(workOn)
        # check if we're done
        if len(schedule) == 0:
            break
    print('Part 2:', timestep)
    end = time.time()
    print(end - start)
