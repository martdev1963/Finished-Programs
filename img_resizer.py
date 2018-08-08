import cv2
import glob

images=glob.glob("*.jpg") # list containing the image file path...which in this case is the current directory...

for image in images: # iterate through the list...
    img=cv2.imread(image,-1) # the loop reads each image...
    re=cv2.resize(img,(400,400)) # resizes the image...
    cv2.imshow("Hey",re) # displays the image...
    cv2.waitKey(3000) # waits for the user input key...
    cv2.destroyAllWindows() # closes the window once the key is pressed...
    cv2.imwrite("resized_"+image,re) # writes the resized image with the file name "re" together with the "resized" prefix...

"""
NOTES:
As you can see, I first created a list containing the image file
paths and then iterated through that list.
The loop reads each image, resizes, displays, waits for the user input key,
closes the window once the key is pressed and then writes the resized image under
the existing file name together with the "resized" prefix.

"""
