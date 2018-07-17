#include <iostream> 
#include <string> 
#include <vector>
using namespace std ; 

vector<string> decoderGG(string key, string message)
{
	int i = 0  ;
	int j = 0  ;
	
	vector <string> keyVector ; 
	
	char blank = ' ' ;
	
	for (char c : key )
	{
		if (c == blank)
		{
			keyVector.emplace_back(key[j,i]) ;
			j = i ;
		}
		i += 1 ;
	}
	
	return keyVector ; 
}

int main() 
{
	
	string key = "H GgG d gGg e ggG l GGg o gGG r Ggg w ggg";
	
	vector <string > v = decoderGG(key, "nothing") ; 
	
	for (string element : v )
	{
		cout << element << endl ; 
	}
	
	return 0 ; 
	
}