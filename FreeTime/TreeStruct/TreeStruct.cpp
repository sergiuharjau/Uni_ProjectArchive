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

void TreeStruct::sort()
{
	vector <string> sortedElements ;
	float size = this-> elements.size()  ;
    bool firstTime = true ; 
	
	for (int i = 0 ; i < size  ; i ++)
	{
		
		int percent = i / size * 100.f; 
		
		cout << percent << " percent."<< endl ; 
		
		int heaps = getHeaps() ; 
		
		
		if (firstTime == true)	
		{ // runs on first time
			for (int i = heaps ; i > 0 ; i --)
			{
				//cout << "Heap nr: " << i << endl ; 

				vector <int> indexes = getHeapIndex(i) ; 		

				int parentIndex = indexes[0] ;
				int firstCIndex = indexes[1] ; 
				int secondCIndex = indexes[2] ;

				string parent = this-> elements[parentIndex] ; 
				string firstC = this-> elements[firstCIndex] ;
				string secondC ; 
				if ( secondCIndex == -1 )
				{
					secondC = "" ; 
				}
				else 
				{
					secondC = this-> elements[secondCIndex] ;
				}

				if ( parent < firstC and (parent < secondC or secondC == "" )) 
				{
					// 
				}
				else if (firstC < secondC or secondC == "")
				{
					//cout << "swap first and parent" << endl ; 
					swap( this-> elements[parentIndex] , this-> elements[firstCIndex] ) ; 

				}
				else
				{
					//cout << "swap second and parent" << endl ; 
					swap ( this-> elements[parentIndex] , this-> elements[secondCIndex] ) ;

				}
				
				firstTime = false ; 
			}
		}
		else
		{ // runs on every other time
			int desiredHeap = 1 ;  
			for (int i = 1 ; i <= log2( this-> getSize() ) ; i ++ )
			{
				
				vector <int> indexes = getHeapIndex(desiredHeap) ; 		
				
				int count = 0 ;
				
				for (int x : indexes)
				{
					if ( x == -1 ) count += 1 ; 
				}
				
				if (count == 3) break ;
				
				int parentIndex = indexes[0] ;
				int firstCIndex = indexes[1] ; 
				int secondCIndex = indexes[2] ;

				string parent = this-> elements[parentIndex] ; 
				string firstC = this-> elements[firstCIndex] ;
				string secondC ; 
				
				if ( secondCIndex == -1 )
				{
					secondC = "" ; 
				}
				else 
				{
					secondC = this-> elements[secondCIndex] ;
				}

				if ( parent < firstC and (parent < secondC or secondC == "" )) 
				{
					// 
				}
				else if (firstC < secondC or secondC == "")
				{
					swap( this-> elements[parentIndex] , this-> elements[firstCIndex] ) ; 
					desiredHeap = i * 2 ;

				}
				else
				{ 
					swap ( this-> elements[parentIndex] , this-> elements[secondCIndex] ) ;
					desiredHeap = i * 2 + 1 ;
				}			
			}				
		}
		//cout << i << endl ; 
		//cout << "Current elements: " ; 
		//for (string c : elements)
		//{
		//	cout << c << " "; 
		//}
		//cout << endl ; 
		
		//cout << "First element: " << elements[0] << " Last element: " << elements[elements.size() - 1] << endl ; 

		swap (this-> elements[0] , this-> elements[this->elements.size() - 1]) ; 
		sortedElements.emplace_back( this-> popLast() ) ;
		
		//cout << "Updated elements: " ;
		//for (string c : elements)
		//{
		//	cout << c << " " ; 
		//}
		///cout << endl ; 
				
		//cout << "Sorted elements " << endl ; 
		//for (string c: sortedElements)
		//{
		//	cout << c << " " ; 
		//}
		//cout << endl ; 
	}
	
	this-> elements = sortedElements ; 
}
int TreeStruct::find(string element)
{
	
}

vector<int> TreeStruct::getHeapIndex(int number)
{
	vector <int> result = {-1,-1,-1}; 
	
	if (number <= this-> getHeaps() )
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
	elements.erase(elements.end() -1) ; 
		
	this-> size -= 1 ; 
	this-> heaps = this-> size / 2 ; 
	
	return result ; 
}

string TreeStruct::popFirst()
{
	string result = this-> elements[0] ; 
	this-> elements.erase(elements.begin()) ; 
		
	this-> size -= 1 ; 
	this-> heaps = this-> size / 2 ; 
	
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