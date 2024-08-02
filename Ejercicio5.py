import cv2
import matplotlib.pyplot as plt

# Leer la imagen en color desde un archivo
imagen = cv2.imread(r'C:\Users\ALBERD\Documents\Procesamiento-Final\venv\reategui.jpg')

# Verificar si la imagen se ha cargado correctamente
if imagen is None:
    print('No se pudo cargar la imagen')
else:
    print('Imagen cargada correctamente')

    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar la ecualización del histograma
    imagen_ecualizada = cv2.equalizeHist(imagen_gris)

    # Configurar el tamaño de la figura para la visualización
    plt.figure(figsize=(12, 6))

    # Mostrar la imagen original en escala de grises
    plt.subplot(1, 2, 1)
    plt.imshow(imagen_gris, cmap='gray')  # Mostrar la imagen en escala de grises
    plt.title('Imagen en escala de grises')  # Establecer el título para la imagen en escala de grises
    plt.axis('off')  # Ocultar los ejes

    # Mostrar la imagen ecualizada
    plt.subplot(1, 2, 2)
    plt.imshow(imagen_ecualizada, cmap='gray')  # Mostrar la imagen ecualizada en escala de grises
    plt.title('Imagen ecualizada')  # Establecer el título para la imagen ecualizada
    plt.axis('off')  # Ocultar los ejes

    plt.tight_layout()
    plt.show()

    # Guardar la imagen ecualizada en un nuevo archivo
    cv2.imwrite('imagen_ecualizada.jpg', imagen_ecualizada)
