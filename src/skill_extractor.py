def extract_skills(text):
    """
    Extract skills from resume text using keyword matching.
    """
    skills_list = [
        "python", "sql", "machine learning", "data analysis",
        "pandas", "numpy", "scikit-learn", "deep learning"
    ]
    
    found_skills = []

    text = text.lower()

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills


if __name__ == "__main__":
    from resume_parser import extract_text_from_pdf

    file_path = "data/sample_resume.pdf"
    text = extract_text_from_pdf(file_path)

    skills = extract_skills(text)

    print("Extracted Skills:", skills)