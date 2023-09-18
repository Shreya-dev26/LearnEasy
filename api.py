from flask import Flask, request, jsonify
import PyPDF2
from PyPDF2 import PdfReader

sneha = Flask(__name__)

@sneha.route('/uploadpdf')
def hi():

    # pdf_name = request.args.get('pdf_name')
    # pg_num = request.args.get('pg_num')
    pdf_name = request.form['pdf_name']
    pg_num = request.form['pg_num']

    print(pdf_name)
    print(pg_num)

    reader = PdfReader(pdf_name)
    page = reader.pages[int(pg_num)]

    text = page.extract_text()
    #print(text)
    return text


if _name_ == "__main__":
    sneha.run(debug=True)
