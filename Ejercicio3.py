import cv2

# Leer la imagen desde un archivo
imagen = cv2.imread(r'C:\Users\ALBERD\Documents\Procesamiento-Final\venv\reategui.jpg')

# Verificar si la imagen se cargó correctamente
if imagen is None:
    print('No se pudo cargar la imagen.')
else:
    print('Imagen cargada correctamente.')

    # Cambiar el tamaño de la imagen a 300x300 píxeles
    dimensiones = (300, 300)  # Definir las nuevas dimensiones en el formato (ancho, alto)
    imagen_redimensionada = cv2.resize(imagen, dimensiones)  # Redimensionar la imagen

    # Guardar la imagen redimensionada en un nuevo archivo
    cv2.imwrite('imagen_redimensionada.jpg', imagen_redimensionada)

    # Mostrar la imagen redimensionada
    cv2.imshow('Imagen Redimensionada', imagen_redimensionada)

    # Esperar a que se pulse una tecla para cerrar la ventana
    cv2.waitKey(0)

