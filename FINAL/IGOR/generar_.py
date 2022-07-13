import cv2
import os

import numpy as np

#datafo= 'C:\\Users\\HP\\Documents\\tkinter\\escuadra y compas\\data'
def generar():
    #datafo= 'C:\\Users\\Dark Wizard\\Documents\\Clases\\modelamiento de datos\\trabajao\\escuadra y compas\data\\victims'
    folder= os.path.dirname(__file__ )
    datafo= folder+ '\\data'
    
    lier=[]
    victims=[]

    con=0

    datali= os.listdir(datafo)

    
    for root in datali:
        print(root)
        square=datafo+'\\'+root
        print(square)
        for data in os.listdir(square):
            
            lier.append(con)
            #victims.append(cv2.imread(square+'\\'+data,0))
            #un maldito 0 >:v
            image= cv2.imread(square+'\\'+data,0)
            print(image)
            #image = cv2.resize(image, (150, 150)) 
            victims.append(image)
            cv2.imshow('uwu',image)

        con+=1

    print(datali)


    print('0', np.count_nonzero(np.array(lier)==0))
    print('1', np.count_nonzero(np.array(lier)==1))
    #print('2', np.count_nonzero(np.array(lier)==2))

    #specter= cv2.face.EigenFaceRecognizer_create()
    #specter= cv2.face.FisherFaceRecognizer_create()
    print('(-_-)zZzz')

    #specter.train(victims, np.array(lier))
    #specter.write(folder+'\\'+'I see I see Whit Little Evil Eye.xml')

    print(':) termino')

#specter.write(datafo+'\\'+'I see I see Whit Little Fish Eye.xml')