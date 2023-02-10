import os
import openai
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("say", type=str, default="apple")
  args= parser.parse_args()
  WORDS = args.say

  print(WORDS)

  MY_PROMPT = f"""アイデアを出すために、適当に返事してくれる話し相手がほしい。適当に会話を続けてほしい。
以下は会話の例。

質問者: こんにちは、回答者さん。
回答者: こんにちは。
質問者: 聞いてほしいアイデアがあるんだけど。
回答者: そう、アイデアがあるんだ。
質問者: {WORDS}
回答者: """

  openai.api_key = os.getenv("OPENAI_API_KEY")

  response = openai.Completion.create(model="text-davinci-003", prompt=MY_PROMPT, temperature=0.25, max_tokens=1024)

  # print(response)

  for choice in response["choices"]:
      print(choice["text"])

main()