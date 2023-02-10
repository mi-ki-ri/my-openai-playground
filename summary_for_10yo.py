import os
import openai
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("text", type=str, default="apple")
  args= parser.parse_args()
  TEXT = args.text

  print("テキスト:", TEXT)

  MY_PROMPT = f"""今から渡すテキストを10歳児にでも分かるように要約してほしい。日本語で、かつ丁寧語でお願いしたい。
要約できたら、サマリー欄に書いてほしい。

テキスト: {TEXT}
サマリー: """

  openai.api_key = os.getenv("OPENAI_API_KEY")

  response = openai.Completion.create(model="text-davinci-003", prompt=MY_PROMPT, temperature=0.66, max_tokens=1024)

  # print(response)

  print("")

  for choice in response["choices"]:
      print("サマリー:", choice["text"])

main()