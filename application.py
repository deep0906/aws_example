from flask import Flask, render_template, request, flash, redirect
import nltk
from nltk.tokenize import RegexpTokenizer,word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

import string

from nltk.util import pr

nltk.download('punkt')

application = Flask(__name__)
application.secret_key="ABCDEF"



@application.route('/', methods=["POST","GET"])
def start():
    return render_template('index.html')

@application.route('/5a', methods=["POST","GET"])
def searchFunc134():
  count=0
  text = request.form.get("text")
  filename = request.form.get("fileName")

  fileHandler1 = open("./%s.txt" % filename, "w")
  n = fileHandler1.write(text)
  fileHandler1.close()

  fileHandler = open("./%s.txt" % filename, "rt")
  data = fileHandler.read()
  data=data.lower()

  
  text_file = open("./%s.txt" % filename, "w")
  n = text_file.write(data)
  text_file.close()
  
  charcount=0
  fileHandler = open("./%s.txt" % filename, "rt")
  data1 = fileHandler.read()
  for word in data1.split():
    word=word.strip()
    count=count+1
    for char in word:
      charcount = charcount+1
  text_file.close()

  return render_template('totalwordscount.html',filename=filename,count=count,charcount=charcount)


@application.route('/5b', methods=["POST","GET"])
def searchFunc():
  text = request.form.get("text")
  filename=request.form.get("fileName")

  print(text)
  foundInDocs=[]
  indexOfWord=[]
  wordCount=0

  
  fileHandler = open("./%s.txt" % filename, "rt")
  data = fileHandler.read()
      

  for word in text.split():
    word=word.lower()
    for d in data.split():
      print(d)
      if word==d:
        wordCount=wordCount+1

  return render_template('search.html',wordCount=wordCount,searchkey=text,filename=filename)

@application.route('/6',methods=['GET','POST'])
def totalwordscount():
  filename=request.form.get("fileName")
  d = dict()
  fileHandler = open("./%s.txt" % filename, "rt")
  data = fileHandler.read()
  for word in data.split():
    if word in d:
      d[word] = d[word] + 1
    else:
      d[word] = 1 
  d = sorted(d.items())
  return render_template('sorted.html',d=d)

@application.route('/7', methods=["POST","GET"])
def searchFunc234():
  text = request.form.get("text")
  filename=request.form.get("fileName")

  print(text)
  list = text.split(',')
  
  wordCount=0
  fileHandler = open("./%s.txt" % filename, "rt")
  data = fileHandler.read()
  
  for word in list:
    word=word.lower()
    for d in data.split():
      if word==d:
        wordCount=wordCount+1
        data=data.replace(d,"")

  text_file = open("./%s.txt" % filename, "w")
  n = text_file.write(data)
  text_file.close()
  
  return render_template('remove.html',wordCount=wordCount,searchkey=text,filename=filename)




if __name__ == '__main__':
    
  application.run(port=5000, debug=True)