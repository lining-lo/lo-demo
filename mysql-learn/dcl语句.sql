/*
  分配用户:
    create:创建
    user:用户
    'user1'@'localhost' : 用户名以及可以访问的主机地址
    IDENTIFIED BY '123' : 分配密码
    
    %:可以在任意远程主机上登录
*/
-- user1用户只能在localhost这个IP登录mysql服务器
CREATE USER 'user1'@'localhost' IDENTIFIED BY '123';
-- user2用户可以在任何电脑上登录mysql服务器
CREATE USER 'user2'@'%' IDENTIFIED BY '123';


/*
   grant:分配权限关键字
   grant后面跟的就是具体的操作权限:select insert update等,如果分配所有权限就写ALL
   
   on:后面跟的是数据库名字 -> 指定啥数据库那么用此用户登录就只能看到哪个数据库名字
   
   `220706_mysql03`.* -> 指定库中所有的表 * 代表所有,如果想要看到所有的库以及所有的表我们就写*.*
   
   to:指明此权限要给的用户
*/
-- 给用户1分配权限
GRANT SELECT ON `230222_day02_2`.* TO 'user1'@'localhost';

-- 给用户2分配权限
GRANT ALL ON *.* TO 'user2'@'%';

/*
  drop:删除用户关键字
*/
DROP USER 'user2'@'%';
DROP USER 'user1'@'localhost';