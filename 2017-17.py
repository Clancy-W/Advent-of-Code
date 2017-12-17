def part1(inp):
    #Initialization
    pos = 0
    arr = [0]
    
    for i in range(1, 2018): #Loops through to 2017
        pos = (pos + inp) % len(arr)
        arr = arr[:pos+1] + [i] + arr[pos+1:]
        pos += 1

    return (arr[arr.index(2017) + 1]) #Returns answer to part 1

def part2(inp):
    #Initialization
    pos = 0
    arr = [0]
    
    
    for i in range(1, 50000000): #Loops through to 5 billion
        pos = (pos + inp) % len(arr)
        if pos == 0: #Only add i if position at zero
            arr = [0] + [i] + arr[1:]
        else:
            arr += [0]
        pos += 1
    return (arr[1]) #Returns answer to part 2

print("Part 1:", part1(324))
print("Part 2:", part2(324))
