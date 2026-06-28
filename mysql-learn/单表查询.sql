/*
  单表查询_数据准备
*/
#创建商品表
create table product(
	pid int primary key,
	pname varchar(20),
	price double
);
#插入数据
INSERT INTO product(pid,pname,price) VALUES(1,'联想',5000);
INSERT INTO product(pid,pname,price) VALUES(2,'海尔',3000);
INSERT INTO product(pid,pname,price) VALUES(3,'雷神',5000);
INSERT INTO product(pid,pname,price) VALUES(4,'JACK JONES',800);
INSERT INTO product(pid,pname,price) VALUES(5,'真维斯',200);
INSERT INTO product(pid,pname,price) VALUES(6,'花花公子',440);
INSERT INTO product(pid,pname,price) VALUES(7,'劲霸',2000);
INSERT INTO product(pid,pname,price) VALUES(8,'香奈儿',800);
INSERT INTO product(pid,pname,price) VALUES(9,'相宜本草',200);
INSERT INTO product(pid,pname,price) VALUES(10,'面霸',5);
INSERT INTO product(pid,pname,price) VALUES(11,'好想你枣',56);
INSERT INTO product(pid,pname,price) VALUES(12,'香飘飘奶茶',1);
INSERT INTO product(pid,pname,price) VALUES(13,'果9',1);

/*
  单表查询_简单查询
*/
#查询product所有数据
SELECT * FROM product;
#查询product 所有数据,展示pname和pid
SELECT pid,pname FROM product;
#去重复值
SELECT DISTINCT(price) FROM product;
#查询所有数据,给price列中所有的数据+100
SELECT pid,pname,price+100 FROM product;
#取别名
SELECT pid,pname,price+100 `newprice` FROM product;

/*
  单表查询_条件查询
*/
#查询商品名为'花花公子'的商品所有信息
SELECT * FROM product WHERE pname = '花花公子';
#查询价格为800的商品
SELECT * FROM product WHERE price = 800;
#查询商品价格大于60元的所有商品信息
SELECT * FROM product WHERE price > 60;
#查询商品价格在200-1000之间的所有商品信息
SELECT * FROM product WHERE price BETWEEN 200 AND 1000;
#查询商品价格是200或者800的商品
SELECT * FROM product WHERE price in (200,800);
#查询以'香'开头的商品
SELECT * FROM product WHERE pname LIKE '香%';
#查询含有'霸'的商品
SELECT * FROM product WHERE pname LIKE '%霸%';
#查询商品名为NULL的
SELECT * FROM product WHERE pname is NULL;
#查询商品名不为NULL的
SELECT * FROM product WHERE pname is NOT NULL;

/*
  单表查询_排序查询
*/
#使用价格排序(降序)
SELECT * FROM product ORDER BY price DESC;
#使用价格排序(升序)
SELECT * FROM product ORDER BY price;
#显示商品的价格(去重复),并排序(降序)
SELECT DISTINCT(price) FROM product ORDER BY price DESC;

/*
  单表查询_聚合查询
*/
-- 统计product的总记录数
SELECT COUNT(*) FROM product;
-- 查询所有商品的价格总和
SELECT SUM(price) FROM product;
-- 查询pid为1,3,7 商品的价格平均值
SELECT AVG(price) FROM product WHERE pid IN (1,3,7);
-- 查询商品的最高价格以及最低价格
SELECT MAX(price),MIN(price) FROM product;

/*
  单表查询_分组查询
*/
#查询相同商品的价格总和
SELECT pname,sum(price) FROM product GROUP BY pname;
#查询相同商品的价格总和并排序
SELECT pname,sum(price) newprice FROM product GROUP BY pname ORDER BY newprice;
#查询相同商品的价格总和,再展示出价格总和大于等于2000的商品
SELECT pname,sum(price) newprice FROM product GROUP BY pname HAVING newprice >= 200;

/*
  单表查询_分页查询
*/
#第一页
SELECT * FROM product LIMIT 0,5;
#第二页
SELECT * FROM product LIMIT 5,5;
#第三页
SELECT * FROM product LIMIT 10,5;

