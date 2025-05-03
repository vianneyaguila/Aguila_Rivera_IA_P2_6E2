import cv2

# Cargar el clasificador Haar para detección de rostros (incluido en OpenCV)
clasificador_rostro = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Cargar una imagen desde archivo
imagen = cv2.imread('imagen_objeto.jpg')
if imagen is None:
    raise FileNotFoundError("No se encontró la imagen. Asegúrate de tener 'imagen_objeto.jpg' en la carpeta del script.")

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar rostros
rostros = clasificador_rostro.detectM_
