from flask import Flask, request, jsonify
import mysql.connector
import json

app = Flask(__name__)

# データベース接続設定
db_config = {
    "user": "your_username",
    "password": "your_password",
    "host": "localhost",
    "database": "my_app",
    "raise_on_warnings": True,
}


# データベース接続
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn


# データを取得するAPI
@app.route("/items", methods=["GET"])
def get_items():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(items)


# データを追加するAPI
@app.route("/items", methods=["POST"])
def add_item():
    new_item = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name) VALUES (%s)", (new_item["name"],))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_item), 201


# サーバーの起動
if __name__ == "__main__":
    app.run(debug=True)
