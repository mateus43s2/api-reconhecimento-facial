import face_recognition as fr
import cv2
import os
import customtkinter

faces = []
def facial_recognition():
    take_picture()
    foto_data = fr.load_image_file("./img/picture.jpeg")
    faces1 = fr.face_encodings(foto_data)
    if len(faces1) > 0:
        return True, faces1
    return False, []


def new_face(nome):
    new_face = facial_recognition()
    if new_face[0]:
        new_face_data = [nome, new_face[1]]
        faces.append(new_face_data)

        print("---------------------------------------------------\n\n")
        print("Rosto do ", nome, "cadastrado com sucesso.\n\n")
    else:
        print("Rosto não cadastrado")


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
        return
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

def clique():
    new_face(nome.get())
    janela.destroy()
def destroy():
    janela.destroy()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")        
janela = customtkinter.CTk()
janela.geometry("500x300")

texto = customtkinter.CTkLabel(janela, text="Digite o nome da pessoa que deseja cadastrar: ")
texto.pack(padx=10,pady=10)
nome = customtkinter.CTkEntry(janela, placeholder_text="Seu nome")
botao = customtkinter.CTkButton(janela, text="Cadastrar", command=clique)
botao2 = customtkinter.CTkButton(janela, text="Cancelar", command=destroy)
nome.pack(padx=10,pady=10)
botao.pack(padx=10, pady=10)
botao2.pack(padx=10, pady=10)
janela.mainloop()