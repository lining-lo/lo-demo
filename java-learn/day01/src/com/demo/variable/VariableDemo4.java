package com.demo.variable;

public class VariableDemo4 {
    public static void main(String[] args) {
        // 目标：变量的详解。
        // 1、字符的存储原理：存储的是字符的编号的二进制。
        System.out.println('a' + 1); // 98
        System.out.println('A' + 1); // 66
        System.out.println('0' + 1); // 49

        // 2、程序中书写 二进制 八进制  十六进制。
        int a1 = 0B11111010; // 二进制 0B 0b开头
        System.out.println(a1); // 250

        int a2 = 0372; // 八进制 0开头
        System.out.println(a2);

        int a3 = 0XFA; // 十六进制0X 0x开头
        System.out.println(a3);
    }
}
