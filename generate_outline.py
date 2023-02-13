import os
import openai
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("subject", type=str, default="apple")
  args= parser.parse_args()
  SUBJECT = args.subject

  MY_PROMPT = f"""Create an outline for an essay or story about {SUBJECT} as Markdown unordered List in Japanese:"""

  openai.api_key = os.getenv("OPENAI_API_KEY")

  response = openai.Completion.create(model="text-davinci-003", prompt=MY_PROMPT, temperature=1, max_tokens=2048)

  for choice in response["choices"]:
      print(choice["text"])


main()