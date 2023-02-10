import os
import openai
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("text", type=str, default="apple")
  args= parser.parse_args()
  TEXT = args.text

  MY_PROMPT = f"""Convert text into emoji.

Back to the Future: 👨👴🚗🕒 
Batman: 🤵🦇 
Transformers: 🚗🤖 
Star Wars: ⭐️⚔
{TEXT}: """

  openai.api_key = os.getenv("OPENAI_API_KEY")

  response = openai.Completion.create(model="text-davinci-003", prompt=MY_PROMPT, temperature=1, max_tokens=2048)

  # print(response)

  print("")

  for choice in response["choices"]:
      print(TEXT, choice["text"])


main()