all: a.out 
	./a.out
	
a.out: SergeLib.o main.o 
	g++ --std=c++14 SergeLib.o main.o 
	
main.o: main.cpp
	g++ --std=c++14 -c main.cpp
	
SergeLib.o: SergeLib.cpp
	g++ --std=c++14 -c SergeLib.cpp 

clean: 
	rm *o a.out 