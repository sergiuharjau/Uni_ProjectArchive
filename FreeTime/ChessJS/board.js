
function setupPieces(){
    currentState = [-3, -4, -5, -2, -1, -5, -4, -3, -6, -6, -6, -6, -6, -6, -6, -6] ; 
    
    for(i = 0 ; i < 32 ; i ++){
        append(currentState, 0)
    }
    finalStates = [6, 6, 6, 6, 6, 6, 6, 6, 3, 4, 5, 2, 1, 5, 4, 3] ; 
    for(i = 0; i < 16 ; i ++) {
        append(currentState, finalStates[i]) ;
    }
    
    increment = 0 
    for (i = 0 ; i < 8 ; i++){
        for (j = 0 ; j < 8 ; j++){
            currentState2D[i][j] = currentState[increment] 
            increment ++ ; 
        }
    }
    console.log(currentState2D)
} 
// Populates array with starting position

function drawBoard(){
    // Draws the original board
    black = 0; 
    boxes = 0;
    for (i = 0 ; i < 8 ; i++){
        for (j = 0 ; j < 8 ; j ++){
            //console.log(black)
            if (black == 1 && boxes < 8){
                fill(125) ; 
                black = 0 ;
                boxes ++ ; 
            }else if (black == 0 && boxes < 8){
                fill(255) ;
                black = 1 ;
                boxes ++ ; 
            }else if (black == 1 && boxes ==8){
                boxes = 0 ;
                fill(255) ; 
                black = 1 ;
                boxes ++ ; 
            }else{
                boxes = 0 ; 
                fill(125) ; 
                black = 0 ; 
                boxes ++ ; 
            }
            rect(scl*j, scl*i, scl, scl);
        }
    }
}
// Draws the original board

function loadPiecesPng(){
    wPawn = loadImage("/Project-Archive/FreeTime/Assets/PiecesPng/Chess_plt60.png")
    wBishop = loadImage("/Project-Archive/FreeTime/Assets/PiecesPng/Chess_blt60.png")
    wRook = loadImage("/Project-Archive/FreeTime/Assets/PiecesPng/Chess_rlt60.png")
    wKnight = loadImage("/Project-Archive/FreeTime/Assets/PiecesPng/Chess_nlt60.png")
    wQueen = loadImage("/Project-Archive/FreeTime/Assets/PiecesPng/Chess_qlt60.png")
    wKing = loadImage("/Project-Archive/FreeTime/Assets/PiecesPng/Chess_klt60.png")  
    
    bPawn = loadImage("/Project-Archive/FreeTime/Assets/PiecesPng/Chess_pdt60.png")
    bBishop = loadImage("/Project-Archive/FreeTime/Assets/PiecesPng/Chess_bdt60.png")
    bRook = loadImage("/Project-Archive/FreeTime/Assets/PiecesPng/Chess_rdt60.png")
    bKnight = loadImage("/Project-Archive/FreeTime/Assets/PiecesPng/Chess_ndt60.png")
    bQueen = loadImage("/Project-Archive/FreeTime/Assets/PiecesPng/Chess_qdt60.png")
    bKing = loadImage("/Project-Archive/FreeTime/Assets/PiecesPng/Chess_kdt60.png")
}

function drawPieces(){
    for (i = 0 ; i < 8 ; i++){
        for (j = 0 ; j < 8 ; j ++){ 
            fill(0);
            if (currentState2D[j][i] !=0) {
                if (currentState2D[j][i] == 1){
                    image(wKing , scl * i, scl*j, scl, scl)
                }else if (currentState2D[j][i] == 2){
                    image(wQueen , scl * i, scl*j, scl, scl)
                }else if (currentState2D[j][i] == 3){
                    image(wRook , scl * i, scl*j, scl, scl)
                }else if (currentState2D[j][i] == 4){
                    image(wKnight , scl * i, scl*j, scl, scl)
                }else if (currentState2D[j][i] == 5){
                    image(wBishop , scl * i, scl*j, scl, scl)
                }else if (currentState2D[j][i] == 6){
                    image(wPawn , scl * i, scl*j, scl, scl)
                }else if (currentState2D[j][i] == -1){
                    image(bKing , scl * i, scl*j, scl, scl)
                }else if (currentState2D[j][i] == -2){
                    image(bQueen , scl * i, scl*j, scl, scl)
                }else if (currentState2D[j][i] == -3){
                    image(bRook , scl * i, scl*j, scl, scl)
                }else if (currentState2D[j][i] == -4){
                    image(bKnight , scl * i, scl*j, scl, scl)
                }else if (currentState2D[j][i] == -5){
                    image(bBishop , scl * i, scl*j, scl, scl)
                }else if (currentState2D[j][i] == -6){
                    image(bPawn , scl * i, scl*j, scl, scl) 
                }
            }
        }
    }
}
// Draws current pieces on the board

function advanceTurn(){
    if (turn == "white"){
        turn = "black"
    } else if (turn == "black"){
        turn = "white"
    }
}
// Sets turn variable to opposite value

function currentBox(){
    return [floor(mouseX / scl), floor(mouseY/scl)]
}
// Returns box in X/Y from 0 to 7  

function movePiece(oldPosition, newPosition){
    currentState2D[newPosition[1]][newPosition[0]] = currentState2D[oldPosition[1]][oldPosition[0]] 
    currentState2D[oldPosition[1]][oldPosition[0]] = 0 
    drawPieces() ; 
}
// Give old position in [x,y] array

function swap(colour){
    if (colour == "white"){
        return ("black")
    } else {
        return ("white")
    }
}