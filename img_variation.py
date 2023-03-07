import os
import time
import openai
import argparse
import requests


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("text", type=str, default="apple")
  args= parser.parse_args()
  IMG = args.text

  response = openai.Image.create_variation(
  image=open(f"{IMG}", "rb"),
  n=5,
  size="1024x1024"
  )
  
  for res in response['data']:
    image_url = res['url']
    print (image_url)

    urlData = requests.get(image_url).content
    with open(f"./dist/{time.time()}.png" ,mode='wb') as f: # wb でバイト型を書き込める
      f.write(urlData)
    time.sleep(0.1)

main()