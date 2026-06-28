/*
  常用函数_数据准备
*/
#
#创建数据表t_user
CREATE TABLE t_user (
  id int(11) NOT NULL AUTO_INCREMENT,
  uname varchar(40) DEFAULT NULL,
  age int(11) DEFAULT NULL,
  sex int(11) DEFAULT NULL,
  PRIMARY KEY (id)
);
#插入数据
insert  into t_user values (null,'zs',18,1);
insert  into t_user values (null,'ls',20,0);
insert  into t_user values (null,'ww',23,1);
insert  into t_user values (null,'zl',24,1);
insert  into t_user values (null,'lq',15,0);
insert  into t_user values (null,'hh',12,0);
insert  into t_user values (null,'wzx',60,null);
insert  into t_user values (null,'lb',null,null);

/*
  常用函数_字符串函数
*/
#使用concat函数显示出 你好uname 的结果
SELECT CONCAT('你好',uname),age,sex FROM t_user;
#使用concat_ws函数显示出 你好,uname 的结果
SELECT CONCAT_WS(',','你好',uname) uname,age,sex FROM t_user;
#查询t_user,uname变成大写
SELECT UPPER(uname),age,sex FROM t_user;
#查询t_user,uname变成小写
SELECT LOWER(uname),age,sex FROM t_user;
#将用户id为9的用户的姓名的两边空白符移除
SELECT TRIM(uname),age,sex FROM t_user WHERE id = 9;
#获取 hello,world 从第二个字符开始的完整子串
SELECT SUBSTRING('hello,world',2);
#获取 hello,world 从第二个字符开始但是长度为4的子串
SELECT SUBSTRING('hello,world',2,4);

/*
  常用函数_数值函数
*/
#获取 -12 的绝对值
SELECT ABS(-12);
#将 -11.2 向上取整
SELECT CEIL(-11.2);
#将 1.6 向下取整
SELECT FLOOR(1.6);
#获得2的2次幂的值
SELECT POW(2,2);
#获得一个在0-100之间的随机数
SELECT RAND()*100;

/*
  常用函数_日期函数
*/
#获取当前的日期(仅仅需要年月日)
SELECT CURRENT_DATE();
#获取当前的时间（仅仅需要时分秒）
SELECT CURRENT_TIME();
#获取当前日期时间（包含年月日时分秒）
SELECT NOW();
#获取到10月1日还有多少天
SELECT DATEDIFF('2026-10-1',NOW());

/*
  常用函数_流程函数
*/
#获取用户的姓名、性别，如果性别为1则显示’男’，否则显示’女’；要求使用if函数查询
SELECT uname,age,IF(sex=1,'男','女') sex FROM t_user;
#获取用户的姓名、性别，如果性别为null则显示为0；要求使用ifnull函数查询
SELECT uname,age,IFNULL(sex,0) sex FROM t_user;
#如果age<=12,显示儿童,如果age<=18,显示少年,如果age<=40,显示中年,否则显示老年
SELECT
  uname,
  CASE
    WHEN age <= 12 THEN
      '儿童'
    WHEN age <= 18 THEN
      '少年'
    WHEN age <= 40 THEN
      '中年'
    ELSE
      '老年'
  END age,
  sex
FROM
  t_user;