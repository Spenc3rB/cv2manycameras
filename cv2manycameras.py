import cv2

cvCapIDs = []

for i in range(100):
    try:
        cap = cv2.VideoCapture(i)
        if cap is not None and cap.isOpened():
            cvCapIDs.append(i)
        
    except:
        pass
        
print(str(cvCapIDs))
