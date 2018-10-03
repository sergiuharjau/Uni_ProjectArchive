#include "fighter.hpp" 
#include "enemy.hpp" 
#include "../Saving.h" 
using namespace std ;

int main()
{
    Fighter player("Serge") ;
    Enemy enemy(1) ;
	Save save ; 
  
    vector <int> choices = {1,2,3,4,5,6,7,8,9,10} ;  
    cout << "" << endl ; 
    cout << "This is our testing bench! We will try out every function, one by one" << endl ; 
    
    for (int c : choices )
    {
        string test ;
        
        if (c == 1)
        {
            cout << " " << endl ; 
            cout << "Attacking the Enemy" << endl ; 
            player.attack(enemy) ; 
        }
        else if (c==2)
        {
            cout << " " << endl ; 
            cout << "Enemy attacks the player" << endl ;
            enemy.attack(player) ;  
        }
        else if (c==3)
        {
            cout << " " << endl ;
            cout << "Player uses defend, then gets attacked" << endl ; 
            player.defend() ; 
            enemy.attack(player) ; 
        }
        else if (c==4)
        {
            cout << " " << endl ;
            cout << "Enemy uses taunt, then gets attacked." << endl ; 
            enemy.taunt(player) ; 
            player.attack(enemy) ; 
        }
        else if(c==5 or c == 6 or c==7)
        {
            cout << " " << endl ;
            cout << "Player levels up, then uses powerAttack()" << endl ; 
            player.levelUP() ; 
            player.powerAttack(enemy) ; 
        }
        else if(c==8)
        {
            cout << " " << endl ;
            cout << "We use expAttack() on the enemy." << endl ; 
            player.expAttack(enemy) ; 
        } 
        else if (c== 9)
        {
			cout << " " << endl ; 
            cout << "We save the Enemy's characteristics to the database, as if it were a player. " << endl ;
			save.NewChar(enemy.saveGame()) ; 
        }
        else if (c == 10)
		{
			cout << " " << endl ; 
			cout << "We load from the database, into our Player object." << endl ; 
			player.loadGame(save.CharacterList()) ; 
		}
        player.giveBrief() ; 
        
        enemy.giveBrief() ;
        
        cin >> test ; 
    }
    
    
    
    return 0 ;
}



