import numpy as np
import face_recognition as fr
import cv2
from engine import get_rostos

# get rostos 
rostos_conhecidos, nomes_dos_rostos = get_rostos()

# webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Falha ao capturar imagem da webcam")
        break

    # Redimensiona o frame para 1/4 do tamanho para processamento mais rápido
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # opencv para rgb
    rgb_small_frame = small_frame[:, :, ::-1]

    localizacao_dos_rostos = fr.face_locations(rgb_small_frame)
    rosto_desconhecidos = fr.face_encodings(rgb_small_frame, localizacao_dos_rostos)

    for (top, right, bottom, left), rosto_desconhecido in zip(localizacao_dos_rostos, rosto_desconhecidos):
        resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
        print(resultados)

        face_distances = fr.face_distance(rostos_conhecidos, rosto_desconhecido)
        melhor_id = np.argmin(face_distances)

        if resultados[melhor_id]:
            nome = nomes_dos_rostos[melhor_id]
        else:
            nome = "Acesso Negado"

        # Converte as coordenadas do rosto para o tamanho original do frame
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        
    # resultado
    cv2.imshow('Video', frame)

    # sai 
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

video_capture.release()
cv2.destroyAllWindows()
