#ifndef PLAYER_HPP
#define PLAYER_HPP 

#include <iostream>
#include <cstdlib>
#include <string>
#include <vector> 
#include "libsqlite.hpp" 
#include <tuple> 

using namespace std;

class Player
{
public:
// Constructor Definition
    Player(string name);
    void attack(Player &enemy);
    void defend(); // Gains TempArmor, shields one attack 
    void gainEXP(int experience); 
    void levelUP();
    void healUP(int health);
    void takeDamage(int damage);
    virtual void death(); //solves double dispatch 
    void giveBrief(); // used for testing 
    
//Setter
    void loadGame(int ID) ; // Loads from ID, sets every variable   
    
//Getter
    tuple <vector <int> , string > saveGame() ; // gets a vector of every variable for James 
    
    int getHP() ; 
    int getLevel();

	string getName() ; 
	
//Data Handling  
	unsigned long int encrypt(string name) ; // unused at the moment, kept for old time's sake 
	string decrypt(unsigned long int) ; // ditto 
    
protected:
    string name;
    int baseDMG;
    int armor;
    int tempArmor;
    int level;
    int hp;
    int hpMAX;
    int experience;
    int expNeeded;
};



#endif 