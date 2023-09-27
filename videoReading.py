import cv2

# webcam
"""
cap = cv2.VideoCapture(0) #webcam'den görüntüyü alır
while True:
    ret, frame = cap.read()

    if ret == 0:# frame'ler yanlış okunursa döngüyü kırması için kod bloğu
    
        break


    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release() #dosyayı kapatmak için
cv2.destroyAllWindows()
"""
# video dosyası
cap = cv2.VideoCapture("antalya.mp4")

while True:
    ret, frame = cap.read()

    if ret == 0:# frame'ler yanlış okunursa döngüyü kırması için kod bloğu
    
        break

    # webcam
    # frame = cv2.flip(frame, 1)

    cv2.imshow("Antalya", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release() #dosyayı kapatmak için
cv2.destroyAllWindows()
