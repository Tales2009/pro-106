import cv2


# Crie nosso classificador de corpos
body_classifier
body_classifier = cv2.CascadeClassifier('haarscacade_fullbody.xml')

# Inicie a captura de vídeo para o arquivo de vídeo
cap = cv2.VideoCapture('walking.avi')

# Faça o loop assim que o vídeo for carregado com sucesso
while True:
    cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Leia o primeiro quadro
    ret, frame = cap.read()

    # Converta cada quadro em escala de cinza
    cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Passe o quadro para nosso classificador de corpos
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)

    
    # Extraia as caixas delimitadoras para quaisquer corpos identificados
    for (x,y,w,h) in bodies:
        cv2.rectangle(bodies,(x,y),(x+w,y+h),(255,0,0,)2)
        roi_color  =  bodies[y:y+h,x:x+w]
        cv2.imwrite("wlking.avi",roi_color)


    if cv2.waitKey(1) == 32: #32 é a barra de espaço
        break

cap.release()
cv2.destroyAllWindows()
