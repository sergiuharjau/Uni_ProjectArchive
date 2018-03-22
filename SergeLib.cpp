#include "SergeLib.hpp"

using namespace std ;

// TEMPLATES GO IN THE HEADER FILE 

clock_t SergeLib::startWatch() 
{
    clock_t start = clock() ; 
    
    return start ; 
}
 
double SergeLib::stopWatch(clock_t start)
{
    clock_t elapsedTicks = clock() - start ; 
    
    double elapsedSeconds = (float)elapsedTicks / CLOCKS_PER_SEC ;
    
    return elapsedSeconds ; 
}

