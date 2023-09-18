import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture
# from a microphone or an audio file
# You can change the source to sr.AudioFile("audio.wav") if you have an audio file
with sr.Microphone() as source:
    print("Please speak something...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for noise levels
    audio = recognizer.listen(source)

# Recognize the speech using Google Web Speech API
try:
    text = recognizer.recognize_google(audio)
    print("You said: ", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"Request to Google Web Speech API failed: {e}")
