def part1(inp):
	out = 0
	for i in range(len(inp)): 
		if inp[i] == inp[i-1]: #Check if digits are same
			out += int(inp[i]) #Add number to output
	return out #Return answer to part 1

def part2(inp):
	out = 0
	for i in range(len(inp)): 
		if inp[i] == inp[i-int(len(inp)/2)]: #Check if digits are same
			out += int(inp[i]) #Add number to output
	return out #Return answer to part 2

print("Part 1:", part1(121211))
print("Part 2:", part2(121211))
