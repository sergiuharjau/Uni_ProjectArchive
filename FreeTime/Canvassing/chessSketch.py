
types of pieces:
    1king - moves 1 around 
    6pawn - moves 1 in front, 2 at first 
    3rook - horizontal , vertical 
    5bishop - diagonals 
    4knights - l shapes 
    2queen - everywhere 

on start of game:
    draw 8 x 8 board 
    draw pieces in their right place
    give white start 
    
on click of piece: 
    colour blue positions where the piece can move:
        if blue position contains enemy piece, make it red 
    on click of blue position:
        if blue position contains enemy piece:
            kill it 
        move own piece there 
        advance turn 

how to determine which piece was clicked:
    squares can be habited by pieces 
    check mouse pos against all squares 