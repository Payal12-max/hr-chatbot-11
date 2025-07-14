'''import openai

def generate_questions(job_role):
    prompt = f"Generate 5 candidate screening questions for a {job_role} role."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an HR assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    questions = response['choices'][0]['message']['content'].split('\n')
    return [q.strip("- ").strip() for q in questions if q.strip()]'''



import cohere

co = cohere.Client("lefSWs11zMKsbaQZcwjRo5vOo9KMvICjXd0f0ecL")

def generate_questions(job_role):
    chat_response = co.chat(
        model='command-r-plus',  # or 'command-r'
        message=f"Generate 5 HR interview screening questions for the role of {job_role}."
    )
    
    lines = chat_response.text.strip().split('\n')
    return [q.strip("12345).•- ") for q in lines if q.strip()]
