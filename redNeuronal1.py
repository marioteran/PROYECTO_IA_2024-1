import cv2
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# Modelo de red neuronal simple para reconocimiento de personajes
model = keras.Sequential([
    layers.Flatten(input_shape=(64, 64, 3)),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(num_classes, activation='softmax')  # Ajusta num_classes según tu conjunto de datos
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Supongamos que tienes un conjunto de datos etiquetado en el formato X_train, y_train
# X_train es un conjunto de imágenes en formato numpy array (64x64x3)
# y_train es un conjunto de etiquetas one-hot encoded (puedes usar keras.utils.to_categorical)

# Entrenamiento del modelo (reemplaza esto con tus datos)
# model.fit(X_train, y_train, epochs=10, batch_size=32)

# Cargar el modelo entrenado
# model = keras.models.load_model('modelo_entrenado.h5')

# Función para reconocer personajes en una imagen
def recognize_character(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (64, 64))
    img = np.expand_dims(img, axis=0)  # Añade una dimensión para representar el lote (batch)

    # Preprocesamiento adicional si es necesario
    # img = ...

    prediction = model.predict(img)
    predicted_class = np.argmax(prediction)

    # Ajusta character_names según tus clases
    character_names = ["ElTigre", "Frida", "Granpapi"]
    return character_names[predicted_class]

# Procesar un video
video_path = "elTigre.mp4"
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Supongamos que obtienes el cuadro clave (keyframe) de cada segundo del video
    # Puedes ajustar este valor según tus necesidades
    frame_rate = int(cap.get(5))
    current_frame = int(cap.get(1))
    if current_frame % frame_rate == 0:
        # Guardar el cuadro clave como imagen PNG
        image_name = f"frame_{current_frame}.png"
        cv2.imwrite(image_name, frame)

        # Llamar a la función para reconocer personajes en la imagen
        recognized_character = recognize_character(image_name)
        print(f"Frame {current_frame}: Recognized character - {recognized_character}")

cv2.destroyAllWindows()
cap.release()
