LIBS=-lpng

CCOPT=-std=c99

all: zapis_obrazky spracuj_obraz

zapis_obrazky:	zapis_obrazky.c pngwriter.c
	gcc -o zapis_obrazky $^ $(LIBS) $(CCOPT)

spracuj_obraz:	spracuj_obraz.c pngwriter.c
	gcc -o spracuj_obraz $^ $(LIBS) $(CCOPT)

clean:
	rm -f zapis_obrazky spracuj_obraz image[0-5].png
