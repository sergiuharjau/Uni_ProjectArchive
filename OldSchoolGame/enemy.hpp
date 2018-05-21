#ifndef ENEMY_HPP
#define ENEMY_HPP

#include <iostream>
#include <cstdlib>
#include <string>
#include "player.hpp" 

using namespace std;

class Enemy : public Player 
{
public:
// Constructor Definition
    Enemy (int level) ; // Starts off with worse stats than Player(), and a randomly generated name 
    
// Class specific Functions
	void attack (Player &other) ; // overrides attack function in Player 
	void taunt (Player &other) ; 
    void improvedAttack(Player &other) ; 
    void death() ; // overrides death(), solved double dispatch 
	
// Data Handling
	string nameGenerator(int seed) ; // seed is unix timestamp, %1000 
};

#endif