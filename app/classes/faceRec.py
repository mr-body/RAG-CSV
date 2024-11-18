import face_recognition

imagem_conhecida = face_recognition.load_image_file("1.jpg")
encoding_conhecido = face_recognition.face_encodings(imagem_conhecida)[0]

foto = "gildo.jpg"
imagem_teste = face_recognition.load_image_file(foto)
encodings_teste = face_recognition.face_encodings(imagem_teste)[0]

resultados = face_recognition.compare_faces([encoding_conhecido], encodings_teste, tolerance=0.4)

if resultados[0]:
    print("Acesso concedido!")
else:
    print("Acesso negado!")
