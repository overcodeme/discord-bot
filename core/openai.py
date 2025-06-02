import openai
from data.settings import OPENAI_KEY


openai_client = openai.OpenAI(OPENAI_KEY)

async def get_openai_response(system_prompt, prompt=None, replying_message=None):
    response = openai_client.completions.create(
        model='gpt-4o',
        messages = [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': replying_message if replying_message else prompt}
        ]
    )

    return response['choices'][0]['message']['content'].strip()