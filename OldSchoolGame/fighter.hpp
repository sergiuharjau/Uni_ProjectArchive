#ifndef FIGHTER_HPP
#define FIGHTER_HPP

#include <iostream>
#include <cstdlib>
#include <string>
#include "player.hpp" 

using namespace std;

class Fighter : public Player 
{
public:
// Constructor Definition
    Fighter(string name) ; // Instantiated with better stats than Player() 
    
//Class specific Functions
    void powerAttack(Player &enemy) ; // Wait 2 turns, hit real hard 
    void expAttack(Player &enemy) ; // If you kill the enemy, gain exp 
    
//Setters    
    void setTimer(int value) ; 
    void setChargingAttack(bool value) ;
          // used in powerAttack  
    void timerTick() ; // timer -= 1 
    void resetTimer() ; // timer = 2 
         
    void swapChargingAttack() ; // negates current Bool 
    
//Getters    
    int getTimer() ; 
    
private: 
    int timer ; // used in powerAttack 
    bool chargingAttack ; // used in powerAttack


};

#endif 
