package com.demo.type;

public class TypeConversionDemo2 {
    public static void main(String[] args) {
        // 目标：理解类型转换-自动类型转换。
        byte a = 12;
        int b = a; // 自动类型转换。
        System.out.println(a);
        System.out.println(b);

        int i = 999;
        double j = i; // 自动类型转换。
        System.out.println(i);
        System.out.println(j); // 999.0

        char ch = 'b'; // 98
        int it = ch; // 自动类型转换。
        System.out.println(ch);
        System.out.println(it);
    }
}

