import face_recognition as fr
import cv2
import os
from cadastro_facial import faces

faces
def facial_recognition():
    take_picture()
    foto_data = fr.load_image_file("./img/picture.jpeg")
    faces1 = fr.face_encodings(foto_data)
    if len(faces1) > 0:
        return True, faces1
    return False, []

def identify_face():
    face_test = facial_recognition()
    if face_test[0]:
        for known_face in faces:
            for datas in known_face[1]:
                match = fr.compare_faces([datas], face_test[1][0])
                if any(match):
                    
                    print("---------------------------------------------------\n\n")
                    print(f"Rosto identificado como  {known_face[0]}.\n\n")
                    return
        print("Rosto não identificado.")
        return 0
    else:
        print("Não há rostos na imagem.")

def take_picture():
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        picture, frame = cam.read()
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    if picture:
        if not os.path.exists("img"):
            os.makedirs("img")
        caminho_arquivo = os.path.join("img", "picture.jpeg")
        cv2.imwrite(caminho_arquivo, frame)
    else:
        print("Não foi possível capturar a imagem.")
        
identify_face()