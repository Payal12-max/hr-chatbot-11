'''import openai

openai.api_key = "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"

def evaluate_answer(question, user_response):
    prompt = f"""
    HR Interview Bot: 
    Question: {question} 
    Candidate's Answer: {user_response}

    Provide:
    - A score from 1 to 10
    - A short explanation why you gave that score.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an HR expert who evaluates candidate answers."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    return response['choices'][0]['message']['content']'''



import cohere

co = cohere.Client("lefSWs11zMKsbaQZcwjRo5vOo9KMvICjXd0f0ecL")


def evaluate_answer(question, user_response):
    chat_response = co.chat(
        model='command-r-plus',  # or 'command-r'
        message=f"Evaluate this answer out of 10 with explanation.\n\nQuestion: {question}\nAnswer: {user_response}"
    )
    return chat_response.text.strip()

