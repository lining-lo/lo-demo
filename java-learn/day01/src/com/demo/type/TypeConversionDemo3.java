package com.demo.type;

public class TypeConversionDemo3 {
    public static void main(String[] args) {
        // 目标：掌握表达式的自动类型转换。
        byte a = 10;
        int b = 20;
        long c = 30;
        // int result = a + b + c + 10; // 报错
        long result = a + b + c + 10;
        System.out.println(result);

        // long result2 = c + b + 3.14; // 报错
        double result2 = c + b + 3.14;
        System.out.println(result2);

        byte a1 = 110;
        byte a2 = 120;
        // byte a3 = a1 + a2; // 报错
        int a3 = a1 + a2;
        System.out.println(a3);
    }
}
