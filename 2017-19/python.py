f = open('Inputs/2017-19.txt')
inpu = []
for line in iter(f):
    inpu += [line[1:].strip("\n")]
f.close() #--- This will just get the input ---

def get_next(surrounds, old): #Gets next direction
    if surrounds[0] != old and surrounds[0] != " ":
        return[0, 1]
    elif surrounds[1] != old and surrounds[1] != " ":
        return[0, -1]
    elif surrounds[2] != old and surrounds[2] != " ":
        return[1, 0]
    elif surrounds[3] != old and surrounds[3] != " ":
        return[-1, 0]

def get_surrounds(p, inp): #Probably is a better way of doing this... but it worked.
    out = []
    try: out += [inp[p[1]+1][p[0]]]
    except: out += [" "]
    try: out += [inp[p[1]-1][p[0]]]
    except: out += [" "]
    try: out += [inp[p[1]][p[0]+1]]
    except: out += [" "]
    try: out += [inp[p[1]][p[0]-1]]
    except: out += [" "]
    return out

def move(p, d): #Get new position of person
    p[0] += d[0]
    p[1] += d[1]
    return p


def part1(inp): #Run this for part 1
    p = [0, 0] #Position
    dire = [0, 1] #Direction
    old = "" #What the old way was
    l = [] #The output
    i = 0 #The iteration --- Doesn't matter for part 1
    while len(l) < 9: #Loops until the string is full
        #Set old one
        if dire[0] == 0: old = "|"
        else: old = "-"
        
        #Manage position
        if inp[p[1]][p[0]] == "|" or inp[p[1]][p[0]] == "-": #Continues if just normal road
            p = move(p, dire)
        elif inp[p[1]][p[0]] == "+": #Turns if corner
            surrounds = get_surrounds(p, inp)
            dire = get_next(surrounds, old)
            p = move(p, dire)
            if dire[0] == 0: old = "|"
            else: old = "-"
        else: #Get other symbols like letters
            l += inp[p[1]][p[0]]
            p = move(p, dire)
    return "".join(l) #Returns the full string

def part2(inp): #Run this for part 2
    p = [0, 0] #Position
    dire = [0, 1] #Direction
    old = "" #What the old way was
    l = [] #The output
    i = 0 #The iteration
    while len(l) < 9: #Loops until the string is full
        i += 1 #Increase iteration
        
        #Set old one
        if dire[0] == 0: old = "|"
        else: old = "-"
        
        #Manage position
        if inp[p[1]][p[0]] == "|" or inp[p[1]][p[0]] == "-": #Continues if normal road
            p = move(p, dire)
        elif inp[p[1]][p[0]] == "+": #Turns if corner
            surrounds = get_surrounds(p, inp)
            dire = get_next(surrounds, old)
            p = move(p, dire)
        else: #Get other symbols like letters
            l += inp[p[1]][p[0]]
            p = move(p, dire)
    return i #Returns iteration

#Runs the programs
print("Part 1:", part1(inpu))
print("Part 2:", part2(inpu))
