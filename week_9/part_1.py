from ollama import chat
from ollama import ChatResponse

# Basic chat test
response: ChatResponse = chat(model='smollm2:1.7b', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])

# Print the response
print(response.message.content)