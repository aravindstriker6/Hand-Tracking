import cv2
import mediapipe as mp
import time
cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
mpDraw=mp.solutions.drawing_utils
hands=mpHands.Hands()
ptime=0
ctime=0
while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLTS in results.multi_hand_landmarks:
            for id,lm in enumerate(handLTS.landmark):
             #print(handLTS.landmark)
             l,w,h=img.shape
             cx,cy=int(l*lm.x),int(w*lm.y)
             print(id,cx,cy)
             if id==4:
                 cv2.circle(img,(cx,cy),5,(255,0,255),15,cv2.FILLED)
            mpDraw.draw_landmarks(img,handLTS,mpHands.HAND_CONNECTIONS)
    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img,str("FPS: ")+str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255))
    cv2.imshow("Img",img)
    cv2.waitKey((1))
