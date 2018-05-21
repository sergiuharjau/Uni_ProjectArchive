#include <iostream>
#include <stdlib.h>
#include <string>
#include "fighter.hpp" 


using namespace std ;

Fighter::Fighter(string name) : Player (name)
{
    cout << "Created Fighter" << endl ; 
    this-> baseDMG += 10 ;
    this-> armor += 5 ; 
    this-> hp += 25 ; 
    this-> chargingAttack = true ;
    this-> timer = 2 
}

void Fighter::powerAttack(Player &enemy)
{
    cout << "powerAttack called" << endl ;
    
    if (this-> timer > 0) 
    {
        this-> chargingAttack = false ;
        if (this-> timer == 2) 
        {
            cout << this-> timer << " turns to charge up." << endl ; 
        }
        else
        {
            cout << this-> timer << " turn to charge up" << endl ; 
        }  // else statement deals with singular (turn) vs plurar (turns)
        this-> timer -= 1 
    }
    else 
    {
        this-> chargingAttack = true ; 
        this-> timer = 2 ; 
        cout << "You smacked him in the head real hard." << endl ; 
        enemy.takeDamage(70) ; 
    }
    
    
    
}

void Fighter::expAttack(Player &enemy)
{
    cout <<"expAttack called" << endl ; 
}

void Fighter::timerTick()
{
    this-> timer -= 1 ; 
}


void Fighter::resetTimer()
{
    this-> timer = 2 ; 
}

void Fighter::swapChargingAttack()
{
    this-> chargingAttack = 
}
