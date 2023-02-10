import os
import openai
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("file_path", type=str, default="apple")
  args= parser.parse_args()
  FILE_PATH = args.file_path
  FILE_BODY = ""

  if os.path.exists(FILE_PATH):
    with open(FILE_PATH, mode="r") as f:
      FILE_BODY = f.read()
      SLICED_BODY = FILE_BODY[0:min(len(FILE_BODY), 2048)]

  MY_PROMPT = f"""以下はあるファイルのファイル名と内容だが、10才児に分かるように要約してみてほしい。
要約できたら、要約欄に書いてほしい。

ファイル名: {FILE_PATH}
内容: {SLICED_BODY}
要約: """

  openai.api_key = os.getenv("OPENAI_API_KEY")

  response = openai.Completion.create(model="text-davinci-003", prompt=MY_PROMPT, temperature=0.33, max_tokens=1024)

  for choice in response["choices"]:
      print(choice["text"])


main()