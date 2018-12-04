import time


def minutes(line):
    return int(line[line.index(':')+1:line.index(']')])


# part 1
start = time.time()
with open('./input.txt', 'r') as f:
    lines = sorted(f.readlines())
    # find the most sleepy guard
    sleeptimes = {}
    guard_id = 'none'
    last_time = 0
    max_id = 'none'
    max_time = 0
    for line in lines:
        if '#' in line:  # Guard #x begins shift
            guard_id = line[line.index('#')+1:line.index('b')-1]
            if guard_id not in sleeptimes:
                sleeptimes[guard_id] = 0
        elif 'w' in line:  # wakes up
            sleeptimes[guard_id] += minutes(line) - last_time
            if sleeptimes[guard_id] > max_time:
                max_time = sleeptimes[guard_id]
                max_id = guard_id
        else:  # falls asleep
            last_time = minutes(line)
    #  find the minute
    counting = False
    counter = [0 for x in range(60)]
    for line in lines:
        if '#' in line:  # Guard #x begins shift
            if line[line.index('#')+1:line.index('b')-1] == max_id:
                counting = True
            else:
                counting = False
        elif counting:
            if 'w' in line:  # wakes up
                for x in range(last_time, minutes(line)):
                    counter[x] += 1
            else:  # falls asleep
                last_time = minutes(line)
    print('Part 1:', counter.index(max(counter)) * int(max_id))
    end = time.time()
    print(end - start)
    # part 2
    start = time.time()
    sleeptimes = {}
    guard_id = 'none'
    last_time = 0
    max_id = 'none'
    max_minute = 0
    max_amount = 0
    for line in lines:
        if '#' in line:  # Guard #x begins shift
            guard_id = line[line.index('#')+1:line.index('b')-1]
            if guard_id not in sleeptimes:
                sleeptimes[guard_id] = [0 for x in range(60)]
        elif 'w' in line:  # wakes up
            for x in range(last_time, minutes(line)):
                sleeptimes[guard_id][x] += 1
                if sleeptimes[guard_id][x] > max_amount:
                    max_amount = sleeptimes[guard_id][x]
                    max_minute = x
                    max_id = guard_id
        else:  # falls asleep
            last_time = minutes(line)
    print('Part 2:', max_minute * int(max_id))
    end = time.time()
    print(end - start)
