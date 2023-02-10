import os
import openai
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("text", type=str, default="apple")
  args= parser.parse_args()
  TEXT = args.text

  MY_PROMPT = f"""次のテキストはFacebookおよびインスタグラムに投稿する予定である。テキストにハッシュタグをつけたい。インスタグラムで使われていそうなハッシュタグをハッシュタグ欄に追記してほしい。
テキスト: {TEXT}
ハッシュタグ: """

  openai.api_key = os.getenv("OPENAI_API_KEY")

  response = openai.Completion.create(model="text-davinci-003", prompt=MY_PROMPT, temperature=0.8, max_tokens=64)

  # print(response)

  print("")

  for choice in response["choices"]:
      print( choice["text"])

main()