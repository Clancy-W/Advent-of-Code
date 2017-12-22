lines = [i.strip("\n") for i in get_lines("Inputs/2017-22.txt")] #Get input
arr = np.empty((8000, 8000), dtype=str)
arr[:] = "."
for x in range(len(lines)):
    for y in range(len(lines[x])):
        arr[x+4000-12, y+4000-12] = lines[x][y]
pos = [4000, 4000]
dire = [-1, 0]
count = 0
standing = arr

def direction(current, manage):
    hasharr = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    dotarr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    farr1 = [[0, 1], [0, -1]]
    farr2 = [[1, 0], [-1, 0]]
    if manage == ".": return dotarr[dotarr.index(current) -1]
    elif manage == "#": return hasharr[hasharr.index(current) - 1]
    elif manage == "F":
        if current in farr1: return farr1[farr1.index(current) - 1]
        return farr2[farr2.index(current) - 1]
    return current

def convert(square, count):
    if cur == ".": return ["W", count]
    elif cur == "W":
        count += 1; return ["#", count]
    elif cur == "F": return [".", count]
    elif cur == "#": return ["F", count]

for i in range(10000000):
    cur = arr[pos[0], pos[1]]
    dire = direction(dire, cur)
    arr[pos[0], pos[1]], count = convert(cur, count)
    
    pos[0] += dire[0]
    pos[1] += dire[1]
    standing = arr
    
print("Part 2:", count)
