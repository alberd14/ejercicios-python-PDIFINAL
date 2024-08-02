import cv2
import matplotlib.pyplot as plt

# Cargar la imagen desde la ruta especificada
imagen = cv2.imread(r'C:\Users\ALBERD\Documents\Procesamiento-Final\venv\reategui.jpg')

# Verificar si la imagen se ha cargado correctamente
if imagen is None:
    print('No se pudo cargar la imagen')
else:
    print('Imagen cargada correctamente')

    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Configurar el tamaño de la figura para la visualización
    plt.figure(figsize=(10, 7))

    # Mostrar la imagen original
    plt.subplot(1, 2, 1) 
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))  # Convertir BGR a RGB para mostrar con matplotlib
    plt.title('Imagen original')  # Establecer el título para la imagen original
    plt.axis('off')  # Ocultar los ejes

    # Mostrar la imagen en escala de grises
    plt.subplot(1, 2, 2)  
    plt.imshow(imagen_gris, cmap='gray')  # Mostrar la imagen en escala de grises
    plt.title('Imagen en escala de grises')  # Establecer el título para la imagen en escala de grises
    plt.axis('off')  # Ocultar los ejes



    plt.tight_layout()
    plt.show()