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
	int find(string element) ; 
	
	string popLast() ; 
	string popFirst() ; 
	
	string getLast() ; 
	string getFirst() ; 
	
	int getSize() ; 
	int getHeaps() ; 
	
	vector<string> getElements() ;  
	
	vector<int> getHeapIndex(int number) ; // Gets the indexes of Parent + Children of heap # 
									//returns-> 0 - Parent, 1- Left Child, 2- Right Child 
	void setHeap(vector<int> order, int number) ; 
									// Sets a certain heap, with a vector of the right order
									// order = {2, 0, 1} = right child should be parent, etc 
private:
	unsigned int capacity ; // max 2^32 elements
	int size ; 
	int heaps ; 
	
	vector <string> elements ; 
	
	bool sorted ; 
};



#endif 