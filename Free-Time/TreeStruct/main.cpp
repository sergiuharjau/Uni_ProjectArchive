#include "TreeStruct.hpp" 

using namespace std; 

int main()
{
	TreeStruct tree ; 
	
	while (true)
	{
		string d ; 
		
		tree.appendVector({"1", "2", "3", "4", "5", "6", "7","8","9","10","11","12"}) ;  
		cout << "Elements " ; 
		for (string c: tree.getElements())
		{
			cout << c << " " ; 	
		}

		cout << endl ; 
		cout << "Size "<< tree.getSize() << endl ;
		cout << "Heaps "<< tree.getHeaps() << endl ;
		
		cout << tree.find("2") << endl ; 
		
		cin >> d ; 
	}
	return 0 ;
}