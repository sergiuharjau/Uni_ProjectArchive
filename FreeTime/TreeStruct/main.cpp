#include "TreeStruct.hpp" 
#include <fstream> 
using namespace std; 


vector <string> readPasswords(string filename)
{
	vector <string> pwdVector {} ; 

	string password ; 
	
	ifstream inFile ; 
	
	inFile.open(filename);
	
	if (!inFile)
	{
		cerr << "Unable to open file datafile.txt" ;
		exit(1) ;   // call system to stop
	}

	while (inFile >> password) 
	{
		pwdVector.emplace_back(password) ;
	}
	
	inFile.close() ;
	
	return pwdVector ; 
}


int main()
{
	TreeStruct tree ; 
	
	while (true)
	{
		string d ; 
		
		tree.appendVector(readPasswords("linkedin_passwords.txt")) ;  
		
		tree.appendVector({"b" ,"c","d","e","a"}) ; 
		
		cout << "Elements " ; 
		for (string c: tree.getElements())
		{
			cout << c << " " ; 	
		}

		cout << endl ; 
		
		cout << "Size "<< tree.getSize() << endl ;
		cout << "Heaps "<< tree.getHeaps() << endl ;
		
		tree.sort() ; 
		cout << "Sorted elements " ; 
		for (string c: tree.getElements())
		{
			cout << c << " " ; 
		}
		cout << endl ; 
		
		cin >> d ; 
	}
	return 0 ;
}