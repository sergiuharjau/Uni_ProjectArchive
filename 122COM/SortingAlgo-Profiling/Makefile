all: a.out
	./a.out

a.out: profilingTests.o SergeLib.o
	g++ --std=c++14 profilingTests.o SergeLib.o 

profilingTests.o: profilingTests.cpp
	g++ --std=c++14 profilingTests.cpp -c 

SergeLib.o: ../SergeLib/SergeLib.cpp
	g++ --std=c++14 ../SergeLib/SergeLib.cpp -c 
	
clean: 
	rm *.o a.out 