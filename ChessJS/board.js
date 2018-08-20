
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
                fill(51) ; 
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
                fill(51) ; 
                black = 0 ; 
                boxes ++ ; 
            }
            rect(scl*j , scl*i, scl-1, scl-1);
        }
    }
}
// Draws the original board

function drawPieces(){
    for (i = 0 ; i < 8 ; i++){
        for (j = 0 ; j < 8 ; j ++){ 
            fill(0);
            if (currentState2D[j][i] == 0){
                //
            }else{
                text(currentState2D[j][i].toString(), scl*i + 40, scl*j + 50);
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