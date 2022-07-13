import cv2
import os

#import inutils
def capturar(code):
    #code= 'Faraon'
    #code= 'Jackson'
    #datafo= 'C:\\Users\\HP\\Documents\\tkinter\\escuadra y compas\\data\\Ricardo'
    datafo= os.path.dirname(__file__ )
    #datafo= datafo + code

    #zelda= "Wismichu.mp4"

    datafo= datafo+ '\\data\\' + code

    if not os.path.exists(datafo):
        os.makedirs(datafo)
    else:
        print('qchaw')

    eye= cv2.VideoCapture(0)

    #detectfile= 'C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalcatface.xml'
    detectfile= 'C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml'
    detetor= cv2.CascadeClassifier(detectfile)

    clock=0

    while True:
        
        ret, frame= eye.read()
        if ret== False: break
        
        gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.rectangle(frame, (50,50), (100, 100), (0,200,0),4)
        lifra=frame.copy()

        face= detetor.detectMultiScale(gray, 1.3, 5)
        for (x,y, w,h) in face:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,0),4)
            print('puagh ')
            littleEye= lifra[y:y+h, x:x+w]
            littleEye=cv2.resize(littleEye,(150,150), interpolation= cv2.INTER_CUBIC)

            grici= cv2.cvtColor(littleEye, cv2.COLOR_BGR2GRAY)
            cv2.imshow('uwu' ,grici)
            if clock <256:
                cv2.imwrite(datafo+ '\\rostro_{}.jpg'.format(clock), grici)
                pass
            
                clock+=1

        if clock ==255:
            break


        cv2.imshow('I see I see whit my litte evil eye', frame)

        if cv2.waitKey(1)== ord('q'): break

    cv2.destroyAllWindows()