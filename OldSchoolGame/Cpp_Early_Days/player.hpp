#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

class Player
{
public:
    // Constructor Definition
    Player(string name);
    void attack(Player &enemy);
    void defend(Player &enemy);
    void gainEXP(int experience);
    void levelUP();
    void healUP(int health);
    void takeDamage(int damage);
    void death();
    void giveBrief();
private:
    std::string variable;
    std::string name;
    int baseDMG;
    int armor;
    int tempArmor;
    int level;
    int hp;
    int hpMAX;
    int experience;
    int expNeeded;
};

