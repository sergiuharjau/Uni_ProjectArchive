#include "player.hpp"

using namespace std ;


Player::Player(string name="Placeholder") 
{
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

void Player::attack(Player &enemy)
{	
        int rng = rand() % 3 ; // 1 in 3 chance to miss 
        int crit = rand() % 5 ; // 1 in 5 chance to crit 
        if (crit == 0)
        {
            cout << "Critical strike!" << endl; 
            enemy.takeDamage(this-> baseDMG * 2); // double damage on crit 
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
    
void Player::defend()
{

        int rng = rand() % 3  ;// 1 in 3 chance to gain extra armor 
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
    
void Player::gainEXP(int experience)
{
        this-> experience += experience ; 
        if (this-> experience >= this-> expNeeded)
        {
            this-> levelUP() ; 
        }
}
    
void Player::levelUP() 
{
		cout << "You have leveled up!" << endl ; 
        this-> experience -= this-> expNeeded ; // extra xp carries over 
        this-> expNeeded = 100 + 10 * 2 * (this-> level) ;
        this-> level += 1 ;     
        this-> armor += 5 ; 
        this-> baseDMG += 10 ; 
        this-> hpMAX += 25 ; 
        this-> hp = this-> hpMAX ; 
}
    
void Player::healUP(int health)
{
        this-> hp += health ; 
        if (this-> hp > this-> hpMAX)
        {
            this-> hp = this-> hpMAX ; 
        }
}    
    
void Player::takeDamage(int damage)
{
        this-> hp -= damage * ((100 - (this->armor + this-> tempArmor)*2)/100.f); // NOTE: 50 armor would give 100% reduction
        this-> tempArmor = 0 ;    
	
        if (this-> hp <= 0)
        {
            this-> death() ; // if hp < 0, you die 
        }
}

void Player::death()
{
        cout << "Game over." << endl ; 
        //
        //
        // this function would return a value to signal that the game ended
}
    
void Player::giveBrief()
{
        cout << "Name: " << this-> name << endl; 
        cout << "HP: " << this-> hp << endl; 
}

void Player::loadGame(int id)
{
    
    sqlite::sqlite db ("..//GameDb.sql") ; // looks in the parent folder 
    
    auto cur = db.get_statement() ; 
    
    cur-> set_sql ("SELECT * " 
                   "FROM tbl_Char "
                   "WHERE chr_key = ?;") ; 
	
    cur-> prepare(); 
    cur-> bind(1, id); // prevents SQL injection (bad programmer)
    
    cur-> step() ; 
    
    this-> name = cur-> get_text(1) ; 
    this-> experience= cur-> get_int(2)  ;
    this-> level = cur-> get_int(3) ; 
    this-> hp = cur-> get_int(4) ; 
    this-> armor = cur-> get_int(5) ; 
    //this-> gold = get_int(6) ; we have no gold at the moment, but that would be the order 
    this-> baseDMG = cur-> get_int(7);
    this-> tempArmor = cur-> get_int(8) ;
    this-> hpMAX = cur-> get_int(9) ; 
    this-> expNeeded = cur-> get_int (10) ; 
}

tuple <vector <int> , string > Player::saveGame()
{
    
    vector<int> gameStateOutput  ; 
	
    gameStateOutput.emplace_back(0) ; // 0 on purpose because the Database counts from 1 
    gameStateOutput.emplace_back(0) ;  // Should be name, but sending it over as a tuple
    gameStateOutput.emplace_back(this-> experience) ;
    gameStateOutput.emplace_back(this-> level) ;
    gameStateOutput.emplace_back(this-> hp) ;
    gameStateOutput.emplace_back(this-> armor) ;
    gameStateOutput.emplace_back(0) ; // No gold 
    gameStateOutput.emplace_back(this-> baseDMG) ;
    gameStateOutput.emplace_back(this-> tempArmor) ;
    gameStateOutput.emplace_back(this-> hpMAX) ;
    gameStateOutput.emplace_back(this-> expNeeded) ;
    
	tuple <vector <int> , string > t = make_tuple(gameStateOutput, this-> name) ; 
	
    return t ; 
    // returns tuple for compatiblity reasons 
}


unsigned long int Player::encrypt(string name)
{
/* This function was used for base 26 encryption, 
 it's not needed anymore at the moment though'*/  
	
	unsigned long int cryptic = 0 ; // unsigned long int means 13 encoded characters max 
	string alphabet = "abcdefghijklmnopqrstuvwxyz" ; 
	for (char character : name)
	{
		int letterPosition = 0 ;
		for (char letter : alphabet )
		{

			if (tolower(character) == tolower(letter) )
			{
				cryptic *= 26 ; 
				cryptic += letterPosition ; 
			}
			
			letterPosition += 1 ;
		}
	}
	return cryptic ; 
}

string Player::decrypt(unsigned long int cryptic)
{
	string alphabet = "abcdefghijklmnopqrstuvwxyz" ; 
	string rName = "" ; 
	string name = "" ; 
	
	while (cryptic > 0)
	{
		int letterIndex = cryptic % 26 ; 
		
		rName += alphabet[letterIndex] ; 
		
		cryptic = cryptic / 26 ; 
	}
	
	for (int i = rName.size() ; i >= 0 ; i --) 
	{
		name += rName[i] ; 
	}
	
	return name ; 
	
}

int Player::getHP()
{
    return this-> hp ; 
}

int Player::getLevel()
{
    return this-> level ; 
}

string Player::getName()
{
	return this-> name ; 
}

