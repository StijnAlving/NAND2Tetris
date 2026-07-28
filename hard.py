import sys
program_filepath = sys.argv[1]
# read file lines
program_lines = []
with open(program_filepath, "r") as program_file:
    program_lines = [
        line.strip() #removes tabs and spaces on the outsides of lines
            for line in program_file.readlines()]
            
state = "outside"
chips = {}
chips["NAND"] = {"inputs": {1: "a", 2: "b"}, "outputs": {1: "o"}}
for line in program_lines:

    # check for empty line or comments
    if line == "" or line[0] == "#":
        continue
    # check if function ends
    if line == "END":
        if state == "outside":
            print("END encountered outside function, ignoring command")
            continue
        else:
            chips[function_name] = {"inputs": inputs, "outputs": outputs, "parts": parts, "wiring": wiring}
            state = "outside"
            continue
    # check if its a function
    if line.endswith(":") and state == "outside":
        function_name = line[:-1]
        inputs = {}
        outputs = {}
        parts = {}
        wiring = {}
        state = "inside"
        continue
    elif line.endswith(":"):
        state = line[:-1]
        continue
    
    if state == "PINS":
        line_parts = line.split(" ")
        if len(line_parts) != 2:
            print("Unexpected PINS syntax")
            print(line)
        pin_type = line_parts[0]      # e.g. "IN1", "OUT2"
        pin_name = line_parts[1]      # e.g. "a", "o"
        if pin_type.startswith("IN"):
            number = int(pin_type[2:]) 
            inputs[number] = pin_name
        elif pin_type.startswith("OUT"):
            number = int(pin_type[3:])   
            outputs[number] = pin_name
            
    elif state == "PARTS":
        line_parts = line.split(" ")
        if len(line_parts) != 2:
            print("Unexpected PARTS syntax")
            print(line)
        part_type = line_parts[0]      # e.g. "NAND", "NOT"
        part_name = line_parts[1]      # e.g. "nand1", "not1"
        parts[part_name] = part_type
        
    elif state == "WIRING":
        line_parts = line.split("=")
        for i in range(len(line_parts)):
            line_parts[i] = line_parts[i].strip() #remove any outside spaces or tabs
            if line_parts[i] not in wiring:
                wiring[line_parts[i]] = []
        for i in range(len(line_parts) - 1):
            wiring[line_parts[i]].append(line_parts[i+1])
            wiring[line_parts[i+1]].append(line_parts[i])
            

def evaluate(name, *args):
    values = {}
    evaluated_parts = {}
    len_args = len(args)
    if name == "NAND":
        if len_args == 2:
            return [int(not (args[0] == 1 and args[1] == 1))]
        else:
            print("Gave " + str(len_args) + " inputs where 2 are expected for NAND")
            return e
    else:
        if len_args == len(chips[name]["inputs"]):
            for i in chips[name]["inputs"]:
                cur_input = chips[name]["inputs"][i]
                values[cur_input] = args[i-1]
                for w in chips[name]["wiring"][cur_input]:
                    values[w] = args[i-1]
            not_done = True
            while not_done:
                not_done = False
                for i in list(values):
                    for w in chips[name]["wiring"][i]:
                        if w not in values:
                            values[w] = values[i]
                            not_done = True
                for p in chips[name]["parts"]: #for each part check if all inputs have a value
                    if p not in evaluated_parts: 
                        missing_input = False
                        part_type = chips[name]["parts"][p]
                        for i in chips[part_type]["inputs"]:
                            if p + ".IN" + str(i) not in values:
                                missing_input = True
                        if not missing_input:
                            not_done = True
                            input_list = []
                            for i in chips[part_type]["inputs"]:
                                input_list.append(values[p + ".IN" + str(i)])
                            output_values = evaluate(part_type,  *input_list)
                            for idx, i in enumerate (chips[part_type]["outputs"]):
                                values[p + ".OUT" + str(i)] = output_values[idx]
                            evaluated_parts[p] = True
            output_list = []
            for out in chips[name]["outputs"]:
                output_list.append(values[chips[name]["outputs"][out]])
            return output_list
        else:
            print("Gave "+str(len_args) + " inputs where "+ str(len(chips[name]["inputs"])) + " are expected for " + name)
            return e
def basic_gates_test():
    if (evaluate("NOT", 0) != [1] or
        evaluate("NOT", 1) != [0] or
        evaluate("AND", 0, 0) != [0] or
        evaluate("AND", 0, 1) != [0] or
        evaluate("AND", 1, 0) != [0] or
        evaluate("AND", 1, 1) != [1]):
            print ("Error in basic gates AND or NOT is wrong")
    else:
            print ("NOT and AND gates are good")
            
    if (evaluate("OR", 0, 0) != [0] or
        evaluate("OR", 1, 0) != [1] or
        evaluate("OR", 0, 1) != [1] or
        evaluate("OR", 1, 1) != [1]):
            print("Error in basic gate OR is wrong")
    else:
            print("OR gate is good")
    
basic_gates_test()
