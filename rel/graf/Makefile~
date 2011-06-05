# Programa para benchmark
CC = gcc
CFLAGS = -g -Wall -lpthread
LIBS = -lm
OBJS = main.o banco.o lista.o locker.o test_threads.o
EXEC = run

all: $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) $(LIBS) -o $(EXEC)

run: all
	./$(EXEC)

$(OBJS): %.o: %.c
	$(CC) -c $(CFLAGS) $<

clean:
	rm -f $(OBJS) $(EXEC) *~

#Relatorio
file=lab2
rel:
	latex $(file).tex
	latex $(file).tex
	dvips $(file).dvi -o
	ps2pdf13 $(file).ps
relshow:
	evince $(file).pdf
relClean:
	rm *.dvi *.aux *.out *.log
