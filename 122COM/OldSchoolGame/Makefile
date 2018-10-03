CC = g++ --std=c++14

all: a.out 
	./a.out 

a.out: main.o player.o fighter.o enemy.o Saving.o
	$(CC) main.o player.o fighter.o enemy.o Saving.o -lsqlite3

main.o: main.cpp
	$(CC) -c main.cpp 
    
player.o: player.cpp
	$(CC) -c player.cpp 

fighter.o: fighter.cpp
	$(CC) -c fighter.cpp 

enemy.o: enemy.cpp
	$(CC) -c enemy.cpp 

Saving.o: ..//Saving.cpp
	$(CC) -c ..//Saving.cpp

clean: 
	rm *o ./a.out