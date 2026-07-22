OVER:
    Initially I believed DUP and SWAP were sufficient. While implementing XOR I found I could not preserve both operands. I tried redefining SWAP, proved to myself it still failed, and introduced OVER.
    OVER is a necessity as otherwise you cannot work out two gate's at the same time making the XOR gate impossible to create (A or B) and (A NAND B).
    Without OVER you can construct either (A or B) or (A NAND B) but not both at the same time.
ROT:
    Strictly necessary to build an XOR otherwise we cannot save intermediary results. (I've tried for several hours)
    
    
