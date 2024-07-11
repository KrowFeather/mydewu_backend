from flask import Flask, jsonify
from flask_cors import CORS
from pymysql import *
import random

app = Flask(__name__)
CORS(app)
conn = None
cursor = None
try:
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='dewudb')
    cursor = conn.cursor()
except Exception as e:
    print(e)


@app.route('/getRandomRecommend', methods=['GET'])
def getRandomRecommend():
    try:
        sql = "SELECT * FROM goods"
        cursor.execute(sql)
        result = cursor.fetchall()
        res = []
        for item in result:
            res.append({
                'id': item[0],
                'name': item[1],
                'picurl': item[2],
                'soldout': item[3],
                'price': item[4],
                'desc': item[5]
            })
        print(res)
        chosen = random.sample(res, 8)
        return jsonify(chosen)
    except Exception as e:
        print(e)


@app.route('/getAllShoes', methods=['GET'])
def getAllShoes():
    try:
        sql = "SELECT * FROM goods where type=\'shoe\'"
        cursor.execute(sql)
        result = cursor.fetchall()
        res = []
        for item in result:
            res.append({
                'id': item[0],
                'name': item[1],
                'picurl': item[2],
                'soldout': item[3],
                'price': item[4],
                'desc': item[5]
            })
        print(res)
        return jsonify(res)
    except Exception as e:
        print(e)


@app.route('/getAllClothes', methods=['GET'])
def getAllClothes():
    try:
        sql = "SELECT * FROM goods where type=\'cl\'"
        cursor.execute(sql)
        result = cursor.fetchall()
        res = []
        for item in result:
            res.append({
                'id': item[0],
                'name': item[1],
                'picurl': item[2],
                'soldout': item[3],
                'price': item[4],
                'desc': item[5]
            })
        print(res)
        return jsonify(res)
    except Exception as e:
        print(e)


@app.route('/getUserInfo/<userid>', methods=['GET'])
def getUserInfo(userid):
    try:
        sql = f"SELECT * FROM user where id={userid}"
        cursor.execute(sql)
        result = cursor.fetchall()
        res = []
        for item in result:
            res.append({
                'id': item[0],
                'name': item[1],
                'sig': item[2],
                'likes': item[3],
                'fans': item[4],
                'subscribe': item[5],
                'sprite': item[6]
            })
        print(res)
        return jsonify(res)
    except Exception as e:
        print(e)


@app.route('/getRandomBlogRecommend', methods=['GET'])
def getRandomBlogRecommend():
    try:
        sql = f"SELECT blogs.id,blogs.content,blogs.likes,blogs.pic,blogs.uid,user.sprite,user.username FROM blogs,user where blogs.uid = user.id"
        cursor.execute(sql)
        result = cursor.fetchall()
        res = []
        for item in result:
            res.append({
                'id': item[0],
                'content': item[1],
                'likes': item[2],
                'pic': item[3],
                'uid': item[4],
                'upic': item[5],
                'uname': item[6]
            })
        print(res)
        return jsonify(res)
    except Exception as e:
        print(e)


@app.route('/getSwiper', methods=['GET'])
def getSwiper():
    try:
        sql = f"SELECT * FROM swiper"
        cursor.execute(sql)
        result = cursor.fetchall()
        res = []
        for item in result:
            res.append({
                'id': item[0],
                'url': item[1],
            })
        print(res)
        return jsonify(res)
    except Exception as e:
        print(e)


@app.route('/getRandomUsers', methods=['GET'])
def getRandomUsers():
    try:
        sql = f"SELECT username,sprite FROM user"
        cursor.execute(sql)
        result = cursor.fetchall()
        res = []
        for item in result:
            res.append({
                'name': item[0],
                'url': item[1],
            })
        rr = random.sample(res, 4)
        print(rr)
        return jsonify(rr)
    except Exception as e:
        print(e)


@app.route('/getMerchandiseInfo/<id>', methods=['GET'])
def getMerchandiseInfo(id):
    try:
        sql = f"SELECT goods.id,name,mainpic,rating,brand,cost FROM goods,m_info where goods.id=m_info.id and goods.id={id}"
        cursor.execute(sql)
        result = cursor.fetchall()
        res = []
        for item in result:
            res.append({
                'id': item[0],
                'name': item[1],
                'picurl': item[2],
                'rating': item[3],
                'brand': item[4],
                'cost': item[5]
            })
        print(res)
        return jsonify(res)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run()
