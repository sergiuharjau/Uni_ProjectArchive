#include "TreeStruct.hpp" 

using namespace std; 

int main()
{
	TreeStruct tree ; 
	
	while (true)
	{
		string d ; 
		
		tree.appendVector({"loleanu", "dota2"}) ; 
		cout << "Size "<< tree.getSize() << endl ; 
		cout << "Heaps "<< tree.getHeaps() << endl ;
		cout << "Elements " ; 
		for (string c: tree.getElements())
		{
			cout << c << " " ; 	
		}

		cout << endl ; 
		cout << tree.getFirst() << " " << tree.getLast() << endl ; 
		cin >> d ; 
	}
	return 0 ;
}