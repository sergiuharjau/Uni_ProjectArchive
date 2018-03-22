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
    string sortedCheck(ITER begin, ITER end) ;
    
    template <typename ITER> 
    void bubbleSort (ITER begin, ITER end) ;

    template <typename ITER>   
    void selectionSort (ITER begin, ITER end) ; 

    template <typename ITER> // works only vectors(of anything) currently     
    void quickSort (ITER begin, ITER end) ; 

    template <typename ITER>   
    void insertionSort (ITER begin, ITER end) ; 
    
    template <typename ITER>  
    void mergeSort (ITER begin, ITER end) ;
    
    template <typename ITER>  
    int bogoSort (ITER begin, ITER end) ; //returns number of tries until sorted 
   
    template <typename ITER>      
    void sleepSort (ITER begin, ITER end) ; //cout the numbers in order 
    
    clock_t startWatch() ; 
    
    double stopWatch(clock_t start) ; 

   /*  DAVID COMMENTS 
    stattic classes and functions 
    namespace is better 
    look into sorting with iterators 
    we implement templates in the header file since they can't compile before
    we would split other functions (not templates) into cpp for performance issues though'*/ 
};

// TEMPLATES GO IN THE HEADER FILE 

template <typename ITER> 
string SergeLib::sortedCheck(ITER begin, ITER end)
{
    string sorted = "sorted!" ;
    for (ITER it = begin ; it != prev(end) ; it = next(it))
    {                           // so we don't go out of bounds 
        if (*it > *next(it))
        {
            sorted = "not sorted." ;
            break ; 
        }
    }
    return sorted ; 
}

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
        end = prev(end) ; 
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
           
template <typename ITER >     
void SergeLib::quickSort (ITER begin, ITER end) 
{ 
    ITER pivot = begin + (end-begin)/2 ; // middle iterator, pivot 
    int pivotCount ; 
    
    vector< typename iterator_traits<ITER>::value_type > lessThan ; // gives the iterator type, such as vector<int> 
    vector< typename iterator_traits<ITER>::value_type > moreThan ;  
    vector< typename iterator_traits<ITER>::value_type > sortedSequence ; 
    
    for (ITER it = begin ; it !=end ; it = next(it))
    {
        if (*it < *pivot)
        {
            lessThan.emplace_back(*it) ; 
        }
        else if (*it > *pivot)
        {
            moreThan.emplace_back(*it) ; 
        }
        else
        {
            pivotCount ++ ; 
        }
    }
    
    if (lessThan.size() == 0)
    {
        //
    }
    else if (lessThan.size() == 1)
    {
        sortedSequence.emplace_back(*lessThan.begin()) ; 
    }
    else
    {
        SergeLib::quickSort( lessThan.begin() , lessThan.end() ) ; //sorts the exact same list
        
        for (ITER it = lessThan.begin() ; it != lessThan.end() ; it = next(it))
        {    // loops through with iterators 
            sortedSequence.emplace_back(*it) ; // add dereferenced iterator to Sorted 
        }
    }
    
    
    for (int i = 0 ; i < pivotCount ; i++)
    {
        sortedSequence.emplace_back(*pivot) ; 
    }
    
    
    if (moreThan.size() == 0)
    {
        //
    }
    else if (moreThan.size() == 1)
    {
        sortedSequence.emplace_back(*moreThan.begin()) ; 
    }
    else
    {
        SergeLib::quickSort( moreThan.begin() , moreThan.end() ) ; //sorts the exact same list
        
        for (ITER it = moreThan.begin() ; it != moreThan.end() ; it = next(it))
        {    // loops through with iterators 
            sortedSequence.emplace_back(*it) ; // add dereferenced iterator to Sorted 
        }
    }
    
    int i = 0 ;
        
    for (ITER it = begin; it != end ; it = next(it))
    {
        *it = sortedSequence[i];
        i++ ; 
    }
}


#endif  