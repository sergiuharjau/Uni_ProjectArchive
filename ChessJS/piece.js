
function checkBox(boxPos){
    if (currentState2D[boxPos[1]][boxPos[0]] > 0){
        colour = "white"
    }else if (currentState2D[boxPos[1]][boxPos[0]] < 0){
        colour = "black"
    }else{
        colour = ""      
    }
    
    return colour 
}
//Checks the current piece in a box, returns black, white or "" 

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
        
        if (turn == "white"){ // makes sure we can't select opponents pieces
            if (currentState2D[boxPos[1]][boxPos[0]] > 0){
                rect(boxPos[0] * scl , boxPos[1] * scl , scl, scl)  
                giveOption(currentState2D[boxPos[1]][boxPos[0]], boxPos, "white") ;
                oldPosition = boxPos ; 
            }
        }else if (turn == "black"){
            if (currentState2D[boxPos[1]][boxPos[0]] < 0){
                rect(boxPos[0] * scl , boxPos[1] * scl , scl, scl)  
                giveOption(currentState2D[boxPos[1]][boxPos[0]], boxPos, "black") ;   
                oldPosition = boxPos ; 
            }
        }
    }

}
//

function fillBoxesGreen(availableBoxes){
    for (i = 0 ; i < availableBoxes.length ; i ++){
        fill(0,255,0)
        rect(availableBoxes[i][0] * scl , availableBoxes[i][1] * scl, scl, scl)
    }       
}              
//

function fillKillBoxes(killBoxes){
    for (i = 0 ; i < killBoxes.length ; i ++){
        fill(255,0,0,150)
        rect(killBoxes[i][0] * scl , killBoxes[i][1] * scl, scl, scl)
    }   
}
//

function giveOption(piece, boxPos, colour){
    if (piece == 6 || piece == -6){

        if (colour == "white"){           //1up
            if (checkBox([boxPos[0], boxPos[1] -1]) == "white"){
                //
            }                       //1up
            else if (checkBox([boxPos[0], boxPos[1] -1]) == "black"){
                //
            }
            else{                   
                availableBoxes = [ [boxPos[0], boxPos[1]-1] ] ;
                if (boxPos[1] == 6){
                    if (checkBox([boxPos[0] , boxPos[1] - 2]) == ""){
                        append (availableBoxes , [boxPos[0] , boxPos[1] - 2] )
                    }
                }
                fillBoxesGreen(availableBoxes) ;
            }
                                    //adjacent left up
            if (checkBox( [boxPos[0] - 1 , boxPos[1] -1 ] ) == "black"){
                killBoxes = [ [boxPos[0] - 1 , boxPos[1] -1] ] ;
                fillKillBoxes(killBoxes) ;
            }                        //adjacent right up
            if (checkBox( [boxPos[0] + 1 , boxPos[1] -1] ) == "black"){
                killBoxes = [ [boxPos[0] + 1 , boxPos[1] -1] ];
                fillKillBoxes(killBoxes) ;
            }


        }else if (colour = "black"){
            if (checkBox([boxPos[0], boxPos[1] +1]) == "black"){
                //
            }                       //1up
            else if (checkBox([boxPos[0], boxPos[1] +1]) == "white"){
                //
            }
            else{                   
                availableBoxes = [ [boxPos[0], boxPos[1]+1] ] ;
                if (boxPos[1] == 1){
                    if (checkBox([boxPos[0] , boxPos[1] + 2]) == ""){
                        append (availableBoxes , [boxPos[0] , boxPos[1] + 2] )
                    }
                }
                fillBoxesGreen(availableBoxes) ; 
            }
                                    //adjacent left up
            if (checkBox( [boxPos[0] - 1 , boxPos[1] +1 ] ) == "white"){
                killBoxes = [[boxPos[0] - 1 , boxPos[1] +1]] ;
                fillKillBoxes(killBoxes) ;
            }                        //adjacent right up
            if (checkBox( [boxPos[0] + 1 , boxPos[1] +1] ) == "white"){
                killBoxes = [[boxPos[0] + 1 , boxPos[1] +1]] ;
                fillKillBoxes(killBoxes) ;
            }
        }
    } // Pawn 
    
    if (piece == 5 || piece == -5 || piece == 2 || piece == -2){
           
      for ( i = 1 ; i < 7 ; i++){
            // top left diagonal
            if (boxPos[0] - i < 0) { break }
            if (boxPos[1] - i < 0) { break }

            if (checkBox( [boxPos[0] - i , boxPos[1] - i] ) == colour){
                break 
            }
            else if (checkBox( [boxPos[0] - i , boxPos[1] - i] ) == swap(colour)){
                append( killBoxes , [boxPos[0] - i , boxPos[1] - i] ) 
                break
            }
            else{
                append( availableBoxes , [boxPos[0] - i , boxPos[1] - i] )
            }
        }

        for ( i = 1 ; i < 7 ; i++){
            // top right diagonal
            if (boxPos[0] + i > 7) { break }
            if (boxPos[1] - i < 0) { break }

            if (checkBox( [boxPos[0] + i , boxPos[1] - i] ) == colour){
                break 
            }
            else if (checkBox( [boxPos[0] + i , boxPos[1] - i] ) == swap(colour)){
                append( killBoxes , [boxPos[0] + i , boxPos[1] - i] ) 
                break
            }
            else{
                append( availableBoxes , [boxPos[0] + i , boxPos[1] - i] )
            }
        }

        for ( i = 1 ; i < 7 ; i++){
            // bottom right diagonal
            if (boxPos[0] + i > 7) { break }
            if (boxPos[1] + i > 7) { break }

            if (checkBox( [boxPos[0] + i , boxPos[1] + i] ) == colour){
                break 
            }
            else if (checkBox( [boxPos[0] + i , boxPos[1] + i] ) == swap(colour)){
                append( killBoxes , [boxPos[0] + i , boxPos[1] + i] ) 
                break
            }
            else{
                append( availableBoxes , [boxPos[0] + i , boxPos[1] + i] )
            }
        }

        for ( i = 1 ; i < 7 ; i++){
            // bottom left diagonal
            if (boxPos[0] - i < 0) { break }
            if (boxPos[1] + i > 7) { break }

            if (checkBox( [boxPos[0] - i , boxPos[1] + i] ) == colour){
                break 
            }
            else if (checkBox( [boxPos[0] - i , boxPos[1] + i] ) == swap(colour)){
                append( killBoxes , [boxPos[0] - i , boxPos[1] + i] ) 
                break
            }
            else{
                append( availableBoxes , [boxPos[0] - i , boxPos[1] + i] )
            }
        }                                   
        fillBoxesGreen(availableBoxes)
        fillKillBoxes(killBoxes)
            
    } // Bishop & Queen
    
    if (piece == 3 || piece == -3 || piece == 2 || piece == -2){
        for ( i = 1 ; i < 7 ; i++){
            // left 
            if (boxPos[0] - i < 0) { break }

            if (checkBox( [boxPos[0] - i , boxPos[1] ] ) == colour){
                break 
            }
            else if (checkBox( [boxPos[0] - i , boxPos[1] ] ) == swap(colour)){
                append( killBoxes , [boxPos[0] - i , boxPos[1] ] ) 
                break

            }
            else{
                append( availableBoxes , [boxPos[0] - i , boxPos[1] ] )
            }
        }
        
        for ( i = 1 ; i < 7 ; i++){
            // right
            if (boxPos[0] + i > 7) { break }

            if (checkBox( [boxPos[0] + i , boxPos[1] ] ) == colour){
                break 
            }
            else if (checkBox( [boxPos[0] + i , boxPos[1] ] ) == swap(colour)){
                append( killBoxes , [boxPos[0] + i , boxPos[1] ] ) 
                break
            }
            else{
                append( availableBoxes , [boxPos[0] + i , boxPos[1] ] )
            }
        }
        
        for ( i = 1 ; i < 7 ; i++){
            // down
            if (boxPos[1] + i > 7) { break }

            if (checkBox( [boxPos[0] , boxPos[1] + i] ) == colour){
                break 
            }
            else if (checkBox( [boxPos[0] , boxPos[1] + i] ) == swap(colour)){
                append( killBoxes , [boxPos[0] , boxPos[1] + i] ) 
                break
            }
            else{
                append( availableBoxes , [boxPos[0] , boxPos[1] + i] )
            }
        }

        for ( i = 1 ; i < 7 ; i++){
            // up 
            if (boxPos[1] - i < 0) { break }

            if (checkBox( [boxPos[0] , boxPos[1] - i] ) == colour){
                break 
            }
            else if (checkBox( [boxPos[0] , boxPos[1] - i] ) == swap(colour)){
                append( killBoxes , [boxPos[0] , boxPos[1] - i] ) 
                break
            }
            else{
                append( availableBoxes , [boxPos[0] , boxPos[1] - i] )
            }
        }              
        
        fillBoxesGreen(availableBoxes)
        fillKillBoxes(killBoxes)
    }  // Rook & Queen
    
    if (piece == 1 || piece == -1){
        for ( i = -1 ; i < 2 ; i++){
            for (j = -1; j < 2 ; j++) {
                if (j == 0 && i == 0) {continue}
                
                if (boxPos[0] + i < 0 || boxPos[0] + i > 7) {continue}
                
                if (boxPos[1] + j < 0 || boxPos[1] + j > 7) {continue}
                
                if (checkBox( [boxPos[0] + i , boxPos[1] + j ] ) == colour){
                    continue 
                }
                else if (checkBox( [boxPos[0] + i , boxPos[1] + j] ) == swap(colour)){
                    append( killBoxes , [boxPos[0] + i , boxPos[1] +j] ) 
                    continue
                }
                else{
                    append( availableBoxes , [boxPos[0] + i , boxPos[1] +j ] )
                }
            }
        }
        fillBoxesGreen(availableBoxes)
        fillKillBoxes(killBoxes)
    } // King
    
    if (piece == 4 || piece == -4){
        for (i = -2 ; i < 3 ; i++){
            for (j = - 2 ; j < 3 ; j++){
                if (i == 0 || j == 0) {continue}
                if (i == j) {continue}
                if (i == -j) {continue}

                if (boxPos[0] + i < 0 || boxPos[0] + i > 7) {continue}
                
                if (boxPos[1] + j < 0 || boxPos[1] + j > 7) {continue}
                console.log(boxPos[0] + i, boxPos[1] + j)
                if (checkBox( [boxPos[0] + i , boxPos[1] + j ] ) == colour){
                    continue 
                }
                else if (checkBox( [boxPos[0] + i , boxPos[1] + j] ) == swap(colour)){
                    append( killBoxes , [boxPos[0] + i , boxPos[1] +j] ) 
                    continue
                }
                else{
                    append( availableBoxes , [boxPos[0] + i , boxPos[1] +j ] )
                }
            }
        }
       fillBoxesGreen(availableBoxes)
       fillKillBoxes(killBoxes) 
    } // Knight
}  
//