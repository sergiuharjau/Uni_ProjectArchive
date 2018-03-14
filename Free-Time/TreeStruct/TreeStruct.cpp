#include "TreeStruct.hpp"

using namespace std ;


TreeStruct::TreeStruct() 
{
	this-> capacity = pow(2,16)	; 
	this-> size = 0 ; 
	this-> elements = {} ; 
	this-> heaps = 0 ; 
	this-> sorted = false ; 
}

void TreeStruct::appendElement(string element)
{	
	if (this-> size < this-> capacity)
	{
		this-> size += 1 ; 
		this-> elements.emplace_back(element) ; 		
		this-> heaps = log2(size) ; 
	}
	else
	{
		cout << ("No room left. Try increasing capacity first.") << endl ; 
	}
}

void TreeStruct::appendVector(vector<string> elements)
{
	for (string element : elements)
	{
		appendElement(element) ; 
	}
}

void TreeStruct::increaseCapacity(int value)
{
	if (this-> capacity + pow(2,value) < pow(2,32) -1 )
	{
		this-> capacity += pow(2,value) ; 
		cout << "Max capacity: " << this-> capacity << endl ; 
	}
	else
	{
		cout << "No one needs more than 4 billion elements." << endl ; 
		this-> capacity = pow(2,32 ) -1 ; 
		cout << "Max Capacity: " << this -> capacity << endl ; 
	}
}

void sort()
{
	//
	//
	//
	//
	//
	//
	
}

string TreeStruct::find(string element)
{
	//
	//
	//
	//
	//
	//
}

string TreeStruct::popLast()
{
	string result = elements[getSize() - 1 ] ; 
	elements.erase(elements.end()) ; 
		
	this-> size -= 1 ; 
	
	return result ; 
}

string TreeStruct::popFirst()
{
	string result = this-> elements[0] ; 
	this-> elements.erase(elements.begin()) ; 
		
	this-> size -= 1 ; 
	
	return result ; 
}

string TreeStruct::getLast()
{
	return this-> elements [getSize() -1] ; 
}

string TreeStruct::getFirst()
{
	return this-> elements [0] ; 
}

int TreeStruct::getSize()
{
	return this-> size ; 
}

int TreeStruct::getHeaps()
{
	return this-> heaps ; 
}

vector<string> TreeStruct::getElements()
{
	return this-> elements ; 
}