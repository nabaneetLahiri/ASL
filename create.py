import cv2                #importing opencv module
import numpy as np		 #importing numpy module and abbreviating it as np
import os				# importing os module

path="C:\\Dataset\\"  	#change path where you want to save files
#cam=int(input("Enter Camera Index : ")) # defining a variable cam which takes an integer value , that value is the camera index or number corresponding to the camera which is to be used for video capturing
cam=0
cap=cv2.VideoCapture(cam)  # VideoCapture is used for opening camera and capturing video and it returns a video object which is stored in variable cap
#i=ord(input("Enter Character : "))	# 65 here references ASCII values
i=65
j=int(input("Enter Starting Index : "))     # variable which keeps count of snaps/pics taken
name=""
limit=int(input("Enter Ending Index : "))   # maximum number of snaps/pics to be taken

while(cap.isOpened()):  # cap.isOpened returns true if video capturing has been initialized already.
	img=cap.read()[1]   # frame is stored in variable img
	x=300
	y=100
	w=300
	h=300
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255))
	imgCrop=img[y:y+h,x:x+w] # stores cropped image of hand
	cv2.imshow('Video',img) #  display camera input in a window
	cv2.imshow('imgCrop',imgCrop) # display cropped image of hand in a window
	k = 0xFF & cv2.waitKey(10)  # waits 10ms to capture the image of hand

	if k == 27:                # 27 ASCII value corresponds to escape value which upon depressing breaks out of loop
		break

	if k == ord('s'):            #press s to save a pic
		directory=path+str(chr(i))+'\\'   # stores the path of the folder where  pics needs to be stored

		if not os.path.exists(directory):  # checks if path in directory exists or not
		    os.makedirs(directory)			# if it doesn't create the folder at the address stored in directory
		name=directory+str(chr(i))+"_"+str(j)+".jpg" # stores the name of the file/pic
		cv2.imwrite(name,imgCrop)							# cv2.imwrite saves the pic in the desired folder

		if(j<limit):									# checks the value of j
			j+=1
			print(j)

		else:										# if limit is reached then moving on to the next symbol
			j=0
			i+=1
			for _ in range(50):
				print(f'changing to {chr(i)}')

cap.release()
cv2.destroyAllWindows()
