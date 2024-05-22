import face_recognition as fr

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos
    
    return False, []

def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    maria1 = reconhece_face("./img/maria1.jpg")
    if(maria1[0]):
        rostos_conhecidos.append(maria1[1][0])
        nomes_dos_rostos.append("Maria")

    mariana1 = reconhece_face("./img/mariana1.jpg")
    if(mariana1[0]):
        rostos_conhecidos.append(mariana1[1][0])
        nomes_dos_rostos.append("Mariana")
    
    return rostos_conhecidos, nomes_dos_rostos