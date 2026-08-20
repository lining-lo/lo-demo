package com.demo.Variable;

public class VariableDemo3 {
    public static void main(String[] args) {
        // 目标：理解变量的注意事项。
        // 1、变量必须先定义才能使用。
//        age = 23;
//        System.out.println(age);

        // 2、变量是什么类型就只能装什么类型的数据。
        int a = 23;
        a = 24;
//        a = 9.9; // 报错

        // 3、变量从定义开始到 }结束有效
        // 同一个范围内，不能定义两个名称一样的变量
        System.out.println(a);
        {
            int b = 23;
            System.out.println(b);
        }
//        System.out.println(b);// 报错
        int b = 234;

        // 4、变量定义时可以不赋值 但是使用时必须有值，否则报错
        int number;
        number = 324;
        System.out.println(number);
    }
}
