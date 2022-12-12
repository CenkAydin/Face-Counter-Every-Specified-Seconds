import time
import cv2
import dlib
import threading

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = dlib.get_frontal_face_detector()
yuz_sayisi = 0
saniye = 0
sayac = 0
yok_olmaz_saniye = 0
eski_yuz_sayisi = -1
def yuz_tanima():
    global sayac
    global saniye
    global eski_yuz_sayisi
    while True:
        sayac = 0
        global yuz_sayisi
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        i = 0

        for face in faces:
            x, y = face.left(), face.top()
            x1, y1 = face.right(), face.bottom()
            cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
            i = i + 1
            sayac = sayac +1
            #cv2.putText(frame,
            #            'face num' + str(i), (x - 10, y - 10),
            #            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255),
            #            2)

            #print(face, i)
        cv2.rectangle(frame, (0, 0), (1280, 50), (0, 0, 0), -1)
        cv2.putText(frame,
                   'FACE COUNTER :  ' + str(yuz_sayisi), (350, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0),
                    2)

            #sayac = 0
        cv2.imshow('frame', frame)
        if (saniye == 5 and eski_yuz_sayisi != yuz_sayisi):
            eski_yuz_sayisi = yuz_sayisi
            yuz_sayisi = yuz_sayisi + sayac
            
            saniye = 0
            sayac = 0
            if eski_yuz_sayisi < yuz_sayisi:
                return_value, image = cap.read()
                cv2.imwrite('opencv' + str(yok_olmaz_saniye) + '.png', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def saniye_sayac():
    global saniye
    global yok_olmaz_saniye
    while True:
        time.sleep(1)
        saniye = saniye + 1
        yok_olmaz_saniye = yok_olmaz_saniye + 1

t1 = threading.Thread(target=yuz_tanima)
t2 = threading.Thread(target=saniye_sayac)
t1.start()
t2.start()
t1.join()
t2.join()















