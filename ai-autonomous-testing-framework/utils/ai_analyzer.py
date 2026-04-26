from openai import OpenAI
client = OpenAI()

def analyze_failure(error):

    prompt = f"""
    Explain this automation test failure and give root cause in simple terms:

    {error}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content