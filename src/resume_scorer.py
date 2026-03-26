def calculate_score(extracted_skills):
    """
    Calculate resume score based on matched skills.
    """
    required_skills = [
        "python", "sql", "machine learning", "data analysis",
        "pandas", "numpy", "scikit-learn", "deep learning"
    ]
    
    matched = 0

    for skill in required_skills:
        if skill in extracted_skills:
            matched += 1

    score = (matched / len(required_skills)) * 100

    return round(score, 2)


if __name__ == "__main__":
    from resume_parser import extract_text_from_pdf
    from skill_extractor import extract_skills

    file_path = "data/sample_resume.pdf"

    text = extract_text_from_pdf(file_path)
    skills = extract_skills(text)

    score = calculate_score(skills)

    print("Skills:", skills)
    print("Resume Score:", score)