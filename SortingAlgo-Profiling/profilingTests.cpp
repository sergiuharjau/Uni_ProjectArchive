#include "../SergeLib/SergeLib.hpp"

using namespace std; 

int main() 
{
	string userInput ; 

	cout << "Choose amount of elements: " ; 

	cin >> userInput ; 

	int amountElements = stoi(userInput) ; 

	cout << "Constructing big vector, may take a while with big numbers." << endl ; 

	vector<int> sequence ; 
	srand(time(NULL)) ; // seeds rand, makes sure we get new numbers every time 

	for (int i = amountElements ; i > 0 ; i--)
	{
		sequence.emplace_back( rand() % amountElements ) ; // div, so max element will be amountElements 
	}

	cout << "Done! Which sorting algorithm do you want to choose? " << endl ; 
	cout << "1. Bubble Sort" << endl << "2. Selection Sort" << endl << "3. Quick Sort" << endl ; 
	int choice ; 
	cin >> choice ;

	cout << "Running. May take a while with worse algos." << endl ; 

	clock_t start = SergeLib::startWatch() ; 

	if (choice > 3) 
	{
		//throw error 
	}
	else if (choice == 1)
	{
		SergeLib::bubbleSort( sequence.begin() , sequence.end() ) ;
	}
	else if (choice == 2)
	{
		SergeLib::selectionSort( sequence.begin() , sequence.end() ) ; 
	}
	else if (choice == 3)
	{
		SergeLib::quickSort( sequence.begin() , sequence.end() ) ; 
	}

	double duration = SergeLib::stopWatch(start) ; 

	cout << "ALgorithm run time: " << duration << " seconds." << endl ; 

	cout << "Is it really sorted? " << SergeLib::sortedCheck( sequence.begin() , sequence.end() ) << endl; 

	return 0 ; 
}