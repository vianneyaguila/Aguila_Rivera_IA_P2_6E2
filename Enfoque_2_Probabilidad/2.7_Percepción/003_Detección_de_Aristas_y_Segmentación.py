import cv2
import matplotlib.pyplot as plt

# Cargar imagen en escala de grises
imagen = cv2.imread('imagen_ejemplo.jpg', cv2.IMREAD_GRAYSCALE)

# Verificar si la imagen se cargó
if imagen is None:
    raise FileNotFoundError("La imagen no se encontró. Asegúrate de tener 'imagen_ejemplo.jpg'.")

# Aplicar suavizado Gaussiano para reducir ruido
imagen_suavizada = cv2.GaussianBlur(imagen, (5, 5), 1)

# Detección de aristas con el algoritmo de Canny
bordes = cv2.Canny(imagen_suavizada, 50, 150)

# Segmentación usando umbral fijo
_, segmentada = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)

# Mostrar los resultados
titulos = ['Original', 'Bordes (Canny)', 'Segmentación (Umbral)']
imagenes = [imagen, bordes, segmentada]

plt.figure(figsize=(10, 4))
for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(imagenes[i], cmap='gray')
    plt.title(titulos[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
