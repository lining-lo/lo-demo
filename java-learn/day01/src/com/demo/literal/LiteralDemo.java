package com.demo.literal;

public class LiteralDemo {
    public static void main(String[] args) {
        // 目标: 学会字面量的书写格式。

        // 1、整数 小数
        System.out.println(23);
        System.out.println(9.9);

        // 2、字符: 必须单引号围起来，有且仅有一个
        System.out.println('a');
        // System.out.println(''); // 报错
        System.out.println(' ');
        System.out.println('中');
        // System.out.println('中国'); // 报错

        // 特殊字符
        System.out.println("我是" + '\t' + "dlei"); // \t代表一个Tab空格
        System.out.println("我是" + '\n' + "dlei"); // \n代表一个换行

        // 3、字符串: 必须使用双引号围起来，里面的内容可以随意
        System.out.println("");
        System.out.println("我爱你中国666 999");
        System.out.println(" ");

        // 4、真假 布尔值 true false
        System.out.println(true);
        System.out.println(false);
    }
}

