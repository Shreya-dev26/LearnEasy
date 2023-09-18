from PyPDF2 import PdfReader
import spacy

pdf_name = input("enter pdf name with .pdf extension: ")
pg_num = int(input("enter page number you want to extract: "))-1
reader = PdfReader(pdf_name)
page = reader.pages[pg_num]
text = page.extract_text()

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Input text
text2 = print(text)

# Process the text using spaCy
doc = nlp(text)

# Extract keywords using spaCy
keywords = [token.text for token in doc if not token.is_stop and token.is_alpha]

# Print the keywords
print(keywords)
