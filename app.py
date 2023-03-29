from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.rjfe2ox.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

@app.route('/')
def home():
    return render_template('detail.html')

@app.route("/movie", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    star_receive=request.form['star_give']


    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive,headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    ogtitle = soup.select_one('meta[property="og:title"]')['content']
    ogdesc = soup.select_one('meta[property="og:description"]')['content']
    ogimage = soup.select_one('meta[property="og:image"]')['content']

    doc={
        'title':ogtitle,
        'desc':ogdesc,
        'image':ogimage,
        'star':star_receive
    }

    db.movies.insert_one(doc)
    
    return jsonify({'msg':'저장완료!'})

@app.route("/movie", methods=["GET"])
def movie_get():

    all_movies = list(db.movies.find({},{'_id':False}))
    return jsonify({'result':all_movies})

@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc={
        'name':name_receive,
        'comment':comment_receive
    }
    db.fan.insert_one(doc)
    
    return jsonify({'msg': '저장완료!'})

@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    all_comments = list(db.fan.find({},{'_id':False}))
    return jsonify({'result':all_comments})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)