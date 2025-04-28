# Importamos la librería de reconocimiento de voz
import speech_recognition as sr

# Crear un objeto reconocedor
reconocedor = sr.Recognizer()

# Usamos el micrófono como fuente de entrada
with sr.Microphone() as source:
    print("Por favor, habla ahora...")

    # Ajustamos el nivel de energía ambiental para reducir ruido de fondo
    reconocedor.adjust_for_ambient_noise(source)

    # Escuchamos lo que el usuario diga
    audio = reconocedor.listen(source)

    try:
        # Intentamos reconocer el audio usando el motor de Google
        texto = reconocedor.recognize_google(audio, language="es-ES")

        # Mostramos el texto reconocido
        print("Has dicho: " + texto)

    except sr.UnknownValueError:
        # Si no se entendió el audio
        print("No entendí lo que dijiste.")
        
    except sr.RequestError as e:
        # Si hubo un error al conectarse al servicio
        print("Error al conectar con el servicio de reconocimiento de voz; {0}".format(e))
