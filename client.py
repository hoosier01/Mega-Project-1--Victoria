from openai import OpenAI
client = OpenAI(
    api_key="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",
)
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)