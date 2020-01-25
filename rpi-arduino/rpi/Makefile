LIBS=-lpthread

CCOPT=-std=c99 -D_DEFAULT_SOURCE

all: priklad_komunikacie

priklad_komunikacie:	priklad_komunikacie.c
	gcc -o priklad_komunikacie $^ $(LIBS) $(CCOPT)

clean:
	rm -f priklad_komunikacie
