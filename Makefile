all: a.out 
	./a.out
	
a.out: main.o SergeLib.o
	g++ --std=c++14 main.o SergeLib.o 
	
main.o: main.cpp
	g++ --std=c++14 -c main.cpp

SergeLib.o: SergeLib.cpp
	g++ --std=c++14 -c SergeLib.cpp 

clean: 
	rm *o a.out 