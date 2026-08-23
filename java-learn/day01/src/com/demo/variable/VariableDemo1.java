package com.demo.variable;

public class VariableDemo1 {
    public static void main(String[] args) {
        // 目标: 认识变量，搞清楚为啥要用变量。
        // 定义格式: 数据类型 变量名 = 初始数据;
        int age = 18;
        System.out.println(age);

        double score = 99.5;
        System.out.println(score);

        System.out.println("----------为啥要用变量呢？--------------");
        // 使用变量记住数据再处理，程序的维护性更好更灵活。
        int a = 999;
        System.out.println(a);
        System.out.println(a);
        System.out.println(a);
        System.out.println(a);
        System.out.println(a);
        System.out.println(a);
    }
}
