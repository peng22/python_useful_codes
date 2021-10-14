from PIL import Image, ImageChops

img1=Image.open('path_to_image1')
img2=Image.open('path_to_image2')


diff=ImageChops.difference(img1,img2)

#show the difference if they have difference between them
if diff.getbbox():
    diff.show()

    
"""
The documentation for this function doesn't tell much in fact. So let me try to clarify it a little. First,
the sizes of the images are irrelevant to whether the function works or not, it internally checks for a size that both images fit.

Now, when can you actually compare the images by using the function ImageChops.difference ?

First, both images have to have pixels that can be stored in an unsigned byte. This is a very common type of image,
but this excludes comparison between images even if they are the same mode. So, 
you cannot compare an image x and y when one or /both/ of them have a mode of: F, I, I;16, I;16L, I;16B, BGR;15, BGR;16, BGR;24, or BGR;32.
Just to make it clear: it doesn't matter if both images are in the same mode if they happen to be in one of the modes above, the function will refuse to work.

So, the comparison can be done when the images are in the modes 
1, P, L, LA, RGB, RGBA, RGBX, RGBa, CMYK, or YCbCr as long as they have the same number of bands. 
This means the images don't have to have the same mode to be compared. 
For instance, difference(x.convert('CMYK'), x.convert('RGBA')) or difference(x.convert('1'), x.convert('P')) work just fine.
Of course this means difference(x.convert('LA'), x.convert('L')), fails. Finally, the resulting image will always h
ave the mode equal to the first image passed to the function.

"""
