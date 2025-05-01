import cv2
import matplotlib.pyplot as plt

# Cargar imagen en escala de grises
imagen = cv2.imread('imagen_ejemplo.jpg', cv2.IMREAD_GRAYSCALE)

# Verifica que se cargó correctamente
if imagen is None:
    raise FileNotFoundError("La imagen no se encontró. Asegúrate de tener 'imagen_ejemplo.jpg'.")

# Aplicar filtro de media (blur promedio)
filtro_media = cv2.blur(imagen, (5, 5))

# Aplicar filtro de mediana (ideal para eliminar ruido tipo sal y pimienta)
filtro_mediana = cv2.medianBlur(imagen, 5)

# Aplicar filtro Gaussiano (suavizado con distribución normal)
filtro_gaussiano = cv2.GaussianBlur(imagen, (5, 5), 1)

# Mostrar resultados
titulos = ['Original', 'Filtro Media', 'Filtro Mediana', 'Filtro Gaussiano']
imagenes = [imagen, filtro_media, filtro_mediana, filtro_gaussiano]

plt.figure(figsize=(10, 4))
for i in range(4):
    plt.subplot(1, 4, i+1)
    plt.imshow(imagenes[i], cmap='gray')
    plt.title(titulos[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
