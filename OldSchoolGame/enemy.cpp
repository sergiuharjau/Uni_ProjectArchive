#include <iostream>
#include <stdlib.h>
#include <string>
#include "enemy.hpp" 


using namespace std ;

Enemy::Enemy(int level) : Player ("PlaceholderEnemy")
{
	this-> name = nameGenerator(time(nullptr) % 100) ; // using time as seed, to keep things random 
    this-> baseDMG = baseDMG - 5 ; 
	this-> armor = armor - 2 ; 
	this-> hp = hp - 25 ;
	this-> hpMAX = this-> hp ; 
	
	for (int i = level ; i > 1 ; i--)
	{
		levelUP() ; // So we can construct the object at whatever level we want 
	}
}

string Enemy::nameGenerator(int seed)
{
/* To keep the game fun, I've created a rough name generator
 which usually get the job done. Uses unix timestamp as seed. */ 
	
	string vowels = "aeiou" ;
	string consonants = "bcdfghjklmnpqrstvwxyz" ;
	string name = "" ; 
	int repeatingVowels = 0 ; 
	int repeatingConsonants = 0 ; 
	
	int nameLength = (rand() + seed) % 5 ; // name length of max 11
	
	nameLength += 6 ;    // min 6 
	
	int vowelsInWord = nameLength * (50 / 100.f) ; 
	
	for (int i = nameLength ; i > 0 ; i --)
	{
		int rngVowel = (rand() + seed) % 5 ; 
		
		int rngConsonant = (rand() + seed) % 21 ; 
		
		int rngCoinFlip = (rand() + seed) % 2 ; 
		
		if (rngCoinFlip = 1 and vowelsInWord > 0 and i!=nameLength and repeatingVowels <2)
		{
			vowelsInWord -= 1 ; 
			name += vowels[rngVowel] ; 
			repeatingVowels += 1 ;
			repeatingConsonants = 0 ; 
		}
		else if (repeatingConsonants < 3)
		{
			name += consonants[rngConsonant] ; 
			repeatingVowels = 0 ; 
			repeatingConsonants += 1 ; 
		}
	}
	
	string upperName = "" ; 
	
	int i = 0 ;
	
	for (char c : name)
	{
		
		if ( i == 0 )
		{
			upperName += toupper(c) ; 
		}
		else
		{
			upperName += c ; 
		}
		i++ ; 
	}
	
	return upperName; 
}

void Enemy::attack(Player &other)
{
	cout << "I am mighty!" << endl ; 
	
	other.takeDamage(this-> baseDMG) ; 
}

void Enemy::taunt(Player &other) 
{
	// says mean words 
	cout << "You are mean, " << other.getName() << "! :(" << endl ; 
}

void Enemy::improvedAttack(Player &other)
{
	cout << "You shall suffer!" << endl ; 
	
	other.takeDamage(this-> baseDMG * 3) ; 
}

void Enemy::death()
{
	cout << "Curses! You have bested me!" << endl ; 
}