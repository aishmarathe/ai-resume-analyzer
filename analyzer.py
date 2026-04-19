def analyze_resume(resume_text, job_description):

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    important_skills = [
        "python", "java", "c++", "c", "sql", "mysql", "mongodb",
        "html", "css", "javascript", "react", "node.js", "angular",
        "power bi", "tableau", "excel", "sas", "r", "matlab",
        "machine learning", "deep learning", "data analysis",
        "data science", "artificial intelligence", "nlp",
        "computer vision", "tensorflow", "pytorch", "scikit-learn",
        "pandas", "numpy", "matplotlib", "seaborn",
        "aws", "azure", "gcp", "databricks",
        "git", "github", "docker", "kubernetes",
        "communication", "teamwork", "leadership",
        "problem solving", "critical thinking",
        "linux", "operating systems", "dbms",
        "oop", "oops", "networking", "cybersecurity"
    ]

    missing_skills = []

    for skill in important_skills:
        if skill in job_description and skill not in resume_text:
            missing_skills.append(skill)

    score = 100 - (len(missing_skills) * 5)

    if score < 0:
        score = 0

    result = f"Resume Score: {score}/100\n\n"

    result += "Missing Skills:\n"

    if len(missing_skills) == 0:
        result += "- None\n"
    else:
        for skill in missing_skills:
            result += f"- {skill.title()}\n"

    result += "\nKeywords to Add:\n"

    if len(missing_skills) == 0:
        result += "- No additional keywords needed\n"
    else:
        for skill in missing_skills:
            result += f"- {skill.title()}\n"

    result += "\nSuggested Improvements:\n"

    if len(missing_skills) == 0:
        result += "- Your resume matches the job description well\n"
        result += "- Add more measurable achievements and project outcomes\n"
    else:
        for skill in missing_skills:
            result += f"- Add {skill.title()} if you have knowledge or experience in it\n"

    result += "- Add more measurable achievements in projects and internship\n"
    result += "- Add GitHub project links in the resume\n"
    result += "- Mention dashboards, SQL optimization, Databricks work, and project results more clearly\n"

    return result