/*
  多表查询_数据准备
*/
#分类表
CREATE TABLE category (
  cid VARCHAR(32) PRIMARY KEY ,
  cname VARCHAR(50)
);

#商品表
CREATE TABLE products(
  pid VARCHAR(32) PRIMARY KEY ,
  pname VARCHAR(50),
  price DOUBLE,
  flag VARCHAR(2), #是否上架标记为：1表示上架、0表示下架
  category_id VARCHAR(32), -- 外键
  CONSTRAINT products_fk FOREIGN KEY (category_id) REFERENCES category (cid)
);
#分类数据
INSERT INTO category(cid,cname) VALUES('c001','家电');
INSERT INTO category(cid,cname) VALUES('c002','服饰');
INSERT INTO category(cid,cname) VALUES('c003','化妆品');
#商品数据
INSERT INTO products(pid, pname,price,flag,category_id) VALUES('p001','联想',5000,'1','c001');
INSERT INTO products(pid, pname,price,flag,category_id) VALUES('p002','海尔',3000,'1','c001');
INSERT INTO products(pid, pname,price,flag,category_id) VALUES('p003','雷神',5000,'1','c001');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p004','JACK JONES',800,'1','c002');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p005','真维斯',200,'1','c002');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p006','花花公子',440,'1','c002');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p007','劲霸',2000,'1','c002');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p008','香奈儿',800,'1','c003');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p009','相宜本草',200,'1','c003');

/*
  多表查询_交叉查询
*/
SELECT * FROM category,products;

/*
  多表查询_内连接
*/
#查询具体的商品信息->隐式内连接
SELECT * FROM category c1,products p1 WHERE c1.cid = p1.category_id;
#查询具体的商品信息->显示内连接
SELECT * FROM category c1 JOIN products p1 on c1.cid = p1.category_id;
#用显示内连接的方式查询"化妆品"的商品信息
SELECT * FROM category c1 JOIN products p1 on c1.cid = p1.category_id WHERE c1.cname = '化妆品';
SELECT * FROM category c1 JOIN products p1 on c1.cid = p1.category_id AND c1.cname = '化妆品';

/*
  多表查询_外连接
*/
#查询所有的商品信息 左外连接
SELECT * FROM category c1 LEFT JOIN products p1 on c1.cid = p1.category_id;
#查询所有的商品信息 右外连接
SELECT * FROM category c1 RIGHT JOIN products p1 on c1.cid = p1.category_id;

/*
  多表查询_子查询
*/
#查询products表中'化妆品'的商品信息
SELECT * FROM products WHERE category_id = (SELECT cid FROM category WHERE cname = '化妆品');
#查询products表中化妆品和家电的商品信息
SELECT * FROM products WHERE category_id IN (SELECT cid FROM category WHERE cname IN ('化妆品','家电'));
#查询化妆品的所有商品信息
SELECT * FROM (SELECT * FROM category WHERE cname = '化妆品') c,products p WHERE c.`cid` = p.`category_id`;
#查询所有化妆品和家电的商品信息
SELECT * FROM (SELECT * FROM category WHERE cname IN ('家电','化妆品')) c,products p WHERE c.`cid` = p.`category_id`