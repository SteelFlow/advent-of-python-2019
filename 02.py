def intcode(ints):
    pointer = 0

    while len(ints) > pointer:
        operator = ints[pointer]
        if operator == 99: return ints

        param1 = ints[ints[pointer+1]]
        param2 = ints[ints[pointer+2]]
        outPos = ints[pointer+3]

        if operator == 1:
            ints[outPos] = param1 + param2
        elif operator == 2:
            ints[outPos] = param1 * param2
        pointer += 4
    return ints

def resetMemory(noun, verb):
    memory = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0]
    memory[1] = noun
    memory[2] = verb
    return memory

def getResult(memory):
    return memory[0]

def day2a():
    return getResult(intcode(resetMemory(12, 2)))

def day2b():
    for n in range(0,99):
        for v in range(0,99):
            result = getResult(intcode(resetMemory(n, v)))
            if result == 19690720:
                print ("Noun:", n, " Verb:", v)
                return 100 * n + v

print (day2a())
print (day2b())