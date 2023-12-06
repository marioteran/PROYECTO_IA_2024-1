import cv2
import numpy as np

# Cargar el modelo YOLOv3 preentrenado
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Cargar las clases (etiquetas) utilizadas por YOLOv3
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Configurar los parámetros del modelo
layer_names = net.getUnconnectedOutLayersNames()
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Función para reconocer placas en un fotograma
def recognize_license_plate(frame):
    height, width, _ = frame.shape

    # Convertir la imagen a un blob para YOLO
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)

    # Obtener las detecciones
    outs = net.forward(layer_names)

    # Procesar las detecciones
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5 and classes[class_id] == 'car':
                # Obtener las coordenadas de la caja del objeto
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Coordenadas de la esquina superior izquierda
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                # Dibujar un rectángulo alrededor del objeto
                cv2.rectangle(frame, (x, y), (x + w, y + h), colors[class_id], 2)

    return frame

# Procesar un video
cap = cv2.VideoCapture("ruta/a/tu/video.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Llamar a la función para reconocer placas
    frame_with_license_plate = recognize_license_plate(frame)

    # Mostrar el video
    cv2.imshow("License Plate Recognition", frame_with_license_plate)

    # Salir al presionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
