import pandas as pd
from PyPDF2 import PdfReader
import io

def load_csv_with_encoding(uploaded_file):
    content = uploaded_file.read()
    for encoding in ['utf-8', 'latin1', 'cp1252']:
        try:
            decoded = content.decode(encoding)
            return pd.read_csv(io.StringIO(decoded))
        except:
            continue
    raise UnicodeDecodeError("All decoding attempts failed.")

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    return "".join([page.extract_text() or "" for page in reader.pages])
