main: Chariters.o Lister.o Main.o
	g++ -o main Chariters.o	Lister.o Main.o

Main.o: main.cpp Chariters.h Lister.h
	g++ -c main.cpp

Lister.o: Lister.cpp Chariters.h Lister.h
	g++ -c Lister.cpp

Chariters.o: Chariters.cpp Chariters.h
	g++ -c Chariters.cpp