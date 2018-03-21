#include "SergeLib.hpp" 

using namespace std ; 

int main() 
{
   // SergeLib object ; 
    
    vector<int> unsorted = {3, 9, 2 , 5, 18, 1} ; 
    
    SergeLib::selectionSort(unsorted.begin() , unsorted.end() ) ; 
    
    for (int element : unsorted)
    {
        cout << element << endl ; 
    }
    
    return 0 ; 
}