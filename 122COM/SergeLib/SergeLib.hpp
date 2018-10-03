#ifndef SERGELIB_HPP
#define SERGELIB_HPP

#include <iostream> 
#include <vector> 
#include <string> 
#include <algorithm> 

using namespace std;

namespace SergeLib 
{  
// Sorting algorithms
    template <typename ITER> // O(n), checks if sorted 
    bool sortedCheck(ITER begin, ITER end) ;
    
    template <typename ITER> // O(n^2), works good on small sequences 
    void bubbleSort (ITER begin, ITER end) ;

    template <typename ITER> // Generally better than bubble, worse than quick   
    void selectionSort (ITER begin, ITER end) ; 

    template <typename ITER> // O(n log(n), generally great all around 
    void quickSort (ITER begin, ITER end) ; // only works on vectors(of anything) 
   
    template <typename ITER> // dear god don't use this  
    int bogoSort (ITER begin, ITER end) ; 

    
//Profiling Tools 
    clock_t startWatch() ; // returns clock_t object, we pass that to the stopWatch() 
    double stopWatch(clock_t start) ; // returns time in seconds as a double 

    
// Searching algortihms 
    template <typename ITER, typename T> // O(n) complexity 
    bool isElement(ITER begin, ITER end, T element) ; // returns bool, true or false 
                    
    template <typename ITER, typename T>
    ITER getElement(ITER begin, ITER end, T element) ; // returns iterator of first occurance of element, or ITER end (0)
    
    template <typename ITER, typename T> // O(log(n)) complexity 
    bool isElementDQ(ITER begin, ITER end, T element) ; // Only works on sorted, much faster  
    
    template <typename ITER, typename T> 
    ITER getElementDQ(ITER begin, ITER end, T element) ;  // Only works on sorted, much faster 
    
    
   /*  DAVID COMMENTS 
    static classes and functions 
    namespace is better 
    look into sorting with iterators 
    we implement templates in the header file since they can't compile before
    we would split other functions (not templates) into cpp for performance issues though'*/ 
};

// TEMPLATES GO IN THE HEADER FILE 

template <typename ITER> 
bool SergeLib::sortedCheck(ITER begin, ITER end)
{
    bool sorted = true ;
    for (ITER it = begin ; it != prev(end) ; it = next(it))
    {                           // so we don't go out of bounds 
        if (*it > *next(it))
        {
            sorted = false ;
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
        for(ITER iter = begin ; iter != prev(end) ; iter = next(iter))
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
           
template <typename ITER >     
void SergeLib::quickSort (ITER begin, ITER end) 
{ 
    ITER pivot = begin + (end-begin)/2 ; // middle iterator, pivot 
    int pivotCount ; 
    
    vector <typename iterator_traits<ITER>::value_type > lessThan ; // gives the iterator type, such as int 
    vector <typename iterator_traits<ITER>::value_type > moreThan ;  
    vector <typename iterator_traits<ITER>::value_type > sortedSequence ; 
    
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
        *it = sortedSequence[i]; // reassign everything to original sequence 
        i++ ; 
    }
}

template <typename ITER> 
int SergeLib::bogoSort(ITER begin, ITER end)
{
    int count = 0 ; // amount of tries 
    
    while(true)
    {
        if (sortedCheck(begin, end) == true)
        {
            return count ; 
        }
        random_shuffle(begin, end) ; 
        count ++ ; 
    }
    
}


template <typename ITER, typename T> 
bool SergeLib::isElement(ITER begin, ITER end, T element) 
{
    bool result = false ; 
    
    for (ITER it = begin ; it != end ; it = next(it))
    {
        if (*it == element)
        {
            result = true ; 
            break ; 
        }
    }
    return result ;    
}

template <typename ITER, typename T> 
ITER SergeLib::getElement(ITER begin, ITER end, T element)
{
    ITER it ; //if we declare inside for loop, we go outside scope 
    
    for (it = begin ; it != end ; it = next(it))
    {
        if (*it == element)
        {
            break ; 
        }
    }
    return it ; 
}

template <typename ITER, typename T> 
bool SergeLib::isElementDQ(ITER begin, ITER end, T element)
{     // means it only works on contiguous sequences  
    ITER it = begin  + (end-begin)/2 ; // midle iterator 
         
    if (*it == element) return true  ; // if middle is element, bingo 
  
    if (*it > element) // if it's bigger than *it, look in the smaller ones 
    {
        if (begin + 1 == it) return false ; // if size is 0, return false 
        return isElementDQ(begin, it, element) ; 
    }
    else // vice versa 
    {
        if (it+1 = end) return false ; // size 0 --> false 
        return isElementDQ(it+1, end, element) ; 
    }
}

template <typename ITER, typename T> 
ITER SergeLib::getElementDQ(ITER begin, ITER end, T element)
{  // means it only works on contiguous seqeunces 
    ITER it = begin  + (end-begin)/2 ; // middle iterator 
    
    if (*it == element) return it  ; // if middle is element, bingo 
  
    if (*it > element) // if it's bigger, look in the smaller ones 
    {
        if (it == begin) return begin ; // Throw error in the future 
        return getElementDQ(begin, it, element) ; 
    }
    else // vice versa 
    {
        if (it+1 == end) return it+1 ; // Throw error in the future 
        return getElementDQ(it+1, end, element) ; 
    }
      
}

#endif  