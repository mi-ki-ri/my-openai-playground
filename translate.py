import os
import openai
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("text", type=str, default="apple")
  args= parser.parse_args()
  TEXT = args.text

  MY_PROMPT = f"""次のテキストを理解できる限りの言語(5カ国語〜10カ国語)に翻訳してほしい。訳語には読み(発音)もつけてほしい。

例:
テキスト: 炎
1. 英語: Fire(ファイアー)
2. 中国語: 火()
3. ドイツ語: Feuer()
4. ポルトガル語: Fogo (フォゴ)
5. ラテン語: Ignis (イグニス)
6. ...

テキスト: {TEXT}
1. """

  openai.api_key = os.getenv("OPENAI_API_KEY")

  response = openai.Completion.create(model="text-davinci-003", prompt=MY_PROMPT, temperature=0.8, max_tokens=512)

  # print(response)

  # print("")

  for choice in response["choices"]:
      print( f"1. {choice['text']}")

main()