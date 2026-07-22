import sys

# read arguments
program_filepath = sys.argv[1]

def python_NAND(a,b):
	return int(not (a == 1 and b == 1))
	
###########################
#     Tokenize Program
###########################

# read file lines
program_lines = []
with open(program_filepath, "r") as program_file:
    program_lines = [
        line.strip() 
            for line in program_file.readlines()]

program = []
token_counter = 0
label_tracker = {}

class Program:
    def __init__(self):
        self.instructions = []
        self.labels = {}
        
for line in program_lines:
    parts  = line.split(" ")
    opcode = parts[0]

    # check for empty line
    if opcode == "":
        continue

    # check if its a label
    if opcode.endswith(":"):
        label_tracker[opcode[:-1]] = token_counter
        continue

    # store opcode token
    program.append(opcode)
    token_counter += 1

    # handle each opcode
    if opcode == "PUSH":
        # expecting a number
        number = int(parts[1])
        program.append(number)
        token_counter += 1
    elif opcode == "PRINT":
        # parse string literal
        string_literal = ' '.join(parts[1:])[1:-1]
        program.append(string_literal)
        token_counter += 1
    elif opcode == "CALL":
        label = parts[1]
        program.append(label)
        token_counter +=1

###########################
#     Interpret Program
###########################

class Stack:

    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp    = -1

    def push(self, number):
        self.sp += 1
        self.buf[self.sp] = number
    
    def pop(self):
        number = self.buf[self.sp]
        self.sp -= 1
        return number
    
    def top(self):
        return self.buf[self.sp]
        


pc = 0
stack = Stack(256)
call_stack = Stack(256)

while program[pc] != "HALT":
    opcode = program[pc]
    pc += 1

    if opcode == "PUSH":
        number = program[pc]
        pc += 1
        stack.push(number)
        
    elif opcode == "POP":
        stack.pop()
    elif opcode == "PRINT":
        string_literal = program[pc]
        pc += 1
        print(string_literal)
    elif opcode == "READ":
        number = int(input())
        stack.push(number)
    elif opcode == "CALL":
        function_name = program[pc]
        pc += 1
        call_stack.push(pc)
        pc = label_tracker[function_name]
    elif opcode == "RETURN":
        pc = call_stack.pop()
    elif opcode == "PRINT_STACK":
        print(stack.buf[:stack.sp+1])
    elif opcode == "NAND":
        b = stack.pop()
        a = stack.pop()
        
        stack.push(python_NAND(a,b))
    else:
        print("Unexpected opcode received")
        exit(1)
