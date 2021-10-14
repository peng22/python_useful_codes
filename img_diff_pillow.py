from PIL import Image, ImageChops

img1=Image.open('path_to_image1')
img2=Image.open('path_to_image2')


diff=ImageChops.difference(img1,img2)

#show the difference if they have difference between them
if diff.getbbox():
    diff.show()
