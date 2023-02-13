import os
import openai
import argparse

"""
Usage:

- in "~/.zshrc"
  - export OPENAI_API_KEY
  - alias "qa" "python {FULLPATH}.py"
"""

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("text", type=str, default="")
  args= parser.parse_args()
  TEXT = args.text

  MY_PROMPT = f"""I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer, in Japanese. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with "Unknown".

  Q: What is human life expectancy in the United States?
  A: Human life expectancy in the United States is 78 years.

  Q: Who was president of the United States in 1955?
  A: Dwight D. Eisenhower was president of the United States in 1955.

  Q: Which party did he belong to?
  A: He belonged to the Republican Party.

  Q: What is the square root of banana?
  A: Unknown

  Q: How does a telescope work?
  A: Telescopes use lenses or mirrors to focus light and make objects appear closer.

  Q: Where were the 1992 Olympics held?
  A: The 1992 Olympics were held in Barcelona, Spain.

  Q: How many squigs are in a bonk?
  A: Unknown

  Q: {TEXT}
  A: """

  openai.api_key = os.getenv("OPENAI_API_KEY")

  response = openai.Completion.create(model="text-davinci-003", prompt=MY_PROMPT, temperature=0.25, max_tokens=512)

  for choice in response["choices"]:
      print(choice["text"])

if __name__ == '__main__':
  main()