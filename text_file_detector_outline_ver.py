from math import ceil, floor
import os
import openai
import argparse

"""消費が激しい"""

def how_many_slice(length):
  i = 1
  while (length / i) > 1024:
    i += 1
  return i

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("file_path", type=str, default="apple")
  args= parser.parse_args()
  FILE_PATH = args.file_path
  FILE_BODY = ""

  if os.path.exists(FILE_PATH):
    with open(FILE_PATH, mode="r") as f:
      FILE_BODY = f.read()

  BODY_LEN = len(FILE_BODY)

  now_len = 0
  slice_len = how_many_slice(BODY_LEN)

  answer_outline_text_list = [""]

  while now_len < BODY_LEN:
    print(f"{now_len} / {BODY_LEN}")
    now_len_tmp = now_len
    now_len += ceil(BODY_LEN / slice_len)

    SLICED_BODY = FILE_BODY[now_len_tmp:now_len]

    MY_PROMPT = f"""以下はあるファイルのファイル名と内容だが、これをごく短く要約し、アウトライン化してMarkdownのUnorderedListに直してほしい(ネスト可)。
できたら『リスト:』欄に書いてほしい。

ファイル名: {FILE_PATH}
内容: {answer_outline_text_list[(len(answer_outline_text_list) - 1)]}\n{SLICED_BODY}
リスト: """

    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(model="text-davinci-003", prompt=MY_PROMPT, temperature=0.5, max_tokens=768)

    for choice in response["choices"]:
        # print(choice["text"])
        
        answer_outline_text_list.append( choice["text"] )
  
  print(answer_outline_text_list[len(answer_outline_text_list) - 1])

main()