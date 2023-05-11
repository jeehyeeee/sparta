import certifi
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
ca = certifi.where()
client = MongoClient(
    'mongodb+srv://sparta:test@cluster0.ghgs9cw.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)

db = client.dbsparta


@app.route('/')
def home():
    return render_template('modal.html')


@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.comment.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})


@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    all_comments = list(db.comment.find({}, {'_id': False}))
    return jsonify({'result': all_comments})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
