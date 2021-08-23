import cv2
import numpy as np
from  pyzbar.pyzbar import decode


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open('E:/VisualStudioCode_project/Python_project/OpenCv/QRBarCodeTurotial/text.txt') as f : #txt文件所在
    myDataList = f.read().splitlines()
    #print(myDataList)

while True:
    success,img = cap.read()

    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')

        print("barcode = " ,barcode)

        if myData in myDataList:
            myOutput = "Authorized"
            myColor = (0,0,255)
            #print('Authorized')
        else:
            myOutput = "Un-Authorized"
            myColor = (255,0,255)
            #print("Un-Authorized")
        print("myData = ",myData)
        pts = np.array([barcode.polygon],np.int32)
        print("pts = ",pts)
        pts = pts.reshape((-1,1,2))
        print("pts = ",pts)
        cv2.polylines(img,[pts],True,(255,0,255),4)  #多边形绘制
        pts2 = barcode.rect
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,myColor,2)



    cv2.imshow("Img",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
