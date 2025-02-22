#include <errno.h>
#include <fcntl.h>
#include <time.h>
#include <linux/videodev2.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/mman.h>
#include <unistd.h>

#include "pngwriter.h"
#include "camera_module.h"


extern int to_exit;

int sirka = 1920;
int vyska = 1080;
int pocet_opakovani = 300;
 
long long usec()
{
  struct timeval tv;
  gettimeofday(&tv, 0);
  return (1000000L * (long long)tv.tv_sec) + tv.tv_usec;
}

void detect_red_in_frame(uint8_t *RGB)
{
    static int pocitadlo = 0;
    static long long tm;
    if (pocitadlo == 0)  tm = usec();

    if (pocitadlo == pocet_opakovani) 
    {
        to_exit = 1;
        long long tm2 = usec();
        double cas = (tm2 - tm) / 1000000.0;
        printf("celkovy cas: %.2lf s (%.2lf fps)\n", cas, pocet_opakovani / (double)cas);
        return;
    }

    printf ("spracovavam obrazok %d... ", pocitadlo++);

    uint8_t *p = (uint8_t *)RGB;

    int cnt = 0;
    // prechadzame cely obrazok bod po bode...
    // na tomto mieste chcete program upravit podla svojich potrieb...

    for (int i = 0; i < vyska; i++)
    {
      for (int j = 0; j < sirka; j++)
      {
  	      uint8_t r = *(p++);
  	      uint8_t g = *(p++);
  	      uint8_t b = *(p++);

  	      if ((r / 2 > g) && (r / 2 > b))
  	      {
  		      cnt++;
  	      }
      }
      printf("%d cervenych bodov\n", cnt);
    } 
    return;
}
 
int main()
{
        setup_camera_callback(detect_red_in_frame);
        camera_main(sirka, vyska);
        return 0;
}
