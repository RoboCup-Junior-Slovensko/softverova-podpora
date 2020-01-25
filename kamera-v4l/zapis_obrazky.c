#include <errno.h>
#include <fcntl.h>
#include <linux/videodev2.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/mman.h>
#include <unistd.h>
#include "pngwriter.h"

uint8_t *buffer;
 
static int xioctl(int fd, int request, void *arg)
{
        int r;
 
        do r = ioctl (fd, request, arg);
        while (-1 == r && EINTR == errno);
 
        return r;
}
 
int setup_format(int fd)
{
        struct v4l2_format fmt = {0};
        fmt.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
        fmt.fmt.pix.width = 640;
        fmt.fmt.pix.height = 480;

        // ak vasa kamera nepodporuje BGR24, m ozno podporuje YUV420,
        // ale v tom pripade bude treba obrazok spracovavat v tom
        // formate, alebo si ho skonvertovat...

        //fmt.fmt.pix.pixelformat = V4L2_PIX_FMT_YUV420;
        fmt.fmt.pix.pixelformat = V4L2_PIX_FMT_BGR24;

        fmt.fmt.pix.field = V4L2_FIELD_NONE;
        
        if (-1 == xioctl(fd, VIDIOC_S_FMT, &fmt))
        {
            perror("nepodarilo sa nastavit format");
            return 1;
        }
 
        return 0;
}
 
int init_mmap(int fd)
{
    struct v4l2_requestbuffers req = {0};
    req.count = 1;
    req.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    req.memory = V4L2_MEMORY_MMAP;
 
    if (-1 == xioctl(fd, VIDIOC_REQBUFS, &req))
    {
        perror("nepodarilo sa inicializovat mmap buffer");
        return 1;
    }
 
    struct v4l2_buffer buf = {0};
    buf.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    buf.memory = V4L2_MEMORY_MMAP;
    buf.index = 0;
    if(-1 == xioctl(fd, VIDIOC_QUERYBUF, &buf))
    {
        perror("nepodarilo sa vytiahnut smernik na mmap buffer");
        return 1;
    }
 
    buffer = mmap (NULL, buf.length, PROT_READ | PROT_WRITE, MAP_SHARED, fd, buf.m.offset);
 
    return 0;
}
 
int capture_images(int fd)
{
    struct v4l2_buffer buf = {0};
    buf.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;

    if(-1 == xioctl(fd, VIDIOC_STREAMON, &buf.type))
    {
        perror("nepodarilo sa zapnut snimanie kamery");
        return 1;
    }

    // do suborov ulozime 5 obrazkov
    for (int i = 0; i < 5; i++)
    {
      buf.memory = V4L2_MEMORY_MMAP;
      buf.index = 0;
      if(-1 == xioctl(fd, VIDIOC_QBUF, &buf))
      {
          perror("nepodarilo sa poziadat o mmap buffer");
          return 1;
      }
   
      fd_set fds;
      FD_ZERO(&fds);
      FD_SET(fd, &fds);
      struct timeval tv = {0};
      tv.tv_sec = 2;
      int r = select(fd+1, &fds, NULL, NULL, &tv);
      if(-1 == r)
      {
          perror("pocas cakania na dalsi obrazok doslo k chybe");
          return 1;
      }
   
      if(-1 == xioctl(fd, VIDIOC_DQBUF, &buf))
      {
          perror("nepodarilo sa ziskat dalsi obrazok");
          return 1;
      }
      printf ("zapisujem obrazok...\n");
  
      static int counter = 0;
      char filename[30];
      sprintf(filename, "image%d.png", counter++);
      
      //ak ste hore pouzili YUV format:
      //write_yuv422_png_image((uint8_t *)buffer, filename, 640, 480);
  
      write_bgr_png_image((uint8_t *)buffer, filename, 640, 480);
    }

    return 0;
}
 
int main(int argc, char **argv)
{
        int fd;
        // ak mate pripojenych viac kamier, moze to byt napr. /dev/video1 
	const char *device = "/dev/video0";
	if (argc > 1) device = argv[1];
 
        fd = open(device, O_RDWR);
        if (fd == -1)
        {
                perror("nepodarilo sa otvorit zariadenie /dev/videoN...");
                return 1;
        }

        if(setup_format(fd))
            return 1;
        
        if(init_mmap(fd))
            return 1;

        if(capture_images(fd))
            return 1;

        close(fd);
        return 0;
}
