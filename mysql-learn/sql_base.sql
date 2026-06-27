/*
  DDL之数据库操作：database
*/
#创建数据库`bj260528_1`
CREATE DATABASE `bj260528_1`;
#查找数据库
SHOW DATABASES;
#删除数据库`bj260528_1`
DROP DATABASE `bj260528_1`;
#创建数据库 `test01`
CREATE DATABASE `test01`;
#使用数据库`test01`
USE `test01`;

/*
  DDL之表操作->table
*/
#创建表user
CREATE TABLE `user`(
  pid INT,
  username VARCHAR(20),
  password int(18)
);
#查看表结构user
DESC `user`;
#查看所有表
SHOW TABLES;
#删除表user
DROP TABLE `user`;
#修改字段类型
ALTER TABLE `user` MODIFY password VARCHAR(20);

/*
  DML之数据操作语言
*/
#插入数据方式1
INSERT INTO `user` (pid,username,password) VALUES (1,'wudalang','123456');
#插入数据方式2
INSERT INTO `user` (pid,username,password) VALUES (2,'zhangsan','zhangsan'),(3,'wangwu','88888888');
#插入数据方式3
INSERT INTO `user` VALUES (4,'tianbi','a1234');
#一次性将所有数据都删除
DELETE FROM `user`;
#根据条件删除数据
DELETE FROM `user` WHERE pid = 4;
#修改数据
UPDATE `user` SET password = '666666' WHERE username = 'tianbi';

/*
  约束
*/
#主键约束方式1
CREATE TABLE `category`(
  cid INT PRIMARY KEY,
  cname VARCHAR(10)
);
DROP TABLE `category`;
#主键约束方式2
CREATE TABLE category(
  cid INT,
  cname VARCHAR(10),
  PRIMARY KEY(cid)
);
DROP TABLE `category`;
#主键约束方式3
CREATE TABLE `category`(
  cid INT,
  cname VARCHAR(10)
);
ALTER TABLE `category` ADD PRIMARY KEY(cid);
#删除主键
ALTER TABLE `category` DROP PRIMARY KEY;
DROP TABLE `category`;
#自增长约束
CREATE TABLE `category`(
  cid INT PRIMARY KEY AUTO_INCREMENT,
  cname VARCHAR(10)
);
DROP TABLE `category`;
#非空约束
CREATE TABLE `category`(
  cid INT PRIMARY KEY AUTO_INCREMENT,
  cname VARCHAR(10) NOT NULL
);
DROP TABLE `category`;
#唯一约束
CREATE TABLE `category`(
  cid INT PRIMARY KEY AUTO_INCREMENT,
  cname VARCHAR(10) UNIQUE
);
DROP TABLE `category`;
#联合主键
CREATE TABLE `person`(
  xing VARCHAR(10),
  ming VARCHAR(10),
  city VARCHAR(10),
  PRIMARY KEY(xing,ming)
);
DROP TABLE `person`;