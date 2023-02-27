import openai
import helperBois as hb

config = hb.loadConfig()  # Load the config file
openai.api_key = config['openai_key']  # replace with your API key


def parse_NL(prompt):
    # Call OpenAI's GPT-3 model to generate text
    response = openai.Completion.create(
        engine="davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated text from the API response
    text = response.choices[0].text.strip()

    return text
