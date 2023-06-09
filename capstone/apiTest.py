import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)