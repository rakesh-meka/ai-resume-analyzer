import PyPDF2

def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF resume.
    """
    text = ""
    
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            
            for page in reader.pages:
                text += page.extract_text()
                
    except Exception as e:
        print(f"Error reading file: {e}")
    
    return text


if __name__ == "__main__":
    file_path = "data/sample_resume.pdf"  
    extracted_text = extract_text_from_pdf(file_path)
    
    print(extracted_text)