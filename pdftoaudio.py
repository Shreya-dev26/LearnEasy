import pyttsx3
from PyPDF2 import PdfReader

pdf_name = input("enter pdf name with .pdf extension: ")
pg_num = int(input("enter page number you want to extract: "))-1
reader = PdfReader(pdf_name)
page = reader.pages[pg_num]

text = page.extract_text()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Read the text aloud
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()
