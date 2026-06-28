/*
  事务
*/
#创建表
CREATE TABLE account(
  name VARCHAR(10),
  money INT
);
#插入数据
INSERT INTO account VALUES ('rose',10000),('jack',10000);
#开启事务
BEGIN;
#执行操作
UPDATE account SET money = money-1000 WHERE `name` = 'rose';
UPDATE account SET money = money+1000 WHERE `name` = 'jack';
#提交事务
COMMIT;
#回滚事务
ROLLBACK;
