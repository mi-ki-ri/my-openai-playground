import argparse
import os
import openai
import webbrowser
import urllib.parse

"""
Usage:

- in "~/.zshrc"
  - export OPENAI_API_KEY
  - alias "nsearch" "python {FULLPATH}.py"
"""

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("q", type=str, default="apple")
  args= parser.parse_args()
  Q = args.q

  MY_PROMPT = f"""Search Word欄を元に、質問者が知りたいことを推測し、検索エンジン(Google)に最適化された詳細なクエリを日本語で書いてほしい。
完成したらSearch Query欄を埋めてほしい。
Search Word: {Q}
Search Query: """

  openai.api_key = os.getenv("OPENAI_API_KEY")

  response = openai.Completion.create(model="text-davinci-003", prompt=MY_PROMPT, temperature=0.33, max_tokens=256)

  # print(response)

  print("")

  for choice in response["choices"]:
      print(f"Curated search word for {Q} is...\n", choice["text"])
      URL=  f"http://pasokatu.com/nsearch#gsc.tab=0&gsc.q={ urllib.parse.quote(choice['text'])}&gsc.sort="
      webbrowser.open(url=URL, new=2)

main()