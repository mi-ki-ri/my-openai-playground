import os
import openai
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("text", type=str, default="apple")
  args= parser.parse_args()
  TEXT = args.text

  print("テキスト:", TEXT)

  MY_PROMPT = f"""今から渡すテキストを4行の謎めいた文語体の自由詩に要約してほしい。
要約できたら、サマリー欄に書いてほしい。

テキスト: {TEXT}
サマリー: """

  openai.api_key = os.getenv("OPENAI_API_KEY")

  response = openai.Completion.create(model="text-davinci-003", prompt=MY_PROMPT, temperature=1, max_tokens=2048)

  # print(response)

  print("")

  for choice in response["choices"]:
      print("サマリー:", choice["text"])

main()