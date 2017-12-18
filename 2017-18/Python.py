def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


inp = "Inputs/2017-18.txt"
lines = get_lines(inp)
def part1(lines):
    o = 0
    dicti = dict()
    dicti = defaultdict(lambda: 0, dicti)
    index = 0
    for i in range(len(lines)):
        lines[i] = lines[i].split(" ")
    sound = "NO"
    while index < len(lines):
        print(dicti)
        whatDo = lines[index][0]
        if whatDo == "set":
            value = lines[index][2]
            toChange = lines[index][1]
            if not is_number(toChange):
                if is_number(value):
                    dicti[toChange] = int(value)
                else:
                    dicti[toChange] = dicti[value]
        elif whatDo == "mul":
            value = lines[index][2]
            toChange = lines[index][1]
            if not is_number(toChange):
                if is_number(value):
                    dicti[toChange] *= int(value)
                else:
                    dicti[toChange] *= dicti[value]
        elif whatDo == "add":
            value = lines[index][2]
            toChange = lines[index][1]
            if not is_number(toChange):
                if is_number(value):
                    dicti[toChange] += int(value)
                else:
                    dicti[toChange] += dicti[value]
        elif whatDo == "mod":
            value = lines[index][2]
            toChange = lines[index][1]
            if not is_number(toChange):
                if is_number(value):
                    dicti[toChange] = dicti[toChange] % int(value)
                else:
                    dicti[toChange] = dicti[toChange] % dicti[value]
        elif whatDo == "rcv":
            checker = lines[index][1]
            if is_number(checker): toCheck = int(checker)
            else: toCheck = dicti[checker]
            if toCheck != 0:
                return sound
        elif whatDo == "snd":
            checker = lines[index][1]
            toCheck = dicti[checker]
            sound = toCheck
            print(toCheck)
        haveJumped = False
        if whatDo == "jgz":
            checker = lines[index][1]
            if is_number(checker): toCheck = int(checker)
            else: toCheck = dicti[checker]
            jumper = lines[index][2]
            if is_number(jumper): toJump = int(jumper)
            else: toJump = dicti[jumper]
            if toCheck > 0:
                index += toJump
                haveJumped = True

        if not haveJumped:
            index += 1
    
part1(lines)

#---------------------------------------------------------------------------------------------------------
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!INFORMATION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#=========================================================================================================
#Some things to say about the code
#=========================================================================================================
#The code above is not very effective, and not built for this challenge.
#It was built for assembunny in last years. I decided that I should probably make a new system
#The one above used an is_number function, which just tried to turn it into a number
#Instead, in version below, it uses a get function, which, in this context, will always return a number
#Also, I changed it so it was compatible with multiple programs
#This programs exits when two variables both equal done
#I chose to split the next part into multiple functions because it would make for much neater code
#This solution is much neater than the previous one which is quite something since it is much
#heavier code
#---------------------------------------------------------------------------------------------------------



inp = "Inputs/2017-18.txt"
lines = get_lines(inp)
for i in range(len(lines)):
    lines[i] = lines[i].split(" ")
    
#Make dictionaries to store values and set p equal to whatever the program number is
values0 = defaultdict(lambda: 0)
values0["p"] = 0
values1 = defaultdict(lambda: 0)
values1["p"] = 1
def get(a, dictionary): #This will get the value no matter if number of dict item... WITH A TRY EXCEPT!!!
    try:
        return int(a)
    except:
        return dictionary[a]


#QUEUES ---- Used to store queues
queue0 = []
queue1 = []


good = [False,False] #Will reach True if life is complete, or just if no values in queue
output = 0 #Initialize output
def run(p, i, instructions):
    global output #New thing I learned, you can get global variable like this
    
    #Make some variables based on which program it is
    values = values0 if p == 0 else values1
    rbr = queue0 if p == 0 else queue1
    
    #Return if index out of range of instructions
    if i < 0 or i >= len(instructions):
        good[p] = True
        return
    
    #Make temp variable for line so you don't have a bajillion square-brackets
    line = instructions[i]
    #This is the command managing system. If you want to add a new command, like a subtract, it is a simple as an elif
    if line[0] == "snd": #Send command --- send value to other program
        if p == 0:
            queue1.insert(0,get(line[1],values)) #Haven't used an insert befor in Python, slowly building my Python vocabulary
        else:
            queue0.insert(0,get(line[1],values))
            output += 1
    elif line[0] == "set": #Set command --- set a value
        values[line[1]] = get(line[2],values)
    elif line[0] == "add": #Add command --- add a value to another value
        values[line[1]] += get(line[2],values)
    elif line[0] == "mul": #Multiply command --- multiply a value by another value
        values[line[1]] *= get(line[2],values)
    elif line[0] == "mod": #Modulo command --- assign value remainder of modulo of other
        values[line[1]] = values[line[1]] % get(line[2],values)
    elif line[0] == "rcv": #Receive command --- recieve value from other program and assign to a variable
        if len(rbr) == 0: #Returns if nothing in queue
            good[p] = True
            return i
        else:
            good[p] = False
            values[line[1]] = rbr.pop() #Pop from queue
    elif line[0] == "jgz": #Jump command --- jump to another pos if given value is greater than zero
        if get(line[1],values) > 0:
            return i + get(line[2],values) #Returns current position + jump distance

def part2(instr):
    #These are positions
    p0 = 0
    p1 = 0

    while not (good[0] and good[1]): #Loop until done
        #Get what returns when run
        r = run(0,p0,instr)
        if r is not None:
            p0 = r
        else:
            p0 += 1
        #Get what returns when run
        r = run(1,p1,instr)
        if r is not None:
            p1 = r
        else:
            p1 += 1

    return (output) #Returns output
part2(lines)
