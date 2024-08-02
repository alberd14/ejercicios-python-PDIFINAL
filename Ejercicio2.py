import cv2
import matplotlib.pyplot as plt

imagen = cv2.imread(r'C:\Users\ALBERD\Documents\Procesamiento-Final\venv\reategui.jpg')

if imagen is None:
    print('No se pudo cargar la imagen')
else:
    print('Imagen cargada correctamente')

    bordes = cv2.Canny(imagen, 100, 200)

    plt.figure(figsize=(10, 7))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    plt.title('Imagen original')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(bordes, cmap='gray')
    plt.title('Imagen con bordes')
    plt.axis('off')

    plt.tight_layout()
    plt.show()