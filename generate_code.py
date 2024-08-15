from openai import OpenAI
import os

CURRENTDIR = os.getcwd()
INPUTFILE = os.path.join(CURRENTDIR, 'input', 'prompt.txt')
OUTPUTDIR = os.path.join(CURRENTDIR, 'output')
OUTPUTFILE = os.path.join(OUTPUTDIR, 'response')

# Set the API key
KEY = 'YourDoubleAPIKEY_forsafeinjectionprotection__mostlymental'
KEYSECONDLY = 'YourDoubleAPIKEY_forsafeinjectionprotection__mostlymental'

# load ./key and paste to KEYSECONDLY
with open('./key', 'r') as f:
  KEYSECONDLY = f.read()

# Use the second key as the API key for the example
os.environ["OPENAI_API_KEY"] = KEYSECONDLY

os.makedirs(OUTPUTDIR, exist_ok=True)

def generatin(subcontext):
  context = f"{subcontext}"

  # gets API Key from environment variable OPENAI_API_KEY
  client = OpenAI()

  # Non-streaming:
  print("----- standard request -----")
  completion = client.chat.completions.create(
      model="gpt-4",
      messages=[
          {
              "role": "user",
              "content": context
          },
      ],
  )
  print(completion.choices[0].message.content)
  return completion.choices[0].message.content

def init():
  count = 0
  
  # count files in the output directory
  for file in os.listdir(OUTPUTDIR):
    if file.endswith('.txt'):
      count += 1

  with open(INPUTFILE, 'r', encoding='utf-8') as f:
    contexted = f.read()


  data = generatin(contexted)

  with open(OUTPUTFILE + count + '.txt', 'w', encoding='utf-8') as f:
      f.write(data)

if __name__ == '__main__':
  init()