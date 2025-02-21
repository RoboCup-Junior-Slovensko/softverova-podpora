#include <errno.h>
#include <time.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>

#include "pngwriter.h"
#include "camera_module.h"


extern int to_exit;


void save_png_frame(uint8_t *RGB)
{
      printf ("zapisujem obrazok...\n");
  
      static int counter = 0;
      char filename[30];
      sprintf(filename, "image%d.png", counter++);
      
#ifdef POUZI_YUV
      write_yuv422_png_image((uint8_t *)RGB, filename, 1920, 1080);
#else
      write_bgr_png_image((uint8_t *)RGB, filename, 1920, 1080);
#endif

      if (counter == 5) to_exit = 1;
}

int capture_images()
{
    // do suborov ulozime 5 obrazkov
    for (int i = 0; i < 5; i++)
    {
    }

    return 0;
}
 
int main()
{
        setup_camera_callback(save_png_frame);

        camera_main();

        return 0;
}
