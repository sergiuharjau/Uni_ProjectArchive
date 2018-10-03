#include <iostream>
#include <string>
#include <vector> 
#include <cstdlib>
using namespace std ; 

int input_int()
{
    int userInput ;
    try
    {
        cin >> userInput ;
    }
    catch(...)
    {
        cout << "Wrong type" << endl ;
    }

    return userInput ;
}

int main()
{
    int starting_number = input_int() ; 
    
    vector<int> choice {}  ;  
    
    float steps = 0 ;
    
    int min_steps = 1000 ;
    
    float average = 0 ; 
    
for(int i = 0 ; i < 1000 ; i ++)   
{
    cout << "Simulation number " << i << endl ; 
    int number = starting_number ;

    while (true)
    {
        if (number == 1 or number == 0) break ;
        
        if (number / 3 == number / 3 + number % 3)
        {
            choice.emplace_back(0) ;
            number = number / 3 ;
        }
        else
        {
            int rng = rand() % 2 ; 
            if (rng == 1)
            {
                number -= 1 ;
                choice.emplace_back(-1) ;
                number = number / 3 ; 
            }
            else
            {
                number += 1 ;
                choice.emplace_back(1) ;
                number = number / 3 ;
            }
        }
        
        steps += 1 ; 
    }
    
    if (steps < min_steps)
    {
        min_steps = steps ; 
        vector<int> best_choice = choice ; 
    } 
    
    average += steps ;
    
    cout << steps << endl; 
    steps = 0 ;
    
    choice = {} ; 
    
}   
    cout << average << endl; 
    
    average = average / 1000.0 ;
        
    cout << "We can do it in " << min_steps << " steps" << endl ; 
    
    cout << "Average steps: " << average << endl; 
    
    return 0 ;
}