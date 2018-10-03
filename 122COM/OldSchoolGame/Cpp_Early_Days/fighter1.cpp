#include <iostream>
#include <stdlib.h>
#include <string>
#include "player.hpp" 

using namespace std; 

class Fighter: public Player
{
    Fighter() : Player(this)
    {
        this-> baseDMG += 10 ; 
        this-> armor += 5 ; 
        this-> hp += 25 ; 
        this-> chargingAttack = True 
        this-> timer = 2 
            // Start with a sword 
    }
};