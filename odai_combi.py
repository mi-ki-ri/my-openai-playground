import os
import openai


def main():
 
  MY_PROMPT = f"""発想の補助にするため、ランダムな形容詞と名詞のセットが5つほどほしい。不釣り合いな(通常使われない)組み合わせほどなお良い。
キーワード例: 「柔らかい・時計」「赤い・無理数」「褪せた・大根」「穏やかな・恒星」「幾何学的な・死」
キーワード本番: """

  openai.api_key = os.getenv("OPENAI_API_KEY")

  response = openai.Completion.create(model="text-davinci-003", prompt=MY_PROMPT, temperature=0.80, max_tokens=1024)

  # print(response)

  print("")

  for choice in response["choices"]:
      print("キーワード",choice["text"])

main()