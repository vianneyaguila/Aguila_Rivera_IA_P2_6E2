import cv2
import numpy as np

# Cargar la imagen en escala de grises
imagen = cv2.imread('lineas.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar detección de bordes (Canny)
bordes = cv2.Canny(imagen, 50, 150)

# Usar la Transformada de Hough para detectar líneas
lineas = cv2.HoughLinesP(bordes, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=10)

# Cargar la imagen original a color para dibujar líneas sobre ella
imagen_color = cv2.imread('lineas.jpg')

# Dibujar las líneas detectadas
if lineas is not None:
    for linea in lineas:
        x1, y1, x2, y2 = linea[0]
        cv2.line(imagen_color, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Mostrar la imagen con líneas etiquetadas
cv2.imshow("Lineas detectadas", imagen_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
