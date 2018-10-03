#include <iostream>
#include <stdlib.h>
#include <string>
#include "fighter.hpp" 


using namespace std ;

Fighter::Fighter(string name) : Player (name)
{
    setTimer(2) ;
    setChargingAttack(true) ; 
}

void Fighter::powerAttack(Player &enemy)
{
/* In order for this function to work, we need to 
call it 3 times. Otherwise, we charge up without attacking. */    
    if (getTimer() > 0) 
    {

        if (getTimer() == 2) 
        {
            cout << getTimer() << " turns to charge up." << endl ; 
        }
        else
        {
            cout << getTimer() << " turn to charge up" << endl ; 
        }  // else statement deals with singular (turn) vs plurar (turns)
        timerTick() ; 
    }
    else 
    {
        swapChargingAttack() ;
        resetTimer() ; 

        cout << "You smacked him in the head real hard." << endl ; 
        enemy.takeDamage(70) ; // smacks the enemy in the head real hard 
    }
        
}

void Fighter::expAttack(Player &enemy)
{
    int rng = rand() % 30  ;  // random damage, 5-35 
    int damage = rng + 5 ; 
    enemy.takeDamage(damage) ; 
    if (enemy.getHP() <= 0)  // if the hit kills the enemy, we get extra xp 
    {
        gainEXP(25) ; 
        cout << "You just gained some xp!" << endl ; 
    }
}

void Fighter::setTimer(int value)
{
    this-> timer = value ; 
}

void Fighter::timerTick()
{
    this-> timer -= 1 ; 
}

void Fighter::resetTimer()
{
    this-> timer = 2 ; 
}

void Fighter::setChargingAttack(bool value)
{
    this-> chargingAttack = value ; 
}

void Fighter::swapChargingAttack()
{
    this-> chargingAttack = not chargingAttack ; 
}

int Fighter::getTimer()
{
    return this-> timer ; 
}
