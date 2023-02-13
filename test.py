import requests
import openai

endpoint = "https://api.openai.com/v1/engines/text-davinci-003/jobs"

#take the first line of the file api_key.txt and return it
def get_api_key():
    with open("api_key.txt", "r") as f:
        return f.readline()

openai.api_key = get_api_key()
api_key=get_api_key()

# The prompt to start the conversation with
prompt = "Hello, I'm a chatbot. How can I help you today?"

# The parameters for your job
params = {
  "prompt": prompt,
  "max_tokens": 100,
  "temperature": 0.5,
  "top_p": 1,
  "frequency_penalty": 0,
  "presence_penalty": 0
}

# Function to send a message to the API
def send_message(prompt):
  response = requests.post(
    endpoint,
    headers={
      "Content-Type": "application/json",
      "Authorization": f"Bearer {api_key}"
    },
    json={
      "prompt": prompt,
      "max_tokens": 100,
      "temperature": 0.5,
      "top_p": 1,
      "frequency_penalty": 0,
      "presence_penalty": 0
    }
  )

  if response.status_code == 200:
    return response.json()["choices"][0]["text"]
  else:
    return f"Request failed with status code {response.status_code}: {response.text}"

# Function to handle user input and send a response
def handle_input(input):
  response = send_message(input)
  print(f"Bot: {response}")

# Start the conversation
print("Bot: Hello, I'm a chatbot. How can I help you today?")

while True:
  user_input = input("You: ")
  if user_input == "exit":
    break
  handle_input(user_input)
