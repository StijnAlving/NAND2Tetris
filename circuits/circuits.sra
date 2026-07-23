MUX: # a, b, s -> (a∧¬s)∨(b∧s)
	DUP
	CALL NOT
	ROT
	CALL AND
	ROT
	CALL AND
	CALL OR
	RETURN

H_ADDER: # a, b -> (a∧b), (a⊕b)
	OVER
	OVER
	CALL AND
	ROT
	CALL XOR
	RETURN
	
F_ADDER: # a, b, c -> (a∧b)∨(c∧(a⊕b)), a⊕b⊕c
	CALL H_ADDER
	SWAP
	ROT
	CALL H_ADDER
	ROT
	CALL OR
	RETURN

4BIT_ADDER: # A3 B3 A2 B2 A1 B1 A0 B0 -> Carry, (A⊕B)3, (A⊕B)2, (A⊕B)1, (A⊕B)0
	CALL H_ADDER
	ROT
	CALL F_ADDER
	ROT
	CALL F_ADDER
	ROT

