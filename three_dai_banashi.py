import os
import openai


def main():
 
  MY_PROMPT = f"""三題噺という種類のストーリーを作るために、できるだけランダムなキーワードを3つ挙げてほしい。
キーワードの1つ目は人物、2つ目は品物、3つ目は場所が望ましい。
キーワード例: 「酔漢」「財布」「芝浜」
キーワード本番:"""

  openai.api_key = os.getenv("OPENAI_API_KEY")

  response = openai.Completion.create(model="text-davinci-003", prompt=MY_PROMPT, temperature=0.80, max_tokens=1024)

  # print(response)

  print("")

  for choice in response["choices"]:
      print("三題噺",choice["text"])

main()