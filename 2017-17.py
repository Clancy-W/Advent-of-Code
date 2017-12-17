def part1(l):
    pos = 0
    arr = [0]
    for i in range(1, 2018):
        pos = (pos + l) % len(arr)
        arr = arr[:pos+1] + [i] + arr[pos+1:]
        pos = pos + 1

    return (arr[arr.index(2017) + 1])

def part2(l):
    pos = 0
    arr = [0]
    for i in range(1, 50000000):
        pos = (pos + l) % len(arr)
        if pos == 0:
            arr = [0] + [i] + arr[1:]
        else:
            arr += [0]
        pos = pos + 1
    return (arr[arr.index(0) + 1])

print(part1(324))
print(part2(324))
