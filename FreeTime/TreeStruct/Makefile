all: a.out 
	./a.out
	
a.out: TreeStruct.o main.o 
	g++ --std=c++14 TreeStruct.o main.o 
	
main.o: main.cpp
	g++ --std=c++14 -c main.cpp
	
TreeStruct.o: TreeStruct.cpp
	g++ --std=c++14 -c TreeStruct.cpp 

clean: 
	rm *o a.out 