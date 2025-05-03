import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import local_binary_pattern

# Cargar imagen en escala de grises
imagen = cv2.imread('imagen_ejemplo.jpg', cv2.IMREAD_GRAYSCALE)

# Verificar si la imagen se cargó correctamente
if imagen is None:
    raise FileNotFoundError("La imagen no se encontró. Asegúrate de tener 'imagen_ejemplo.jpg'.")

# ---------- TEXTURA: Cálculo del patrón binario local (LBP) ----------
radio = 1  # distancia del píxel central a los vecinos
puntos = 8 * radio  # número de vecinos
lbp = local_binary_pattern(imagen, puntos, radio, method='uniform')

# ---------- SOMBRAS: Detección con umbral adaptativo ----------
sombra = cv2.adaptiveThreshold(imagen, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY_INV, 11, 2)

# ---------- Mostrar resultados ----------
titulos = ['Original', 'Textura (LBP)', 'Sombras Detectadas']
imagenes = [imagen, lbp, sombra]

plt.figure(figsize=(12, 4))
for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(imagenes[i], cmap='gray')
    plt.title(titulos[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
