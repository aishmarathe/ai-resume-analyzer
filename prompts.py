def create_prompt(resume_text, job_description):
    prompt = f"""
You are a smart HR recruiter.

Look at the resume and the job description.

Then give:

1. Resume Score out of 100
2. Missing Skills
3. Keywords to Add
4. Suggestions to Improve the Resume

Write the answer exactly like this:

Resume Score: __/100

Missing Skills:
- skill 1
- skill 2
- skill 3

Keywords to Add:
- keyword 1
- keyword 2
- keyword 3

Suggested Improvements:
- improvement 1
- improvement 2
- improvement 3

Resume:
{resume_text}

Job Description:
{job_description}
"""
    return prompt