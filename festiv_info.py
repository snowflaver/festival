import requests
import json
from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

url = 'http://api.data.go.kr/openapi/tn_pubr_public_cltur_fstvl_api?serviceKey=UHJ3sDYi2evKsyac0dnwdliA7%2Fo0%2Bqv6CdI%2BFUfXvDySc29Lmayp1gdicJ%2FD7rcam%2Bc2MezDM9fWJH0V3QQexw%3D%3D&pageNo=0&numOfRows=100&type=json'
# params ={'serviceKey' : 'UHJ3sDYi2evKsyac0dnwdliA7/o0+qv6CdI+FUfXvDySc29Lmayp1gdicJ/D7rcam+c2MezDM9fWJH0V3QQexw==',
#          'pageNo' : '0', 'numOfRows' : '100', 'type' : 'json',
#          'fstvlNm' : '', 'opar' : '', 'fstvlStartDate' : '', 'fstvlEndDate' : '', 'fstvlCo' : '', 'mnnst' : '', 'auspcInstt' : '', 'suprtInstt' : '', 'phoneNumber' : '', 'homepageUrl' : '', 'relateInfo' : '', 'rdnmadr' : '', 'lnmadr' : '', 'latitude' : '', 'longitude' : '', 'referenceDate' : '', 'instt_code' : '' }

response = requests.get(url)
data=response.text

json_ob = json.loads(data)['response']['body']['items']


@app.route("/fstiv_info", methods=["GET"])
def fstiv_get():
    festiv_info = json_ob
    return jsonify({'result':festiv_info})
