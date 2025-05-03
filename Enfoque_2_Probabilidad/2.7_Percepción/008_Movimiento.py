import cv2

# Inicializar la cámara (0 = webcam)
camara = cv2.VideoCapture(0)

# Leer el primer cuadro y convertirlo a escala de grises
ret, cuadro_anterior = camara.read()
cuadro_anterior = cv2.cvtColor(cuadro_anterior, cv2.COLOR_BGR2GRAY)

while True:
    # Leer el siguiente cuadro
    ret, cuadro_actual = camara.read()
    if not ret:
        break

    # Convertir a escala de grises
    gris_actual = cv2.cvtColor(cuadro_actual, cv2.COLOR_BGR2GRAY)

    # Calcular la diferencia absoluta entre los cuadros
    diferencia = cv2.absdiff(cuadro_anterior, gris_actual)

    # Aplicar un umbral para detectar movimiento
    _, umbral = cv2.threshold(diferencia, 30, 255, cv2.THRESH_BINARY)

    # Mostrar el cuadro original con movimiento marcado
    cv2.imshow("Movimiento Detectado", umbral)

    # Actualizar el cuadro anterior
    cuadro_anterior = gris_actual

    # Presionar 'q' para salir
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar ventanas
camara.release()
cv2.destroyAllWindows()
