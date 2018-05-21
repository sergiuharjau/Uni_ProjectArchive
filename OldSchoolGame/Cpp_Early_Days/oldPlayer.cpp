#include <iostream>
#include <stdlib.h> 
#include <string>
using namespace std ;

class Player
{
  public:
    // Constructor Definition
    Player(string name="Placeholder") 
    {        
        this -> variable = "meh" ; 
        cout << "Constructor called " << (size_t)this << endl ; //to ensure we do create the objects 
    
        if (name == "Placeholder")
        {
            cout << "You have no name."; cout << endl ; 
        }
        else cout <<"Your name is "<< name << endl ; 
        
        this-> name = name ; 
        this-> baseDMG = 15 ;
        this-> armor = 10 ;
        this-> tempArmor = 0 ;
        this-> level = 1 ;
        this-> hp = 100 ;  
        this-> hpMAX = 100 ; 
        this-> experience = 0 ;
        this-> expNeeded = 100 ;
        
        
    }
    
    void attack(Player &enemy)
    {
        cout << (size_t)this << " attacks " << (size_t)&enemy << endl;
        
        int rng = rand() % 3 ; // 0, 1, 2
        int crit = rand() % 5 ; // 0, 1, 2, 3, 4 
        if (crit == 0)
        {
            cout << "Critical strike!" << endl; 
            enemy.takeDamage(this-> baseDMG * 2);
        }
        else if (rng == 1 or rng ==2)
        {
            cout << "Normal damage!" << endl; 
            enemy.takeDamage(this->baseDMG);
        }
        else
        {
            cout << "Missed!" << endl;
        }
    }
    
    void defend(Player &enemy)
    {
        int rng = rand() % 3  ;// 0, 1, 2 
        if (rng == 0)
        {
            cout << "Super Defend!" << endl ; 
            this-> tempArmor = 20 ;
        }
        else
        {
            cout << "Normal armor." << endl ; 
            this-> tempArmor = 10 ;
        }         
    }
    
    void gainEXP(int experience)
    {
        this-> experience += experience ; 
        if (this-> experience >= this-> expNeeded)
        {
            this-> levelUP() ; 
        }
    }
    
    void levelUP() 
    {
        this-> experience -= this-> expNeeded ; 
        this-> expNeeded = 100 + 10 * 2 * (this-> level) ;
        this-> level += 1 ;     
        this-> armor += 5 ; 
        this-> baseDMG += 10 ; 
        this-> hpMAX += 25 ; 
        this-> hp = this-> hpMAX ; 
    }
    
    void healUP(int health)
    {
        this-> hp += health ; 
        if (this-> hp > this-> hpMAX)
        {
            this-> hp = this-> hpMAX ; 
        }
    }    
    
    void takeDamage(int damage)
    {
        this-> hp -= damage * ((100 - (this->armor + this-> tempArmor)*2)/100.f); // NOTE: 50 armor would give 100% reduction
        this-> tempArmor = 0 ;    
        
        if (this-> hp <= 0)
        {
            this-> death() ; 
        }
    }
    
    void death()
    {
        cout << "You have died. Game over." << endl ; 
        //
        //
        //
    }
    
    void giveBrief()
    {
        cout << "Name: " << this-> name << endl; 
        cout << "HP: " << this-> hp << endl; 
    }
    
    void increaseDamage(damage)
    {
        this-> baseDMG += damage ; 
    }
    
    void increaseArmor(armor) 
    {
        this-> armor += armor ; 
    }
    
    void increaseHP(health)
    {
        this-> hp += health ; 
    }
    
    private: 
    string variable ; 
    string name ; 
    int baseDMG ;
    int armor ; 
    int tempArmor ;
    int level ;
    int hp ;
    int hpMAX ; 
    int experience ; 
    int expNeeded ; 
    
    
};

int main()
{

    Player martin("Martin") ;
  
    Player enemy("Enemy") ; 
  
    while (true)
    {
  
        char test; 
        
        martin.attack(enemy) ; 
        
        martin.giveBrief() ; 
        enemy.giveBrief() ; 
        
        cin >> test ; 
    }

    
    
    return 0 ;
}



