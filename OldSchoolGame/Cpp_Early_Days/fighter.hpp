#include <iostream>
#include <cstdlib>
#include <string>
#include "player.hpp" 

using namespace std;

class Fighter : public Player 
{
public:
    // Constructor Definition
    Fighter(string name) ;
    void powerAttack(Player &enemy);
    void expAttack(Player &enemy); 
    void timerTick();
    void resetTimer();
    void swapChargingAttack() ; 
    
    
    private: 
    
    int timer ; 
    
    bool chargingAttack ; 


};

