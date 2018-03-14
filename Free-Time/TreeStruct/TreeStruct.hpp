#ifndef TREESTRUCT_HPP
#define TREESTRUCT_HPP

#include <iostream>
#include <string>
#include <vector> 
#include <cmath> 

using namespace std;

class TreeStruct
{
public:
    TreeStruct() ;
	
	void appendElement(string element) ; 
	void appendVector(vector<string> elements) ; 
	
	void increaseCapacity(int value) ; // += pow(2,value)
	
	void sort() ; 	
	string find(string element) ; 
	
	string popLast() ; 
	string popFirst() ; 
	
	string getLast() ; 
	string getFirst() ; 
	
	int getSize() ; 
	int getHeaps() ; 
	
	vector<string> getElements() ;  
	
private:
	unsigned int capacity ; // max 2^32 elements
	int size ; 
	int heaps ; 
	
	vector <string> elements ; 
	
	bool sorted ; 
};



#endif 