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

  MY_PROMPT = f"""日本語で答えるQ&Aボットがほしい。答えが不明な場合「不明」と答えてほしい。

  Q: 富士山の高さは？
  A: 3,776メートルです

  Q: 日本の人口は？
  A: 1.257億(2021年当時)

  Q: バナナの平方根は？
  A: 不明

  Q: ビートルズの代表的なアルバム
  A: "Abbey Road", "Rubber Soul", "White Album"

  Q: {TEXT}
  A: """

  openai.api_key = os.getenv("OPENAI_API_KEY")

  response = openai.Completion.create(model="text-davinci-003", prompt=MY_PROMPT, temperature=0.25, max_tokens=512)

  for choice in response["choices"]:
      print(choice["text"])

if __name__ == '__main__':
  main()