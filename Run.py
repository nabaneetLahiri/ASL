import cv2
import numpy as np
import tensorflow as tf
#from keras.models import load_model
from tensorflow.keras.models import load_model
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
model1 = load_model('keras.StationaryModel')
model2 = load_model('keras.MotionModel')
class Target:
    # master frame
    master = None
    trCount=1
    trCountPrev=0
    trCountCount=0
    trLimit=10
    @staticmethod
    def motionCount(imgCrop):
        frame0=imgCrop
        frame1 = cv2.cvtColor(frame0,cv2.COLOR_BGR2GRAY)
        # blur frame
        frame2 = cv2.GaussianBlur(frame1,(21,21),0)
        # initialize master
        if Target.master is None:
            Target.master = frame2
        # delta frame
        frame3 = cv2.absdiff(Target.master,frame2)
        # threshold frame
        frame4 = cv2.threshold(frame3,15,255,cv2.THRESH_BINARY)[1]
        # dilate the thresholded image to fill in holes
        kernel = np.ones((5,5),np.uint8)
        frame5 = cv2.dilate(frame4,kernel,iterations=4)
        # find contours on thresholded image
        #nada,contours,nada = cv2.findContours(frame5.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        contours,nada = cv2.findContours(frame5.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        # make coutour frame
        frame6 = frame0.copy()
        # target contours
        targets = []
        # loop over the contours
        for c in contours:
            # if the contour is too small, ignore it
            if cv2.contourArea(c) < 500:
                    continue
            # contour data
            M = cv2.moments(c)#;print( M )
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            x,y,w,h = cv2.boundingRect(c)
            rx = x+int(w/2)
            ry = y+int(h/2)
            ca = cv2.contourArea(c)
            # save target contours
            targets.append((rx,ry,ca))
        # make target
        area = sum([x[2] for x in targets])
        mx = 0
        my = 0
        if targets:
            for x,y,a in targets:
                mx += x
                my += y
            mx = int(round(mx/len(targets),0))
            my = int(round(my/len(targets),0))
        # plot target
        tr = 50
        frame7 = frame0.copy()
        if targets:
            Target.trCount=Target.trCount+1
        # update master
        Target.master = frame2

        if Target.trCountCount==Target.trLimit:
            Target.trCount=0
            Target.trCountPrev=None
            Target.trCountCount=0
        if Target.trCountPrev==Target.trCount:
            Target.trCountCount=Target.trCountCount+1
        else:
            Target.trCountCount=0
        Target.trCountPrev=Target.trCount
        return Target.trCount
def keras_process_image(img):
  img = cv2.resize(img, (224, 224))
  img = np.array(img, dtype=np.float32)
  img = np.reshape(img, (1, 224, 224, 3))
  return img

def keras_predict(model, image):
  processed = keras_process_image(image)
  pred_probab = model.predict(processed)[0]
  pred_class = list(pred_probab).index(max(pred_probab))
  return max(pred_probab), pred_class

def displaySigns():
    signs=cv2.imread("SIGNS.jpg",1)
    commandBoard = np.zeros((131, 688, 3), dtype=np.uint8)
    cv2.putText(commandBoard, "_"*50, (0, 1), cv2.FONT_HERSHEY_TRIPLEX, 0.75, (0, 255, 0))
    cv2.putText(commandBoard, "Press Escape : To close screen", (10, 20), cv2.FONT_HERSHEY_TRIPLEX, 0.75, (0, 255, 255))
    cv2.putText(commandBoard, "Press Delete : To clear screen", (10, 45), cv2.FONT_HERSHEY_TRIPLEX, 0.75, (0, 255, 255))
    cv2.putText(commandBoard, "Press Backspace : To clear last character", (10, 70), cv2.FONT_HERSHEY_TRIPLEX, 0.75, (0, 255, 255))
    cv2.putText(commandBoard, "Press Spacebar : To give space", (10, 95), cv2.FONT_HERSHEY_TRIPLEX, 0.75, (0, 255, 255))
    cv2.putText(commandBoard, "Press Enter : To speak", (10, 120), cv2.FONT_HERSHEY_TRIPLEX, 0.75, (0, 255, 255))
    cv2.putText(commandBoard, "_"*50, (0, 130), cv2.FONT_HERSHEY_TRIPLEX, 0.75, (0, 255, 0))
    signs=np.vstack((signs,commandBoard))
    cv2.imshow("Signs",signs)


def recognize():
  cam = cv2.VideoCapture(0)
  blackboard = np.zeros((40, 960, 3), dtype=np.uint8)
  x, y, w, h = 300, 100, 300, 300
  old_character='a'
  word = ""
  count_frame = 0
  count_motion = 0
  displaySigns()
  while True:
    img = cam.read()[1]
    img = cv2.flip(img, 1)
    imgCrop=np.zeros((300,300,3))
    imgCrop = img[y:y+h, x:x+w]
    imgCrop = cv2.flip(imgCrop, 1)

    count_motion=Target.motionCount(imgCrop)
    if count_motion<30:
        model=model1
        pred_probab, pred_class = keras_predict(model, imgCrop)
        if pred_class>8:
            pred_class=pred_class+1
        if pred_class==25:
            cv2.putText(img, "NON", (30, 200), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255, 0, 0))
        else:
            character= chr(pred_class+65)
            cv2.putText(img, character, (30, 200), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 255, 0))
            if old_character == character:
                count_frame += 1
            else:
                count_frame = 0
            if count_frame == 25:
                count_frame=0
                word = word + character
                cv2.putText(blackboard, word, (15, 35), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255, 255, 255))
            if len(word)>31:
                word=""
                blackboard = np.zeros((40, 960, 3), dtype=np.uint8)
            old_character=character
    else:
        model=model2
        pred_probab, pred_class = keras_predict(model, imgCrop)
        if pred_class==0:
            pred_class=9
        if pred_class==1:
            pred_class=25
        if pred_class==2:
            cv2.putText(img, "NON", (30, 200), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255, 0, 0))
        else:
            character= chr(pred_class+65)
            cv2.putText(img, character, (30, 200), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 255, 0))
            if old_character == character:
                count_frame += 1
            else:
                count_frame = 0
            if count_frame == 25:
                count_frame=0
                word = word + character
                cv2.putText(blackboard, word, (15, 35), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255, 255, 255))
            if len(word)>31:
                word=""
                blackboard = np.zeros((40, 960, 3), dtype=np.uint8)
            old_character=character

    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255))
    img = cv2.resize(img, (960, 720))
    img=np.vstack((img,blackboard))
    cv2.imshow("Video",img)
    k=cv2.waitKey(5) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        return
    elif k == 32:
        word=word+" "
        cv2.putText(blackboard, word, (15, 35), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255, 255, 255))
    elif k == 8:
        word=word[:-1]
        blackboard = np.zeros((40, 960, 3), dtype=np.uint8)
        cv2.putText(blackboard, word, (15, 35), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255, 255, 255))
    elif k == 0:
        if not word=="":
            blackboard = np.zeros((40, 960, 3), dtype=np.uint8)
        word=""
    elif k == 13:
        speak.Speak(word)
recognize()
