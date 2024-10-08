from ultralytics import YOLO
import cv2
model = YOLO('yolov10n.pt')
import serial
#arduino = serial.Serial("COM4", 9600, timeout=1)


cap = cv2.VideoCapture(0)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))/3

left = frame_width
center = frame_width*2
right = frame_width*3
while True : 
    ret , frame = cap.read()
    results = model(frame)
    for result in results:
        boxes = result.boxes
        for box in boxes:
            if box.cls.item()==39:
                x1,y1,x2,y2 = map(int , box.xyxy[0])
                label = result.names[box.cls[0].item()]
                pos = (x1+x2)/2
                if pos <left :
                    cv2.putText(frame, 'Obstacle on left', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                    #arduino.write(b'l')
                if left < pos < center:
                    cv2.putText(frame, 'Obstacle on center', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                    #arduino.write(b'c')
                if pos > center :
                    cv2.putText(frame, 'Obstacle on Right', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                    #arduino.write(b'r')
                


                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                

    cv2.imshow('Yolov8',frame)
    if cv2.waitKey(1) & 0xFF ==27:
        break

cap.release()
cv2.destroyAllWindows()
