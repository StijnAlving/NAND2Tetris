OVER:
    Initially I believed DUP and SWAP were sufficient. While implementing XOR I found I could not preserve both operands. I tried redefining SWAP, proved to myself it still failed, and introduced OVER.
    OVER is a necessity as otherwise you cannot work out two gate's at the same time making the XOR gate impossible to create (A or B) and (A NAND B).
    Without OVER you can construct either (A or B) or (A NAND B) but not both at the same time.
ROT:
    Strictly necessary to build an XOR otherwise we cannot save intermediary results. (I've tried for several hours)
    
Multi-bit values
    Bits are stored least-significant first.
    Binary operators on multi-bit values expect operands to be interleaved.

    Example:
    A = 0111 : A3 A2 A1 A0
    B = 0111 : B3 B2 B1 B0
    Stack (bottom → top):
    A3 B3 A2 B2 A1 B1 A0 B0
