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
var killBoxes = []; 
var oldPosition = []; 

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

function mousePressed(){
    // Triggers on left click
    boxPos = currentBox() 
    console.log(boxPos)
    for (i = 0 ; i < availableBoxes.length ; i ++) {
        if (boxPos[0] == availableBoxes[i][0] && boxPos[1] == availableBoxes[i][1]){
            advanceTurn() ;
            movePiece(oldPosition , availableBoxes[i]) ;
            console.log(turn, "plays") ;
        }
    } 
    for (i = 0 ; i < killBoxes.length ; i ++) {
        if (boxPos[0] == killBoxes[i][0] && boxPos[1] == killBoxes[i][1]){
            advanceTurn() ;
            movePiece(oldPosition , killBoxes[i]) ;
            console.log(turn, "plays") ;
        }
    } 
    availableBoxes = [] 
    killBoxes = [] 
    selectPiece(turn) ; 
}

