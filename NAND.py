def NAND(a,b):
	return int(not (a == 1 and b == 1))
	
if __name__ == '__main__':
    for a in (0,1):
        for b in (0,1):
            output = NAND(a,b)
            print(str(a) + "---+--+ \n")
            print("    | N|---" + str (output) + "\n")
            print(str(b) + "---+--+ \n \n \n")
            
