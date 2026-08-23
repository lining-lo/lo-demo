package com.demo.if_;

import java.util.Scanner;

public class IfDemo3 {
    public static void main(String[] args) {
        //需求:键盘录入用户名和用户密码, 如果用户名为”小哈“，密码为 ”123456“,
        // 程序输出用户登录成功，否则输出密码或者用户名有误
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入你的用户名：");
        String userName = sc.next();
        System.out.println("请输入你的用密码：");
        String password = sc.next();
        // 判断用户输入的用户名（小哈）和密码（123456）是否正确
        // TODO == 只能判断两个字符串的地址是否相同，内容是无法判断
        //if(userName == okUserName && password == okPassword){
        // TODO 变量1.equals(变量2或者值) 判断两个字符串是否内容一致
        if(userName.equals("小哈") && password.equals("123456")){
            System.out.println(userName + "，欢迎登录！");
        } else {
            System.out.println("用户名或者密码错误！");
        }
    }
}
