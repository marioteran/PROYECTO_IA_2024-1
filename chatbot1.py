import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_input(input_text):
    # Tokenizar y eliminar stopwords
    stop_words = set(stopwords.words('spanish'))
    words = word_tokenize(input_text, language='spanish')
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    return filtered_words

def chatbot_response(input_text):
    input_text = preprocess_input(input_text)

    # Reglas del chatbot
    rules = {
        ('hola', 'hi', 'hey'): ['¡Hola! ¿En qué puedo ayudarte?', '¡Hola! ¿Cómo estás?', '¡Hey! ¿En qué puedo ayudarte?'],
        ('clima', 'temperatura', 'pronóstico'): ['Lo siento, no puedo proporcionar información sobre el clima en este momento.'],
        ('nombre', 'quién eres', 'tu nombre'): ['Soy solo un chatbot.', 'Puedes llamarme Marioneitor.'],
        ('cómo estás', 'cómo te encuentras'): ['Soy un programa de computadora, así que no tengo sentimientos, ¡pero gracias por preguntar!'],
        ('adiós', 'chau', 'nos vemos'): ['¡Adiós! ¡Que tengas un gran día!', '¡Hasta luego!', '¡Chau!'],
        ('gracias', 'gracias', 'aprecio'): ['¡De nada!', '¡No hay problema!', '¡En cualquier momento!'],
        ('ayuda', 'asistencia', 'soporte'): ['¿Cómo puedo ayudarte hoy?', 'Estoy aquí para ayudar. ¿En qué necesitas asistencia?'],
        ('broma', 'cuéntame una broma', 'gracioso'): ['¿Por qué los científicos no confían en los átomos? ¡Porque lo componen todo!', '¿Oíste hablar del matemático que le tiene miedo a los números negativos? ¡No se detendrá ante nada para evitarlos!'],
        ('edad', 'cuántos años tienes', 'cuánto tiempo llevas'): ['Soy un programa, así que no tengo una edad en el sentido tradicional.'],
        ('hora', 'hora actual', '¿qué hora es?'): ['Lo siento, no tengo la capacidad de proporcionar la hora actual.'],
        ('programación', 'código', 'python'): ['¡Me encanta hablar de programación! ¿Qué te gustaría saber o discutir específicamente?'],
        ('amor', 'enamorado', 'relación'): ['Soy solo un chatbot, así que no experimento emociones como el amor.'],
        ('música', 'canción favorita', 'música favorita'): ['No tengo preferencias personales, pero puedo recomendar algunos géneros de música populares si estás interesado.'],
        ('cómo puedes ayudarme', 'qué puedes hacer'): ['Puedo ayudarte con información, responder preguntas o simplemente charlar. ¿Cómo puedo ayudarte hoy?'],
        ('predeterminado',): ['No entendí eso. ¿Puedes reformularlo o hacer una pregunta diferente?']
    }

    # Buscar una respuesta basada en las reglas
    for keywords, responses in rules.items():
        if any(keyword in input_text for keyword in keywords):
            return random.choice(responses)

    # Si no coincide con ninguna regla, usar la regla predeterminada
    return random.choice(rules[('predeterminado',)])

# Bucle principal del chatbot
while True:
    user_input = input("Tú: ")
    if user_input.lower() in ['salir', 'adiós', 'chau']:
        print("Chatbot: ¡Adiós!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
