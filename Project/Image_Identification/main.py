import ClassificationModule as cfm
import cv2


cap = cv2.VideoCapture(0)
myClassifier = cfm.Classifier('E:\VisualStudioCode_project\Python_project\Machine\Image_Identification2\keras_model.h5','E:\VisualStudioCode_project\Python_project\Machine\Image_Identification2\labels.txt')


while True:
    _, img = cap.read()
    predictions, index = myClassifier.getPrediction(img)
    print(predictions)
    #cv2.namedWindow("Image",0)
    #cv2.resizeWindow("Image",640,640)
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
