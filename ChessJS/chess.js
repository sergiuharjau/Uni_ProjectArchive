var scl = 100; 
var boxPos = []; 
var currentState = [] ; 
var currentState2D = [ 
                [],[],[],[],[],[],[],[] 
                            ] ; 
var increment = 0;
var piece;
var turn; 
var availableBoxes = [];

function setup(){
    createCanvas(8 * scl, 8 * scl );
    
    drawBoard() ; 
    setupPieces() ;
    drawPieces() ; 
    
    console.log("White plays")
    turn = "white"
}

function draw(){
    //checkMouse()
}

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

function drawBoard(){
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

function advanceTurn(){
    if (turn == "white"){
        turn = "black"
    } else if (turn == "black"){
        turn = "white"
    }
}

function mousePressed(){
    boxPos = currentBox() 
    for (i = 0 ; i < availableBoxes.length ; i ++) {
        if (boxPos[0] == availableBoxes[i][0] && boxPos[1] == availableBoxes[i][1]){
            advanceTurn() ; 
            console.log(turn, "plays") ;
        }
    } 
    selectPiece(turn) ; 
}

function currentBox(){
    return [floor(mouseX / scl), floor(mouseY/scl)]
}

function selectPiece(turn){
    drawBoard() ; //to override past selects
    drawPieces() ;    
    
    boxPos = currentBox() ;
    if (currentState2D[boxPos[1]][boxPos[0]] != 0){
        //if no piece in square, can't select  
        if ((boxPos[0] + boxPos[1]) % 2 == 0){
            fill(0,0,255,180) ; //handles different coloured squares
        }else{
            fill(0,0,255,80);
        }
        
        if (turn == "white"){
            if (currentState2D[boxPos[1]][boxPos[0]] > 0){
                rect(boxPos[0] * scl , boxPos[1] * scl , scl-1, scl-1)  
                giveOption(currentState2D[boxPos[1]][boxPos[0]], boxPos, "white") ;
            }
        }else if (turn == "black"){
            if (currentState2D[boxPos[1]][boxPos[0]] < 0){
                rect(boxPos[0] * scl , boxPos[1] * scl , scl-1, scl-1)  
                giveOption(currentState2D[boxPos[1]][boxPos[0]], boxPos, "black") ;   
            }
        }
    }

}

function giveOption(piece, boxPos, colour){
    if (piece == 6 || piece == -6){
        if (colour == "white"){
            fill(0,255,0)
            rect(boxPos[0] * scl, (boxPos[1]-1) * scl, scl -1, scl -1)
            rect(boxPos[0] * scl, (boxPos[1]-2) * scl, scl -1, scl -1)
            availableBoxes = [ [boxPos[0], boxPos[1]-1] , [boxPos[0], boxPos[1]-2] ]
            console.log(availableBoxes)
        }else{
            fill(0,255,0)
            rect(boxPos[0] * scl, (boxPos[1]+1) * scl, scl -1, scl -1)
            rect(boxPos[0] * scl, (boxPos[1]+2) * scl, scl -1, scl -1)
            availableBoxes = [ [boxPos[0], boxPos[1]+1 ] , [boxPos[0], boxPos[1]+2] ]
            console.log(availableBoxes)
        }
    }
}