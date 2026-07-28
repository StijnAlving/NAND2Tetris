chips = {}
chips["NAND"] = {"inputs": {1: "a", 2: "b"}, "outputs": {1: "o"}}
chips["AND"] = {"parts": {"nand1": "NAND", "not1": "NOT"}}
for p in chips["AND"]["parts"]:
    print(p)
    print(chips["AND"]["parts"][p])
    
for i in chips["NAND"]["inputs"]:
    print(i)
