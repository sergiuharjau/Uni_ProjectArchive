#include "SergeLib.hpp" 

using namespace std ; 

// Used for testing SergeLib

int main() 
{
   // SergeLib object ; 
    vector<int> unsorted ; 
    srand(time(NULL)) ; 
    
    int testSize = 100000 ;  
    for (int i = 0 ; i < testSize ; i ++ )
    {
        unsorted.emplace_back(rand()%testSize) ; 
    } 
    
    cout << SergeLib::sortedCheck(unsorted.begin() , unsorted.end() ) << endl ;     
    clock_t start = SergeLib::startWatch() ;
    
    SergeLib::quickSort( unsorted.begin() , unsorted.end() ) ; 
    
    cout << "Elapsed seconds: " <<SergeLib::stopWatch(start) << endl ;   
    cout << SergeLib::sortedCheck(unsorted.begin() , unsorted.end()) << endl ; 
    
    return 0 ; 
}