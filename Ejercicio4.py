import cv2
import matplotlib.pyplot as plt

# Cargar la imagen desde la ruta especificada
imagen = cv2.imread(r'C:\Users\ALBERD\Documents\Procesamiento-Final\venv\reategui.jpg')

# Verificar si la imagen se ha cargado correctamente
if imagen is None:
    print('No se pudo cargar la imagen')
else:
    print('Imagen cargada correctamente')

    # Aplicar un filtro gaussiano con un kernel de 5x5
    imagen_suavizada = cv2.GaussianBlur(imagen, (5, 5), 0)

    # Configurar el tamaño de la figura para la visualización
    plt.figure(figsize=(12, 6))

    # Mostrar la imagen original
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))  # Convertir BGR a RGB para mostrar con matplotlib
    plt.title('Imagen original') 
    plt.axis('off')  # Ocultar los ejes

    # Mostrar la imagen suavizada
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(imagen_suavizada, cv2.COLOR_BGR2RGB))  # Convertir BGR a RGB para mostrar con matplotlib
    plt.title('Imagen suavizada')  
    plt.axis('off')  # Ocultar los ejes

    plt.tight_layout()
    plt.show()

    # Guardar la imagen suavizada en un nuevo archivo
    cv2.imwrite('imagen_suavizada.jpg', imagen_suavizada)
