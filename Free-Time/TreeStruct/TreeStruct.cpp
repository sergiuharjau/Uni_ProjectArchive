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
	if (find(element) == -1)
	{
		cout << " This element already exists in the heap. Skipping it. " << endl ;
	}	
	else if (this-> size < this-> capacity)
	{
		this-> size += 1 ; 
		this-> elements.emplace_back(element) ; 		
		this-> heaps = size / 2.f ; 
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
	
}

int TreeStruct::find(string element)
{
	int desiredHeap = 1 ; 
	int count = 0 ; 
	
	for (int i = 1 ; i < getHeaps() ; i ++)
	{
		//cout << "Inside for loop" << endl ; 

		if (element == elements[getHeapIndex(i)[0]])
		{
			cout << count << endl ; 
			return i ; 
		}
		else if (i != desiredHeap) 
		{
			//
		}
		else
		{
			count += 1 ; 
			int parentIndex = getHeapIndex(i)[0] ; // returns the vector of heap, position 0 is parent index 
			cout << "Parent index "<< parentIndex << endl ; 
			cout << "Heap Number " << i << endl ; 
			if (element < elements[parentIndex])
			{
				cout << element << " is smaller than " << elements[parentIndex] << endl ; 
				desiredHeap = 2 * i -1  ; 
				cout << "We go left to desired heap " << desiredHeap << endl ; 
			}
			else
			{
				cout << element << " is bigger than " << elements[parentIndex] << endl ; 
				desiredHeap = 2 * i + 1 -1 ; 
				cout << "We go right to desired heap " << desiredHeap << endl ; 
			}
		}
	}
	
	return 0 ; // change to 0 
}

vector<int> TreeStruct::getHeapIndex(int number)
{
	vector <int> result = {-1,-1,-1}; 
	
	if (number <= this-> getHeaps() + 1 )
	{
		result[0] = number - 1 ; // Parent 
		if (2*number > getSize()) result[1] = -1; // if it has no first child = -1 
		else result[1] = 2*number -1 ; // First Child 
		
		if (2*number + 1> getSize()) result[2] = -1 ; // if it has no second child = - 1 
		else result[2] = 2*number + 1 - 1; // Second Child 
	}
	
	return result ; // if we get -1 -1 -1, Heap does not exist 
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