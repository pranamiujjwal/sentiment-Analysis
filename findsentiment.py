#!/usr/bin/python3

def FormatString(string):
  import re
  string=re.sub(r'[^\w\s]', '', string)
  formatted_string=''
  useless=['i', 'im', 'my', 'he', 'she', 'it', 'was', 'is', 'am', 'are']
  for word in string.split():
    if word.lower()  not in useless:
      formatted_string=formatted_string + ' ' + word
  return formatted_string


def find_sentiment(string):
  #print(string)
  string=FormatString(string)
  from textblob import TextBlob
  textblob_obj=TextBlob(string)
  return textblob_obj.sentiment.polarity


def analysis(sentiment, score):
  if sentiment>0:
    print("Positive, with score:{} %".format(score))
  elif sentiment<0:
    print("Negative, with score:{} %".format(score))
  else:
    print("Neutral, with score:{} %".format(score))


def FromTextFile(filename):
  sentiments=[]
  elements=0
  with open(filename, "r") as file:
    for line in file.readlines():
      sentences=line.split(".")
      for string in sentences:
        if (string!='\n') or (string!=''):
          sentiments.append(find_sentiment(string))
          elements+=1
    file.close()
  return sentiments, elements


if __name__=="__main__":
  sentiment, score=FromTextFile("my.txt")  
  analysis(sum(sentiment), int((sum(sentiment)/len(sentiment))*100))
  #analysis(sentiment)
  