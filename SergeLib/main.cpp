#include "SergeLib.hpp" 

using namespace std ; 

// Used for testing SergeLib

int main() 
{
   // SergeLib object ; 
    vector<int> unsorted ; 
    srand(time(NULL)) ; 
    
    int testSize = 11 ; //1 billion 
    for (int i = 0 ; i < testSize ; i ++ )
    {
        unsorted.emplace_back(rand() % 100) ; 
    } 
    
    cout <<  "Sorted? "<< SergeLib::sortedCheck(unsorted.begin() , unsorted.end() ) << endl ; 
    
    clock_t start = SergeLib::startWatch() ; 
    
    
    cout << "Tries: " << SergeLib::bogoSort( unsorted.begin() , unsorted.end() ) << endl ; // actual sorting happens here 
    
    
    cout << "Elapsed seconds: " << SergeLib::stopWatch(start) << endl ; 
    
    cout << "Sorted? "<< SergeLib::sortedCheck( unsorted.begin() , unsorted.end()) << endl ; 
        
    
    start = SergeLib::startWatch() ; 
     
    cout << "Element, DQ " << *SergeLib::getElementDQ( unsorted.begin() , unsorted.end() , 99) << endl ; 
    
    
    
    cout << "Elapsed seconds: " << SergeLib::stopWatch(start) << endl ; 
 
    return 0 ; 
}