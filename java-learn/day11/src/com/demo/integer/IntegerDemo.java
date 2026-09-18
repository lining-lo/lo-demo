package com.demo.integer;

import java.util.ArrayList;

public class IntegerDemo {
    /*
        将基本数据类型, 包装成类 (变成引用数据类型)

        byte            Byte
        short           Short
        int             Integer
        long            Long
        char            Character
        float           Float
        double          Double
        boolean         Boolean

        手动装箱: 手动调用 Integer.valueOf() 方法, 将基本数据类型, 手动包装为类
        手动拆箱: 手动调用 Integer中的 intValue() 方法, 将包装类对象, 转换为基本数据类型

        自动拆装箱: 基本数据类型和对应的包装类, 可以直接运算, 操作起来非常便捷
     */
    public static void main(String[] args) {
        int i1 = 10;
        Integer i2 = 20;

        int result = i1 + i2;
    }
}
