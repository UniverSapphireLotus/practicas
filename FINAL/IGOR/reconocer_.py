from asyncio.windows_events import NULL
import cv2
import os

import datetime

datafo= os.path.dirname(__file__ )
#datali= os.listdir(datafo)

marley=['ADMIN', 'CLARK', 'GWEN', 'JHON CHINA', 'Pipo', 'SPYDER']


specter= cv2.face.EigenFaceRecognizer_create()
specter.read(datafo+'\\'+'I see I see Whit Little Evil Eye.xml')

eye= cv2.VideoCapture(0)

detectfile= 'C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml'
#tower= 'C:\\opencv\\build\etc\\haarcascades\\haarcascade_eye_tree_eyeglasses.xml'
#smile= 'C:\\opencv\\build\etc\\haarcascades\\haarcascade_smile.xml'

#phone= 'C:\\opencv\\build\etc\\haarcascades\\Phone_Cascade.xml'
#detetor= cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
detetor= cv2.CascadeClassifier(detectfile)
###################################################################################

atroska = os.path.dirname(__file__ )

visa_allowed= atroska + '\\capturas\\'+ 'permitido'
visa_denied = atroska + '\\capturas\\'+ 'intrusos'

if not os.path.exists(visa_allowed):
    os.makedirs(visa_allowed)

if not os.path.exists(visa_denied):
    os.makedirs(visa_denied)

i_allowed = len(os.listdir(visa_allowed))
i_denied = len(os.listdir(visa_denied))

print("<<<owo>>> :| ", i_allowed, " ]_<[<n_n>]>_{ ", i_denied)

def reconocer(userID):
    #datafo= 'C:\\Users\\HP\\Documents\\tkinter\\escuadra y compas\\data'
    
    #dect_eyes= cv2.CascadeClassifier(tower)
    #dect_smile= cv2.CascadeClassifier(smile)
    #dect_phone= cv2.CascadeClassifier(phone)
    accc= 0
    lv_coincidencia=10

    visa= False

    for i in range(0,100):
        ret, frame= eye.read()
        if ret== False: break

        gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.rectangle(frame, (50,50), (100, 100), (0,200,0),4)
        lifra=gray.copy()

        face= detetor.detectMultiScale(gray, 1.3, 5)
        #sauron= dect_eyes.detectMultiScale(gray, 1.3, 5)
        #sadness= dect_smile.detectMultiScale(gray, 1.3, 5)

        #boomer= dect_phone.detectMultiScale(gray, 3, 9)

        result= -1

        for (x,y, w,h) in face:
            littleEye= lifra[y:y+h, x:x+w]
            littleEye=cv2.resize(littleEye,(150,150), interpolation= cv2.INTER_CUBIC)
            #image = cv2.resize(image, (150, 150)) 

            result= specter.predict(littleEye)
            print(result)
            if result[1]<5700:
                cv2.putText(frame,'{}'.format(marley[result[0]]), (x,y-5), 1,1.3,(255,0,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
                result= result[0]
                #cv2.imwrite(datafo+ '\\rostro_{}.jpg'.format(clock), grici)
                
            else:
                cv2.putText(frame,'No reconocido', (x,y-5), 1,1.3,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255),2)
                result= -1
            #cv2.putText(frame,'{}'.format(result), (x,y-5), 1,1.3,(255,255,0),1,cv2.LINE_AA)
            #cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)
            """for (ex,ey, ew,eh) in sauron:
                littleEye= lifra[ey:ey+eh, ex:ex+ew]
                cv2.rectangle(frame, (ex,ey), (ex+ew, ey+eh), (255,255,0),2)"""
            '''
            for (ex,ey, ew,eh) in sadness:
                w=x+w
                h=y+h
                if x<ex<w and y<ey<h:
                    littleEye= lifra[ey:ey+eh, ex:ex+ew]
                    cv2.rectangle(frame, (ex,ey), (ex+ew, ey+eh), (0,255,0),2)
        
            '''
        '''    
        for (ex,ey, ew,eh) in boomer:
                littleEye= lifra[ey:ey+eh, ex:ex+ew]
                cv2.putText(frame,'Celular', (ex,ey-5), 1,1.3,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (ex,ey), (ex+ew, ey+eh), (230,230,250),2)
        '''
        
        cv2.imshow('I see I see whit my litte evil eye', frame)
        
        if result == userID:
            print("DAR ACCESO")
            accc+=1
        
        if accc >=lv_coincidencia:
            print("<--(X_X)--x")
            visa= True
            break
        if cv2.waitKey(1)== ord('q'): break

    cv2.destroyAllWindows()
    return visa

def detectar():
    #datafo= 'C:\\Users\\HP\\Documents\\tkinter\\escuadra y compas\\data'
    
    #dect_eyes= cv2.CascadeClassifier(tower)
    #dect_smile= cv2.CascadeClassifier(smile)
    #dect_phone= cv2.CascadeClassifier(phone)

    #i_allowed = len(os.listdir(visa_allowed))
    #i_denied = len(os.listdir(visa_denied))
    while True:
        ret, frame= eye.read()
        if ret== False: break

        gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.rectangle(frame, (50,50), (100, 100), (0,200,0),4)
        lifra=gray.copy()

        face= detetor.detectMultiScale(gray, 1.3, 5)
        #sauron= dect_eyes.detectMultiScale(gray, 1.3, 5)
        #sadness= dect_smile.detectMultiScale(gray, 1.3, 5)

        #boomer= dect_phone.detectMultiScale(gray, 3, 9)

        result= NULL

        for (x,y, w,h) in face:
            littleEye= lifra[y:y+h, x:x+w]
            littleEye=cv2.resize(littleEye,(150,150), interpolation= cv2.INTER_CUBIC)
            #image = cv2.resize(image, (150, 150)) 

            result= specter.predict(littleEye)
            hora= datetime.datetime.now().strftime("%Y=%m=%d[owo]%H=%M=%S")
            if result[1]<5700:
                cv2.putText(frame,'{}'.format(marley[result[0]]), (x,y-5), 1,1.3,(255,0,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
                result= result[0]
                cv2.imwrite(visa_allowed+ '\\code_{}__hora_{}_.jpg'.format(result, hora), littleEye)

                
            else:
                cv2.putText(frame,'No reconocido', (x,y-5), 1,1.3,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255),2)
                cv2.imwrite(visa_denied+ '\\intruso__hora_{}_.jpg'.format(hora), littleEye)
                result= NULL

        cv2.imshow('I see I see whit my litte evil eye', frame)
        

        if cv2.waitKey(1)== ord('q'): break

    cv2.destroyAllWindows()


#reconocer(1)