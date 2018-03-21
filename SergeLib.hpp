#ifndef SERGELIB_HPP
#define SERGELIB_HPP

#include <iostream> 
#include <vector> 
#include <string> 

using namespace std;

namespace SergeLib 
{  
    // sorting algorithms for any container 
    
    template <typename ITER> 
    void bubbleSort (ITER begin, ITER end) ;

    template <typename ITER>   
    void selectionSort (ITER begin, ITER end) ; 

    template <typename ITER>     
    void quicksort (ITER begin, ITER end) ; 

    template <typename ITER>   
    void insertionSort (ITER begin, ITER end) ; 
    
    template <typename ITER>  
    void mergeSort (ITER begin, ITER end) ;
    
    template <typename ITER>  
    int bogoSort (ITER begin, ITER end) ; //returns number of tries until sorted 
   
    template <typename ITER>      
    void sleepSort (ITER begin, ITER end) ; //cout the numbers in order 
 
    
    // searching algorithms 
    // 
    // stopwatch of milliseconds 
    // 
    // read a file into a vector 
    // 
    
   /*  DAVID COMMENTS 
    stattic classes and functions 
    namespace is better 
    look into sorting with iterators 
    we implement templates in the header file since they can't compile before
    we would split other functions (not templates) into cpp for performance issues though'*/ 
};

template <typename ITER> 
void SergeLib::bubbleSort (ITER begin, ITER end)
{
    bool sortedCheck = false ; 
    while (sortedCheck == false)
    {
        sortedCheck = true ; 
        for(ITER iter = begin ; iter != end ; iter = next(iter))
        {
            if (*iter > *next(iter)) // if not in order, swap 
            {
                iter_swap(iter,next(iter)) ;
                sortedCheck = false ; // if we swap, it means they're not in order 
            }
        }
    } 
} 

template <typename ITER>
void SergeLib::selectionSort (ITER begin, ITER end)
{
    for (ITER iter = begin ; iter !=end ; iter = next(iter))
    {
        ITER iterMin = iter ; 
        
        for (ITER nestedIter = next(iter) ; nestedIter != end ; nestedIter = next(nestedIter))
        {
            if (*nestedIter <  *iterMin)
            {
                iterMin = nestedIter ; 
            }
        }

        iter_swap(iterMin, iter) ;    
    }  
}
           
           
           
           
#endif  