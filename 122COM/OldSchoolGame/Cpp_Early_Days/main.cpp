#include <iostream>
#include <cstdlib>
#include <string>
#include "fighter.hpp" 

using namespace std ;

int main()
{
    Fighter martin("Martin") ;
    Player enemy("Enemy") ;

    while (true)
    {
        char test;
        martin.expAttack(enemy) ; 
        martin.giveBrief() ;
        enemy.giveBrief() ;
        cin >> test ;
    }
    return 0 ;
}



