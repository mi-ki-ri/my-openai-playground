import os
import openai
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--keyword", type=str, default="apple")
  args= parser.parse_args()
  KEYWORD = args.keyword

  my_prompt = f"""The following is a list of keyword to tagging needed.
please tagging keywords.
taggin format like,
banana: [
  fruit,
  yellow,
  yummy
]
guitar: [
  instrument,
  expensive, 
  loud
]
dog: [
  pet,
  loyal,
  furry
]
car: [
  vehicle,
  fast,
  expensive
]
{KEYWORD}: ["""

  openai.api_key = os.getenv("OPENAI_API_KEY")

  response = openai.Completion.create(model="text-davinci-003", prompt=my_prompt, temperature=0.33, max_tokens=1024)

  for choice in response["choices"]:
      print(my_prompt+choice["text"])

main()