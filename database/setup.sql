-- データベースの作成
CREATE DATABASE IF NOT EXISTS myapp;

-- myapp データベースを使用
USE myapp;

-- users テーブルの作成
CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(50) PRIMARY KEY,
    password VARCHAR(255) NOT NULL
);

-- サンプルデータの挿入
INSERT INTO users (user_id, password) VALUES ('user1', 'password1');
INSERT INTO users (user_id, password) VALUES ('user2', 'password2');
