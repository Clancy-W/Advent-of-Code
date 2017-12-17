def part1(inp):
    o = 0
    for i in range(len(inp)):
        ints = [int(x) for x in inp[i]] #Get all numbers in row
        o += max(ints) - min(ints) #Add the max - the min
    return o #Returns the answer to part 1

def part2(inp):
    o = 0
    for i in range(len(inp)):
        ints = [int(x) for x in inp[i]] #Get all numbers in row
        for j in range(len(ints)):
            for k in range(len(ints)): #Loops through numbers in row
                if ints[k] % ints[j] == 0 and ints[k] != ints[j]: #Checks if divisible
                    o += ints[k] / ints[j] #Add the first / second
    return o #Returns the answer to part 2

print("Part 1:", part1([[1, 2, 3], [3, 5, 6])
print("Part 2:", part2([[1, 2, 3], [3, 5, 6])
