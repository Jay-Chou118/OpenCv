import cv2
import mediapipe as mp
import time

from mediapipe.python.solutions.pose import POSE_CONNECTIONS

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture('E:\VisualStudioCode_project\Python_project\OpenCv\PoseModules\Test.mp4')

pTime = 0

while True :
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = pose.process(imgRGB)
    print(results.pose_landmarks)

    if results.pose_landmarks:
         mpDraw.draw_landmarks(img,results.pose_landmarks,POSE_CONNECTIONS)

    
    cTime = time.time()
    fps = 1/(cTime -pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,
    (255,0,0), 3)

    
    cv2.imshow("Img",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

