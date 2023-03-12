def addNoise(img):
    row,col = img.shape
    pixels = random.randint(100,500) #adjust noise intensity
    
    #adding white noise pixels 
    for i in range(pixels):
        y = random.randint(0, row-1)
        x = random.randint(0, col-1)
        img[y,x] = 255
    
    #adding black noise pixels
    pixels = random.randint(100, 500)
    for i in range(pixels):
        y = random.randint(0, row - 1)
        x = random.randint(0, col - 1)
        img[y, x] = 0

    return img
  
  
def linearFilter(img,kernel_size):

  ##source :https://docs.opencv.org/3.4/d4/dbd/tutorial_filter_2d.html
  ddepth = -1 #-1 = depth same as source
  kernel = np.ones((kernel_size, kernel_size), dtype=np.float32)
  kernel /= (kernel_size * kernel_size)
  imgFiltered = cv2.filter2D(img,ddepth,kernel)

  return imgFiltered
